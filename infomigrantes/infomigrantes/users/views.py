from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Users


# Create your views here.
def index(request):
    return render(request, '../sitio/index.html', {}) 
def contacto(request):
    return render(request, '../sitio/contacto.html', {}) 
def galeria(request):
    return render(request, '../sitio/galeria.html', {})