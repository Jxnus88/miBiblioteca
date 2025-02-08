import os.path
from django.utils.text import slugify
from .choices import *
from django.db import models

# Modelo que representa a un autor de libros.
# Incluye su nombre, biografía e imagen asociada.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField()
    imagen = models.ImageField(upload_to='LibrosApp/autores', null=True, blank=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        db_table = "insertar_autor"

    # Sobrescribe el método de eliminación para eliminar la imagen asociada al autor.
    def delete(self, *args, **kwargs):
        if self.imagen and os.path.isfile(self.imagen.path):
            os.remove(self.imagen.path)
        super(Autor, self).delete(*args, **kwargs)

    def __str__(self):
        return self.nombre

# Modelo que representa un nombre de directorio.
# Se utiliza para asociar directorios a los libros.
class NombreDirectorio(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'NombreDirectorio'
        verbose_name_plural = 'NombreDirectorios'
        db_table = "seleccionar_nombre_directorio"

    def __str__(self):
        return self.nombre

# Modelo que representa un libro.
# Incluye información sobre el autor, género, subgéneros, editorial, etc.
class Libro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libro')
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=30, choices=GENERO_CHOICES)
    sub_genero_a = models.CharField(max_length=30, choices=SUBGENERO_CHOICES, blank=True, null=True)
    sub_genero_b = models.CharField(max_length=30, choices=SUBGENERO_CHOICES, blank=True, null=True)
    editorial = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    resumen = models.TextField()
    puntuacion_choice = models.IntegerField(choices=PUNTUACION_CHOICES, default=1)
    nombre_directorio = models.ForeignKey(NombreDirectorio, on_delete=models.CASCADE, related_name='libro', null=True)
    imagen = models.ImageField(upload_to='LibrosApp/libros', null=True, blank=True)
    imagen_background = models.ImageField(upload_to='', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        db_table = "insertar_libro"
        ordering = ['fecha_publicacion']

    # Sobrescribe el método de eliminación para eliminar las imágenes asociadas al libro.
    def delete(self, *args, **kwargs):
        if self.imagen and os.path.isfile(self.imagen.path):
            os.remove(self.imagen.path)
        super(Libro, self).delete(*args, **kwargs)

    # Sobrescribe el método de guardado para configurar el nombre de archivo de la imagen de fondo.
    def save(self, *args, **kwargs):
        if self.nombre_directorio:
            folder_name = slugify(self.nombre_directorio.nombre)
            if self.imagen_background:
                self.imagen_background.name = f'Background/{folder_name}/{self.imagen_background.name.split("/")[-1]}'
        super(Libro, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo
