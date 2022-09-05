# Generated by Django 3.2.6 on 2022-09-04 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=50, verbose_name='Nombre Categoría')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'db_table': 'category',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Título')),
                ('date_published', models.DateField(verbose_name='Fecha Publicación')),
                ('front_page', models.ImageField(upload_to='portadas', verbose_name='Portada')),
                ('views', models.PositiveIntegerField()),
                ('authors', models.ManyToManyField(to='authors.Author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_book', to='books.category')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'db_table': 'book',
                'ordering': ['id'],
            },
        ),
    ]
