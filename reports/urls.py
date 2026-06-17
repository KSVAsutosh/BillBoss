from django.urls import path
from . import views

urlpatterns = [

    path(
        'monthly/',
        views.monthly_report,
        name='monthly_report'
    ),

    path(
        'yearly/',
        views.yearly_report,
        name='yearly_report'
    ),

    path(
        'category/',
        views.category_report,
        name='category_report'
    ),

    path(
        'analytics/',
        views.analytics,
        name='analytics'
    ),
]