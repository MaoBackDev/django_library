import datetime
from django.db.models import Manager,Count

from .models import *

class BookManager(Manager):
    
    def search_books(self, kword):
        query = self.filter(
            title__icontains=kword
        )
        return query

    
    def search_books2(self, date1, date2):
        """Filtra los libros publicados en un rango de fechas"""

        # formato de fecha yyyy-mm-dd --> 2020-09-02
        date1_format = datetime.datetime.strptime(date1, "%Y-%m-%d").date()  
        date2_format = datetime.datetime.strptime(date2, "%Y-%m-%d").date()

        query = self.filter(
            date_published__range=(date1_format, date2_format)
        )
        return query

    def list_books_by_category(self, category):
        return self.filter(
            category__id=category
        ).order_by('title')

    def add_author_book(self,book_id, author_id):
        """Agragar un author a un libro"""
        book = self.get(id=book_id)
        book.authors.add(author_id)
        return book


    # Uso de agregate() = Es útil cuando se desea obtener una operación global. 
    # select count(*) AS "Num_préstamos" from loans_loan
    def num_books_loan(self):
        """Retorna el número de préstamos realizados"""
        return self.aggregate(
            num_loans=Count('book_loan')
        )


class CategoryManager(Manager):
    """Manager para el modelo categoría"""

    def list_categories_by_author(self, author):
        return self.filter(
            category_book__authors__id=author
        ).distinct()


    # annotate: es el equivalente a una consulta agrupada por un elemento.
    # select bc.name_category, count(b.category_id)
    # from books_category AS "bc"
    # inner join books_book AS "b"
    # on bc.id = b.category_id
    # group by bc.name_category
    
    def list_categories_books(self):
        """Cuenta la cantidad de libros registrados en cada categoría"""
        result = self.annotate(
            num_books=Count('category_book') 
        )
        for r in result:
            print('-----------')
            print(r,r.num_books)

        return result
        
