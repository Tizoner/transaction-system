import json
from typing import List

from celery import shared_task
from django.db.transaction import atomic
from django.utils import timezone
from pydantic import BaseModel

from .models import Transaction


class Task(BaseModel):
    transaction_id: int


def get_tasks() -> List[Task]:
    now = timezone.now()
    tasks = []
    for transaction in Transaction.objects.filter(
        status=Transaction.Status.UNPROCESSED
    ):
        client = transaction.client
        process_at = timezone.localtime(transaction.process_at, client.timezone)
        if timezone.localtime(now, client.timezone) >= process_at:
            tasks.append(Task(transaction_id=transaction.id))
    return tasks


@shared_task
def process_transaction(task_data: str):
    """Process single transaction.

    Args:
        task_data (str): JSON string with task data
    """
    task = Task.parse_obj(json.loads(task_data))
    transaction = Transaction.objects.get(id=task.transaction_id)
    client = transaction.client
    new_balance = client.balance + (
        transaction.amount if transaction.refill else -transaction.amount
    )
    with atomic():
        if new_balance < 0:
            transaction.status = Transaction.Status.BLOCKED
        else:
            client.balance = new_balance
            client.save(update_fields=["balance"])
            transaction.status = Transaction.Status.PROCESSED
        transaction.save(update_fields=["status"])


def add_task(task: Task):
    """Add a task to the queue.

    Args:
        task (Task): Task instance
    """
    process_transaction.apply_async(args=[task.json()])


@shared_task
def check_transactions():
    """Scheduled task for CELERY_BEAT_SCHEDULE. Search for transactions to process at the current time"""
    any(map(add_task, get_tasks()))
