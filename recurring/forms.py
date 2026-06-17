from django import forms
from .models import RecurringTransaction


class RecurringTransactionForm(forms.ModelForm):

    class Meta:
        model = RecurringTransaction

        fields = [
            'title',
            'account',
            'category',
            'amount',
            'transaction_type',
            'frequency',
            'start_date',
            'next_due_date',
            'is_active'
        ]

        widgets = {
            'start_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),
            'next_due_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),
        }