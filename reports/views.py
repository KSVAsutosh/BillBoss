from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.db.models.functions import ExtractMonth
from django.db.models.functions import ExtractYear

from transactions.models import Transaction


@login_required
def monthly_report(request):

    monthly_data = (
        Transaction.objects
        .filter(user=request.user)
        .annotate(month=ExtractMonth('date'))
        .values('month')
        .annotate(total=Sum('amount'))
        .order_by('month')
    )

    return render(
        request,
        'reports/monthly_report.html',
        {
            'monthly_data': monthly_data
        }
    )


@login_required
def yearly_report(request):

    yearly_data = (
        Transaction.objects
        .filter(user=request.user)
        .annotate(year=ExtractYear('date'))
        .values('year')
        .annotate(total=Sum('amount'))
        .order_by('year')
    )

    return render(
        request,
        'reports/yearly_report.html',
        {
            'yearly_data': yearly_data
        }
    )


@login_required
def category_report(request):

    category_data = (
        Transaction.objects
        .filter(
            user=request.user,
            transaction_type='expense'
        )
        .values('category__name')
        .annotate(total=Sum('amount'))
        .order_by('-total')
    )

    return render(
        request,
        'reports/category_report.html',
        {
            'category_data': category_data
        }
    )


@login_required
def analytics(request):

    total_income = (
        Transaction.objects
        .filter(
            user=request.user,
            transaction_type='income'
        )
        .aggregate(total=Sum('amount'))
        ['total'] or 0
    )

    total_expense = (
        Transaction.objects
        .filter(
            user=request.user,
            transaction_type='expense'
        )
        .aggregate(total=Sum('amount'))
        ['total'] or 0
    )

    balance = total_income - total_expense

    return render(
        request,
        'reports/analytics.html',
        {
            'income': total_income,
            'expense': total_expense,
            'balance': balance
        }
    )