from django.contrib import admin

from .models import (
    Debt,
    DebtPayment
)


@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):

    list_display = (
        'person_name',
        'debt_type',
        'amount',
        'remaining_amount',
        'due_date',
        'is_closed'
    )


@admin.register(DebtPayment)
class DebtPaymentAdmin(admin.ModelAdmin):

    list_display = (
        'debt',
        'amount',
        'payment_date'
    )