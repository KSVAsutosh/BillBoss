from django import forms
from .models import Transaction


class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction

        fields = [
            'account',
            'category',
            'transaction_type',
            'amount',
            'description',
            'date'
        ]

        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'rows': 3
                }
            )
        }