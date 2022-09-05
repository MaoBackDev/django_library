from multiprocessing.dummy import Manager
from django.db.models import Manager, Q, Count,Avg
from django.db.models.functions import *


class LoanManager(Manager):
    """Manager para préstamos"""

    def avg_readers_books(self):
        return self.filter(
            book__id=3
        ).aggregate(
            prom_age=Avg('reader__age')
        )

     # Uso de values() = Esta función realiza una consulta usando la sentencia group by
    def cant_books_loans(self):
        return self.values(
            'book',
            'reader'
        ).annotate(
            num_loans=Count('book'),
            title=Lower('book__title')
        )
