from django.shortcuts import render
from .models import Agregar, Users
from .forms import AgregarForm

# Create your views here.
def index(request):
    return render(request, 'app/index.html', {}) 
def contacto(request):
    return render(request, 'app/contacto.html', {}) 
def galeria(request):
    return render(request, 'app/galeria.html', {})
def agregar(request):

    data = {
        'form': AgregarForm()
    }

    if request.method == 'POST':
        formulario = AgregarForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'app/agregar.html', data)
def listar(request):
    usuarios = Agregar.objects.all()

    data = {
        'usuarios': usuarios
    }
        
    return render(request, 'app/listar.html', data)

