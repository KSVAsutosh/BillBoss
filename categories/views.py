from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Category
from .forms import CategoryForm


@login_required
def category_list(request):

    categories = Category.objects.filter(
        user=request.user
    ).order_by('name')

    return render(
        request,
        'categories/category_list.html',
        {
            'categories': categories
        }
    )


@login_required
def add_category(request):

    if request.method == 'POST':

        form = CategoryForm(request.POST)

        if form.is_valid():

            category = form.save(
                commit=False
            )

            category.user = request.user

            category.save()

            messages.success(
                request,
                'Category added successfully.'
            )

            return redirect(
                'category_list'
            )

    else:

        form = CategoryForm()

    return render(
        request,
        'categories/add_category.html',
        {
            'form': form
        }
    )


@login_required
def edit_category(request, pk):

    category = get_object_or_404(
        Category,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':

        form = CategoryForm(
            request.POST,
            instance=category
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Category updated successfully.'
            )

            return redirect(
                'category_list'
            )

    else:

        form = CategoryForm(
            instance=category
        )

    return render(
        request,
        'categories/edit_category.html',
        {
            'form': form
        }
    )


@login_required
def delete_category(request, pk):

    category = get_object_or_404(
        Category,
        pk=pk,
        user=request.user
    )

    category.delete()

    messages.success(
        request,
        'Category deleted successfully.'
    )

    return redirect(
        'category_list'
    )