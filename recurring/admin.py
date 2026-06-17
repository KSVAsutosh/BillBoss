from django.contrib import admin
from .models import RecurringTransaction


@admin.register(RecurringTransaction)
class RecurringTransactionAdmin(
    admin.ModelAdmin
):

    list_display = (
        'title',
        'amount',
        'frequency',
        'next_due_date',
        'is_active',
        'user'
    )

    list_filter = (
        'frequency',
        'is_active'
    )

    search_fields = (
        'title',
    )