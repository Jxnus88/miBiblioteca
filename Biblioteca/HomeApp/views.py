from django.shortcuts import render
from LibrosApp.models import Libro

# Vista de la página de inicio, muestra todos los libros disponibles.
def home(request):
    libros = Libro.objects.all()
    return render(request, 'HomeApp/home.html', {'libros': libros})

# Vista para mostrar los detalles de un libro seleccionado.
# Recupera un libro por su ID y su imagen de fondo si está disponible.
def libro_seleccionado(request, libro_id):
    libro = Libro.objects.get(id=libro_id)
    imagen_background_url = libro.imagen_background.url if libro.imagen_background else None

    context = {
        'libro': libro,
        'imagen_background_url': imagen_background_url,
    }
    return render(request, 'HomeApp/libroSeleccionado.html', context)
