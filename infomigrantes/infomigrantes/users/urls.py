from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView 

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto', views.contacto, name='contacto'),
    path('galeria', views.galeria, name='galeria'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
