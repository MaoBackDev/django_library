from django.db import models

from .managers import AuthorManager

class Person(models.Model):
    first_name = models.CharField('Nombre', max_length=80)
    last_name = models.CharField('Apellido', max_length=80)
    nationality = models.CharField('Nacionalidad', max_length=80)
    age = models.PositiveIntegerField()
    
    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Author(Person):
    # nick_name = models.CharField('Pseudónimo', max_length=50, blank=True)
    objects = AuthorManager()

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['-id']
        db_table = 'author'

    