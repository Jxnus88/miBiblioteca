# Generated by Django 5.1.5 on 2025-02-06 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibrosApp', '0006_alter_libro_genero_alter_libro_sub_genero_a_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='genero',
            field=models.CharField(choices=[('novela', 'Novela'), ('ficcion', 'Ficción'), ('no_ficcion', 'No Ficción'), ('alta_fantasia', 'Alta Fantasía'), ('fantasia', 'Fantasía'), ('ciencia_ficcion', 'Ciencia Ficción'), ('biografia', 'Biografía'), ('historia', 'Historia'), ('romance', 'Romance'), ('terror', 'Terror'), ('aventura', 'Aventura'), ('misterio', 'Misterio')], max_length=30),
        ),
        migrations.AlterField(
            model_name='libro',
            name='sub_genero_a',
            field=models.CharField(blank=True, choices=[('aventura', 'Aventura'), ('fantasia', 'Fantasía'), ('literatura_fantastica', 'Literatura Fantástica'), ('aventura_fantastica', 'Aventura Fantástica'), ('drama', 'Drama'), ('accion', 'Acción'), ('thriller', 'Thriller'), ('comedia', 'Comedia'), ('psicologico', 'Psicológico'), ('romance_fantastico', 'Romance Fantástico'), ('ficcion_historica', 'Ficción Histórica'), ('terror_psicologico', 'Terror Psicológico')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='libro',
            name='sub_genero_b',
            field=models.CharField(blank=True, choices=[('aventura', 'Aventura'), ('fantasia', 'Fantasía'), ('literatura_fantastica', 'Literatura Fantástica'), ('aventura_fantastica', 'Aventura Fantástica'), ('drama', 'Drama'), ('accion', 'Acción'), ('thriller', 'Thriller'), ('comedia', 'Comedia'), ('psicologico', 'Psicológico'), ('romance_fantastico', 'Romance Fantástico'), ('ficcion_historica', 'Ficción Histórica'), ('terror_psicologico', 'Terror Psicológico')], max_length=30, null=True),
        ),
    ]
