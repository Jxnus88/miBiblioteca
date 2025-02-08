# Proyecto de Gestión de Libros

Este proyecto es una aplicación web de gestión de libros, desarrollada con **Django** y **Python 3.12**. 
El proyecto fue creado utilizando el entorno de desarrollo **PyCharm**. Permite a los usuarios explorar libros, ver detalles sobre cada uno, y navegar por diferentes géneros y autores.
Está diseñado con un panel de administración para gestionar los datos de autores, libros y directorios asociados.

El proyecto también utiliza la librería **Pillow** para el control y manejo de imágenes en los libros y autores.

## Características

- **Vista de Inicio**: Muestra todos los libros disponibles con sus títulos y autores.
- **Detalles del Libro**: Permite ver la información detallada de cada libro, incluyendo su autor, género, subgéneros y una imagen de fondo si está disponible.
- **Panel de Administración**: Los administradores pueden gestionar los libros, autores y directorios desde el panel de administración de Django.
- **Búsqueda y Filtrado**: Funciones de búsqueda por título, autor y género, y filtrado por autor en el panel de administración.

## Tecnologías Utilizadas

- **Django**: Framework de desarrollo web en Python.
- **Python 3.12**: Versión utilizada para el desarrollo.
- **PyCharm**: Entorno de desarrollo utilizado para crear y gestionar el proyecto.
- **SQLite**: Base de datos predeterminada para el desarrollo.
- **Pillow**: Librería para el manejo de imágenes.
- **HTML/CSS**: Frontend básico.
- **Bootstrap**: Para diseño responsivo (opcional, si se decide usarlo).
- **Django Admin**: Para la gestión de los modelos (libros, autores y directorios).

## Instalación

### Requisitos

- Python 3.12
- Django (ver `requirements.txt` para versiones específicas)
- **Pillow**: Necesario para el control y manejo de imágenes.
- **PyCharm** (opcional): Para una mejor experiencia de desarrollo.

### Pasos para instalar

1. Clona el repositorio:
  
    bash
    - git clone https://github.com/Jxnus88/miBiblioteca.git
    - cd miBiblioteca

3. Crea un entorno virtual (opcional, pero recomendado):
   
    bash
    - python3 -m venv venv
    - source venv/bin/activate 
    - En Windows usa 'venv\Scripts\activate'

4. Instala las dependencias, incluida Pillow para el control de imágenes:
    
    bash
    - pip install Pillow

5. Realiza las migraciones de la base de datos:
  
    bash
    - python manage.py makemigrations
    - python manage.py migrate

6. Crea un superusuario para acceder al panel de administración:

    bash
    - python manage.py createsuperuser
    - Introduce un nombre
    - Introduce un email(opcional)
    - Introduce contraseña
    - Confirma contraseña

7. Ejecuta el servidor de desarrollo:

    bash
    - python manage.py runserver
  
