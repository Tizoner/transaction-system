from django.contrib import admin

from .models import Client, Transaction


class CustomModelAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(CustomModelAdmin, self).__init__(model, admin_site)


@admin.register(Client)
class ClientAdmin(CustomModelAdmin):
    search_fields = "id", "balance"
    list_filter = ("timezone",)


@admin.register(Transaction)
class TransactionAdmin(CustomModelAdmin):
    search_fields = "id", "amount"
    list_filter = "status", "refill", "created_at", "process_at", "client"
