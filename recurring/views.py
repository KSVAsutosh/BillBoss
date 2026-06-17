from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import RecurringTransaction
from .forms import RecurringTransactionForm


@login_required
def recurring_list(request):

    recurring_transactions = (
        RecurringTransaction.objects
        .filter(user=request.user)
        .order_by('next_due_date')
    )

    return render(
        request,
        'recurring/recurring_list.html',
        {
            'recurring_transactions':
            recurring_transactions
        }
    )


@login_required
def add_recurring(request):

    if request.method == 'POST':

        form = RecurringTransactionForm(
            request.POST
        )

        if form.is_valid():

            recurring = form.save(
                commit=False
            )

            recurring.user = request.user

            recurring.save()

            messages.success(
                request,
                'Recurring transaction added successfully.'
            )

            return redirect(
                'recurring_list'
            )

    else:

        form = RecurringTransactionForm()

    return render(
        request,
        'recurring/add_recurring.html',
        {
            'form': form
        }
    )


@login_required
def edit_recurring(request, pk):

    recurring = get_object_or_404(
        RecurringTransaction,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':

        form = RecurringTransactionForm(
            request.POST,
            instance=recurring
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Recurring transaction updated successfully.'
            )

            return redirect(
                'recurring_list'
            )

    else:

        form = RecurringTransactionForm(
            instance=recurring
        )

    return render(
        request,
        'recurring/edit_recurring.html',
        {
            'form': form
        }
    )


@login_required
def delete_recurring(request, pk):

    recurring = get_object_or_404(
        RecurringTransaction,
        pk=pk,
        user=request.user
    )

    recurring.delete()

    messages.success(
        request,
        'Recurring transaction deleted successfully.'
    )

    return redirect(
        'recurring_list'
    )