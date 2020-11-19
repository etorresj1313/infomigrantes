from django.urls import path
from .views import index,galeria,contacto,agregar,listar,menu,modificar,modlista,eliminar,elimlista,indexc,galeriac,indexi,galeriai,quienes,quienesc,quienesi

urlpatterns = [
    path('', index, name="index"),
    path('indexc/', indexc, name="indexc"),
    path('indexi/', indexi, name="indexi"),
    path('galeria/', galeria, name="galeria"),
    path('galeriac/', galeriac, name="galeriac"),
    path('galeriai/', galeriai, name="galeriai"),
    path('quienes/', quienes, name="quienes"),
    path('quienesc/', quienesc, name="quienesc"),
    path('quienesi/', quienesi, name="quienesi"),
    path('contacto/', contacto, name="contacto"),
    path('agregar/', agregar, name="agregar"),
    path('listar/', listar, name="listar"),
    path('menu/', menu, name="menu"),
    path('modlista/', modlista, name="modlista"),
    path('elimlista/', elimlista, name="elimlista"),
    path('modificar/<rut>/', modificar, name="modificar"),
    path('eliminar/<rut>/', eliminar, name="eliminar"),    
]
