from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.transaction_list,
        name='transaction_list'
    ),

    path(
        'add/',
        views.add_transaction,
        name='add_transaction'
    ),

    path(
        'edit/<int:pk>/',
        views.edit_transaction,
        name='edit_transaction'
    ),

    path(
        'detail/<int:pk>/',
        views.transaction_detail,
        name='transaction_detail'
    ),

    path(
        'delete/<int:pk>/',
        views.delete_transaction,
        name='delete_transaction'
    ),
]