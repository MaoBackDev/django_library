from django.urls import path

from apps.loans.views import *

urlpatterns = [
    path('loans/add/',AddLoanView.as_view(), name='add'),
    path('loans/add-multiple/',AddMultipleLoanView.as_view(), name='add_multiple'),
]