# Generated by Django 3.2.6 on 2022-09-05 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0002_loan_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='stock',
        ),
    ]
