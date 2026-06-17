from django.db import models
from django.contrib.auth.models import User


class Debt(models.Model):

    DEBT_TYPES = [
        ('borrowed', 'Borrowed'),
        ('lent', 'Lent'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    person_name = models.CharField(
        max_length=150
    )

    debt_type = models.CharField(
        max_length=20,
        choices=DEBT_TYPES
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    start_date = models.DateField()

    due_date = models.DateField()

    remaining_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    is_closed = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.person_name


class DebtPayment(models.Model):

    debt = models.ForeignKey(
        Debt,
        on_delete=models.CASCADE,
        related_name='payments'
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    payment_date = models.DateField()

    note = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.debt.person_name} - {self.amount}"