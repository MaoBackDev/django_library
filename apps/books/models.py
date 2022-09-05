from django.db import models
from django.db.models.signals import post_save

from PIL import Image

from apps.authors.models import Author
from .managers import CategoryManager, BookManager


class Category(models.Model):
    name_category = models.CharField('Nombre Categoría', max_length=50)
    objects = CategoryManager()

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-id']
        db_table = 'category'

    def __str__(self):
        return self.name_category


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_book')
    authors = models.ManyToManyField(Author)
    title = models.CharField('Título', max_length=80)
    date_published = models.DateField('Fecha Publicación')
    front_page = models.ImageField('Portada', upload_to='portadas')
    views = models.PositiveIntegerField()
    stock = models.IntegerField(default=0)

    objects = BookManager()

    class Meta:
        """Esta clase hace referencia a los métadatos, a su vez, un metadato es todo aquello que dentro del modelo no es un atributo 
            propio de la tabla en la base de datos. """

        # Metadatos para el admin de django
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['id']
        db_table = 'book'  # Asigna el nombre que tendrá la tabla en la base de datos

        # unique_together = ['title', 'date_published']  Crea una llave unica combinada. Evita la inserción de datos duplicados
        # Permite crear restricciones o validaciones sencillas para condicionar los registros en la base de datos
        # constraints= [
        #     models.CheckConstraint(check=models.Q(edad__gte=18), name='age_max_18')
        # ]

    def __str__(self):
        return self.title

# SIGNALS
def customize_image(sender, instance, **kwargs):

    if instance.front_page:
        front_page = Image.open(instance.front_page.path)
        front_page.save(instance.front_page.path, quality=20, optimize=True)
        

post_save.connect(customize_image, sender=Book)