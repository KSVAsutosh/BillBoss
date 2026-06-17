from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):

    ACCOUNT_TYPES = [
        ('cash', 'Cash'),
        ('bank', 'Bank'),
        ('wallet', 'Wallet'),
        ('credit', 'Credit Card'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=100
    )

    account_type = models.CharField(
        max_length=20,
        choices=ACCOUNT_TYPES,
        default='cash'
    )

    balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    account_number = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    color = models.CharField(
        max_length=20,
        default='#0d6efd'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name