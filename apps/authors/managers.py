from django.db import models
from django.db.models import Q
from .models import *


class AuthorManager(models.Manager):
    """Manager Author model"""

    def search_authors(self, kword):
        """Filtra los autores si contienen lo que se obtenga del parámetro kword"""
        result = self.filter(first_name__icontains=kword) 
        return result

    def search_authors2(self, kword):
        """Filtra los autores por nombre o apellido. S e hace uso de la función Q """
        result = self.filter(
           Q(first_name__icontains=kword) | Q(last_name__icontains=kword)
        ) 
        return result

    def search_authors3(self, kword):
        """Filtra los autores si contienen lo que se obtenga del parámetro kword pero excluyendo de acuerdo al parámetro que se indique"""
        result = self.filter(first_name__icontains=kword).exclude(age=56)
        return result

    def search_authors4(self, kword):
        """Filtra los autores si contienen lo que se obtenga del parámetro kword y además la edad sea mayor a 40 y menor a 60"""
        result = self.filter(
            age__gt=30,  #  la denotación __gt es igual al mayor que >
            age__lt=70  #  la denotación __lt es igual al menor que <
        ).order_by('last_name')
        return result