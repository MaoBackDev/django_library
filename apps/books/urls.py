from django.urls import path
from .views import *

urlpatterns = [
    path('books/', BookListView.as_view(), name='books'),
    path('books-categories/', BookCategoriesListView.as_view(), name='books-categories'),
    path('detail/<int:pk>/', BookDetailView.as_view(), name='detail'),
]