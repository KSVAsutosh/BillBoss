from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Budget
from .forms import BudgetForm


@login_required
def budget_list(request):

    budgets = Budget.objects.filter(
        user=request.user
    ).order_by('-year', '-month')

    return render(
        request,
        'budgets/budget_list.html',
        {
            'budgets': budgets
        }
    )


@login_required
def add_budget(request):

    if request.method == 'POST':

        form = BudgetForm(request.POST)

        if form.is_valid():

            budget = form.save(
                commit=False
            )

            budget.user = request.user

            budget.save()

            messages.success(
                request,
                'Budget added successfully.'
            )

            return redirect(
                'budget_list'
            )

    else:

        form = BudgetForm()

    return render(
        request,
        'budgets/add_budget.html',
        {
            'form': form
        }
    )


@login_required
def edit_budget(request, pk):

    budget = get_object_or_404(
        Budget,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':

        form = BudgetForm(
            request.POST,
            instance=budget
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Budget updated successfully.'
            )

            return redirect(
                'budget_list'
            )

    else:

        form = BudgetForm(
            instance=budget
        )

    return render(
        request,
        'budgets/edit_budget.html',
        {
            'form': form
        }
    )


@login_required
def delete_budget(request, pk):

    budget = get_object_or_404(
        Budget,
        pk=pk,
        user=request.user
    )

    budget.delete()

    messages.success(
        request,
        'Budget deleted successfully.'
    )

    return redirect(
        'budget_list'
    )