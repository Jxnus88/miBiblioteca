from django.contrib import admin
from .models import Autor, Libro, NombreDirectorio

# Registro del modelo Libro en el panel de administración.
# Permite personalizar la vista en el admin para mostrar los campos más relevantes.
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('autor', 'titulo', 'genero')
    ordering = ('titulo',)
    # Permite buscar por el nombre del autor, título y género
    search_fields = ('autor__nombre','titulo', 'genero')
    list_filter = ('autor__nombre',)  # Filtrado por autor
    list_display_links = ('titulo',)
    list_per_page = 6  # Mostrar 6 elementos por página

# Registro del modelo Autor en el panel de administración.
# Personaliza la vista para mostrar el ID y nombre del autor.
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    ordering = ('nombre',)
    search_fields = ('nombre',)
    list_display_links = ('nombre',)
    list_per_page = 6

# Registro del modelo NombreDirectorio en el panel de administración.
# Simplemente muestra el nombre de cada directorio.
@admin.register(NombreDirectorio)
class NombreDirectorio(admin.ModelAdmin):
    list_display = ('nombre',)
    list_display_links = ('nombre',)
