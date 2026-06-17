from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Account
from .forms import AccountForm


@login_required
def account_list(request):

    accounts = Account.objects.filter(
        user=request.user
    )

    total_balance = sum(
        account.balance
        for account in accounts
    )

    return render(
        request,
        'accounts_wallet/account_list.html',
        {
            'accounts': accounts,
            'total_balance': total_balance
        }
    )


@login_required
def add_account(request):

    if request.method == 'POST':

        form = AccountForm(request.POST)

        if form.is_valid():

            account = form.save(
                commit=False
            )

            account.user = request.user

            account.save()

            messages.success(
                request,
                'Account created successfully.'
            )

            return redirect(
                'account_list'
            )

    else:

        form = AccountForm()

    return render(
        request,
        'accounts_wallet/add_account.html',
        {
            'form': form
        }
    )


@login_required
def edit_account(request, pk):

    account = get_object_or_404(
        Account,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':

        form = AccountForm(
            request.POST,
            instance=account
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Account updated successfully.'
            )

            return redirect(
                'account_list'
            )

    else:

        form = AccountForm(
            instance=account
        )

    return render(
        request,
        'accounts_wallet/edit_account.html',
        {
            'form': form
        }
    )


@login_required
def delete_account(request, pk):

    account = get_object_or_404(
        Account,
        pk=pk,
        user=request.user
    )

    account.delete()

    messages.success(
        request,
        'Account deleted successfully.'
    )

    return redirect(
        'account_list'
    )