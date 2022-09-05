from django.shortcuts import render
from django.views.generic import *

# 
from .models import *


class ListAuthorsView(ListView):
    model = Author
    template_name = 'authors/list.html'
    context_object_name = 'authors'

    def get_queryset(self):
        """Obtiene la lista de autores a través del método GET. 
            Además, filtra por el campo first_name
        """
        kword = self.request.GET.get('kword','')
        return Author.objects.search_authors4(kword)