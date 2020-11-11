<<<<<<< HEAD
from django.shortcuts import render
=======
from django.shortcuts import render,redirect, get_object_or_404
from .models import Agregar, Users
from .forms import AgregarForm, UsersForm
>>>>>>> develop

# Create your views here.
def index(request):
    return render(request, 'app/index.html', {}) 
def contacto(request):
    data = {
        'form': UsersForm()
    }    
    if request.method == 'POST':        
        formulario = UsersForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Enviado Correctamente"
        else:
            data["form"] = formulario
    return render(request, 'app/contacto.html', data)
    
def galeria(request):
    return render(request, 'app/galeria.html', {})