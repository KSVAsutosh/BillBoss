from django.urls import path

from . import views

urlpatterns = [

    path(
        '',
        views.debt_list,
        name='debt_list'
    ),

    path(
        'add/',
        views.add_debt,
        name='add_debt'
    ),

    path(
        'detail/<int:pk>/',
        views.debt_detail,
        name='debt_detail'
    ),

    path(
        'payment/<int:pk>/',
        views.add_payment,
        name='add_payment'
    ),
]