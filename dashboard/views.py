from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from transactions.models import Transaction


@login_required
def dashboard(request):

    income = Transaction.objects.filter(
        user=request.user,
        transaction_type='income'
    ).aggregate(
        total=Sum('amount')
    )['total'] or 0

    expense = Transaction.objects.filter(
        user=request.user,
        transaction_type='expense'
    ).aggregate(
        total=Sum('amount')
    )['total'] or 0

    balance = income - expense

    recent_transactions = Transaction.objects.filter(
        user=request.user
    ).order_by('-date')[:5]

    context = {
        'income': income,
        'expense': expense,
        'balance': balance,
        'recent_transactions': recent_transactions
    }

    return render(
        request,
        'dashboard/dashboard.html',
        context
    )