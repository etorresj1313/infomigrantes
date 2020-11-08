from django.urls import path
from .views import index
from .views import galeria
from .views import contacto
from .views import agregar
from .views import listar

urlpatterns = [
    path('', index, name="index"),
    path('galeria/', galeria, name="galeria"),
    path('contacto/', contacto, name="contacto"),
    path('agregar/', agregar, name="agregar"),
    path('listar/', listar, name="listar"),
]
