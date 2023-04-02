from django.contrib import admin
from invoice.models import InvoiceModel


@admin.register(InvoiceModel)
class InvoiceModelAdmin(admin.ModelAdmin):
    pass
