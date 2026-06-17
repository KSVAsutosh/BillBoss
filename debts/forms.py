from django import forms

from .models import (
    Debt,
    DebtPayment
)


class DebtForm(forms.ModelForm):

    class Meta:
        model = Debt

        fields = [
            'person_name',
            'debt_type',
            'amount',
            'description',
            'start_date',
            'due_date'
        ]

        widgets = {
            'start_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'due_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }


class DebtPaymentForm(forms.ModelForm):

    class Meta:
        model = DebtPayment

        fields = [
            'amount',
            'payment_date',
            'note'
        ]

        widgets = {
            'payment_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }