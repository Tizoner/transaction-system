from django.db.models.signals import post_save
from django.dispatch import receiver

from .tasks import Task, add_task


@receiver(post_save, sender="api.Transaction")
def on_post_save_transaction(sender, instance, created, **kwargs):
    if created and instance.amount < 1000:
        add_task(Task(transaction_id=instance.id))
