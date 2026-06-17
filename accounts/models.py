from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    THEME_CHOICES = [
        ('light', 'Light'),
        ('dark', 'Dark'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    profile_picture = models.ImageField(
        upload_to='profiles/',
        default='profiles/default.png',
        blank=True
    )

    currency = models.CharField(
        max_length=10,
        default='INR'
    )

    theme = models.CharField(
        max_length=10,
        choices=THEME_CHOICES,
        default='light'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username