# Generated by Django 4.1.4 on 2023-02-01 19:05

import django.db.models.deletion
import timezone_field.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("balance", models.PositiveBigIntegerField(default=0)),
                (
                    "timezone",
                    timezone_field.fields.TimeZoneField(
                        choices_display="WITH_GMT_OFFSET"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.PositiveIntegerField(
                        choices=[(0, "Unprocessed"), (1, "Blocked"), (2, "Processed")],
                        default=0,
                    ),
                ),
                ("refill", models.BooleanField()),
                ("amount", models.PositiveBigIntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("process_at", models.DateTimeField(auto_now_add=True)),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="api.client"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
