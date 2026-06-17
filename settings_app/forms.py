from django import forms
from .models import UserSettings


class UserSettingsForm(forms.ModelForm):

    class Meta:
        model = UserSettings

        fields = [
            'currency',
            'theme',
            'email_notifications',
            'budget_alerts',
            'recurring_reminders'
        ]