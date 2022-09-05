from django.db import models

from apps.books.models import Book
from apps.authors.models import Person
from apps.loans.managers import LoanManager


class Reader(Person):
    class Meta:
        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'
        ordering = ['-id']
        db_table = 'reader'


class Loan(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_loan')
    date_loan = models.DateField('Fecha Préstamo')
    date_return = models.DateField('Fecha Devolución', blank=True, null=True)
    is_returned = models.BooleanField('Devuelto', default=False)

    objects = LoanManager()

    class Meta:
        verbose_name = 'Préstamo'
        verbose_name_plural = 'Préstamos'
        ordering = ['-id']
        db_table = 'loan'

    def __str__(self):
        return self.book.title

    def save(self, *args, **kwargs):
        """Realiza una disminución del stock de libros una vez se crea un prestamo"""
        self.book.stock -= 1
        self.book.save()
        super(Loan, self).save(*args, **kwargs)
        