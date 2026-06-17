from django.db import models
from django.contrib.auth.models import User
from categories.models import Category


class Budget(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
    Category,
    on_delete=models.CASCADE,
    related_name='budgets'
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    month = models.IntegerField()

    year = models.IntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = (
            'user',
            'category',
            'month',
            'year'
        )

    def __str__(self):
        return (
            f"{self.category.name} - "
            f"{self.amount}"
        )