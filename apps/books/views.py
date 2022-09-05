from django.views.generic import *

# 
from .models import *


class BookListView(ListView):
    model = Book
    template_name = 'books/list.html'
    context_object_name = 'books'

    def get_queryset(self):
        kword = self.request.GET.get('kword', '')
        date1 = self.request.GET.get('date1', '')
        date2 = self.request.GET.get('date2', '')

        if date1 and date2:
            return Book.objects.search_books2(date1, date2)

        return Book.objects.search_books(kword)

class BookCategoriesListView(ListView):
    model = Book
    template_name = 'books/list_books_category.html'
    context_object_name = 'books_categories'

    def get_queryset(self):
        return Book.objects.list_books_by_category(3)



class BookDetailView(DetailView):
    model = Book
    template_name = "books/detail.html"
