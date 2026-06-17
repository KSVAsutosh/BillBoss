from django.db import models
from django.contrib.auth.models import User

from categories.models import Category
from accounts_wallet.models import Account


class RecurringTransaction(models.Model):

    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    ]

    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=150
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    transaction_type = models.CharField(
        max_length=20,
        choices=TRANSACTION_TYPES
    )

    frequency = models.CharField(
        max_length=20,
        choices=FREQUENCY_CHOICES
    )

    start_date = models.DateField()

    next_due_date = models.DateField()

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title