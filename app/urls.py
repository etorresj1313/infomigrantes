from django.urls import path
from .views import index
from .views import galeria
from .views import contacto

urlpatterns = [
    path('', index, name="index"),
    path('galeria', galeria, name="galeria"),
    path('contacto', contacto, name="contacto"),
]