from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import (
    RegisterForm,
    ProfileUpdateForm,
    UserUpdateForm
)


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Account created successfully."
            )

            return redirect('login')

    else:
        form = RegisterForm()

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )


@login_required
def profile_view(request):

    if request.method == 'POST':

        user_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )

        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():

            user_form.save()
            profile_form.save()

            messages.success(
                request,
                "Profile updated successfully."
            )

            return redirect('profile')

    else:

        user_form = UserUpdateForm(
            instance=request.user
        )

        profile_form = ProfileUpdateForm(
            instance=request.user.profile
        )

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(
        request,
        'accounts/profile.html',
        context
    )