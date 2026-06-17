from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserSettings
from .forms import UserSettingsForm


@login_required
def settings_view(request):

    settings_obj, created = (
        UserSettings.objects.get_or_create(
            user=request.user
        )
    )

    if request.method == 'POST':

        form = UserSettingsForm(
            request.POST,
            instance=settings_obj
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Settings updated successfully.'
            )

            return redirect(
                'settings'
            )

    else:

        form = UserSettingsForm(
            instance=settings_obj
        )

    return render(
        request,
        'settings_app/settings.html',
        {
            'form': form
        }
    )