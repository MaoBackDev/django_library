from django.urls import path
# 
from .views import *


app_name = 'authors'

urlpatterns = [
    path('authors/', ListAuthorsView.as_view(), name='authors')
]