from django.urls import path
from .views import index,galeria,contacto,agregar,listar,menu,modificar,modlista,eliminar,elimlista

urlpatterns = [
    path('', index, name="index"),
    path('galeria/', galeria, name="galeria"),
    path('contacto/', contacto, name="contacto"),
    path('agregar/', agregar, name="agregar"),
    path('listar/', listar, name="listar"),
    path('menu/', menu, name="menu"),
    path('modlista/', modlista, name="modlista"),
    path('elimlista/', elimlista, name="elimlista"),
    path('modificar/<rut>/', modificar, name="modificar"),
    path('eliminar/<rut>/', eliminar, name="eliminar"),    
]
