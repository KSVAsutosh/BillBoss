from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import (
    Debt,
    DebtPayment
)

from .forms import (
    DebtForm,
    DebtPaymentForm
)


@login_required
def debt_list(request):

    debts = Debt.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'debts/debt_list.html',
        {
            'debts': debts
        }
    )


@login_required
def add_debt(request):

    if request.method == 'POST':

        form = DebtForm(request.POST)

        if form.is_valid():

            debt = form.save(
                commit=False
            )

            debt.user = request.user
            debt.remaining_amount = debt.amount

            debt.save()

            messages.success(
                request,
                'Debt record added.'
            )

            return redirect('debt_list')

    else:

        form = DebtForm()

    return render(
        request,
        'debts/add_debt.html',
        {
            'form': form
        }
    )


@login_required
def debt_detail(request, pk):

    debt = get_object_or_404(
        Debt,
        pk=pk,
        user=request.user
    )

    payments = debt.payments.all()

    return render(
        request,
        'debts/debt_detail.html',
        {
            'debt': debt,
            'payments': payments
        }
    )


@login_required
def add_payment(request, pk):

    debt = get_object_or_404(
        Debt,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':

        form = DebtPaymentForm(
            request.POST
        )

        if form.is_valid():

            payment = form.save(
                commit=False
            )

            payment.debt = debt
            payment.save()

            debt.remaining_amount -= payment.amount

            if debt.remaining_amount <= 0:
                debt.remaining_amount = 0
                debt.is_closed = True

            debt.save()

            messages.success(
                request,
                'Payment recorded.'
            )

            return redirect(
                'debt_detail',
                pk=debt.id
            )

    else:

        form = DebtPaymentForm()

    return render(
        request,
        'debts/add_payment.html',
        {
            'form': form,
            'debt': debt
        }
    )