# Generated by Django 5.1.5 on 2025-02-06 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LibrosApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='libro',
            options={'ordering': ['fecha_publicacion'], 'verbose_name': 'Libro', 'verbose_name_plural': 'Libros'},
        ),
    ]
