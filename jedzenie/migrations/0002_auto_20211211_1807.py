# Generated by Django 3.2.8 on 2021-12-11 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzenie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restauracja',
            name='Kategoria',
            field=models.CharField(blank=True, max_length=45),
        ),
        migrations.AlterField(
            model_name='restauracja',
            name='Nazwa',
            field=models.CharField(max_length=45, unique=True),
        ),
        migrations.AlterField(
            model_name='zamowienie',
            name='Telefon',
            field=models.CharField(max_length=45),
        ),
    ]