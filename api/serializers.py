from rest_framework import serializers

from .fields import TimeZoneSerializerField
from .models import Client, Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = ("status",)


class ClientSerializer(serializers.ModelSerializer):
    timezone = TimeZoneSerializerField()

    class Meta:
        model = Client
        fields = tuple(field.name for field in model._meta.fields)
