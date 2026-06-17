from django.contrib import admin
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'account_type',
        'balance',
        'user',
        'created_at'
    )

    search_fields = (
        'name',
        'account_number'
    )

    list_filter = (
        'account_type',
        'created_at'
    )