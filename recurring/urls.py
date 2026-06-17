from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.recurring_list,
        name='recurring_list'
    ),

    path(
        'add/',
        views.add_recurring,
        name='add_recurring'
    ),

    path(
        'edit/<int:pk>/',
        views.edit_recurring,
        name='edit_recurring'
    ),

    path(
        'delete/<int:pk>/',
        views.delete_recurring,
        name='delete_recurring'
    ),
]