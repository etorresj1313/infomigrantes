from django.shortcuts import render,redirect, get_object_or_404
from .models import Agregar, Users
from .forms import AgregarForm, UsersForm

# Create your views here.
def index(request):
    return render(request, 'app/index.html', {})
def indexc(request):
    return render(request, 'app/indexc.html', {}) 
def indexi(request):
    return render(request, 'app/indexi.html', {}) 
def menu(request):
    return render(request, 'app/menu.html', {}) 
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
def galeriac(request):
    return render(request, 'app/galeriac.html', {})
def galeriai(request):
    return render(request, 'app/galeriai.html', {})
def agregar(request):

    data = {
        'form': AgregarForm()
    }

    if request.method == 'POST':
        formulario = AgregarForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario

    return render(request, 'app/agregar.html', data)
def listar(request):
    usuarios = Agregar.objects.all()

    data = {
        'usuarios': usuarios
    }
        
    return render(request, 'app/listar.html', data)
def modlista(request):
    usuarios = Agregar.objects.all()

    data = {
        'usuarios': usuarios
    }      
    return render(request, 'app/modlista.html', data)
def elimlista(request):
    usuarios = Agregar.objects.all()

    data = {
        'usuarios': usuarios
    }      
    return render(request, 'app/elimlista.html', data)    

def modificar(request, rut):
    
    usuarios = get_object_or_404(Agregar,rut=rut)

    data = {
        'form':AgregarForm(instance=usuarios)
    }

    if request.method == 'POST':
        formulario = AgregarForm(data=request.POST, instance=usuarios)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Modificado Correctamente"
            return redirect(to='modlista')
        else:
            data["form"] = formulario
    return render(request, 'app/modificar.html',data)

def eliminar(request, rut):
    usuarios = get_object_or_404(Agregar,rut=rut)
    usuarios.delete()
    return redirect(to="elimlista")