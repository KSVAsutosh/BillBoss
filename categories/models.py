from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=100
    )

    icon = models.CharField(
        max_length=100,
        default='bi-tag'
    )

    color = models.CharField(
        max_length=20,
        default='#0d6efd'
    )

    budget = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name