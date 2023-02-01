import itertools
from datetime import timedelta
from random import random

from django.db import models
from timezone_field import TimeZoneField
from ujson import dumps

from .utils import serialize_object


class BaseModel(models.Model):
    def __repr__(self):
        return dumps(
            self.to_dict(),
            indent=4,
            default=serialize_object,
            ensure_ascii=False,
            escape_forward_slashes=False,
        )

    def to_dict(self):
        data = {}
        options = self._meta
        for field in itertools.chain(options.concrete_fields, options.private_fields):
            data[field.name] = field.value_from_object(self)
        for field in options.many_to_many:
            data[field.name] = [i.id for i in field.value_from_object(self)]
        return data

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    class Meta:
        abstract = True


class Client(BaseModel):
    balance = models.PositiveBigIntegerField(default=0)
    timezone = TimeZoneField(choices_display="WITH_GMT_OFFSET")


class Transaction(BaseModel):
    class Status(models.IntegerChoices):
        UNPROCESSED = 0
        BLOCKED = 1
        PROCESSED = 2

    status = models.PositiveIntegerField(
        choices=Status.choices, default=Status.UNPROCESSED
    )
    refill = models.BooleanField()
    amount = models.PositiveBigIntegerField()
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    process_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.amount > 1000:
            if self.amount < 50000:
                self.process_at += timedelta(minutes=1)
            else:
                self.process_at += timedelta(hours=5) + timedelta(hours=18) * random()
        super().save(*args, **kwargs)
