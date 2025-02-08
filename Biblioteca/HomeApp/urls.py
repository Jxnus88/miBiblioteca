from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

# Rutas de la aplicación
urlpatterns = [
    path('', views.home, name='home'),  # Página de inicio
    path('libro/<int:libro_id>/', views.libro_seleccionado, name='libro_seleccionado')  # Detalle de libro
]

# Servir archivos estáticos/media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
