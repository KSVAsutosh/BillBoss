from django.db import models
from django.contrib.auth.models import User


class UserSettings(models.Model):

    CURRENCY_CHOICES = [
        ('INR', 'Indian Rupee'),
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('GBP', 'British Pound'),
    ]

    THEME_CHOICES = [
        ('light', 'Light'),
        ('dark', 'Dark'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    currency = models.CharField(
        max_length=10,
        choices=CURRENCY_CHOICES,
        default='INR'
    )

    theme = models.CharField(
        max_length=10,
        choices=THEME_CHOICES,
        default='light'
    )

    email_notifications = models.BooleanField(
        default=True
    )

    budget_alerts = models.BooleanField(
        default=True
    )

    recurring_reminders = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.user.username