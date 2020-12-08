import requests
from django.shortcuts import render,redirect, get_object_or_404
from .models import Agregar, Users, City
from .forms import AgregarForm, UsersForm, CreationForm, CityForm
from django.contrib.auth import authenticate, login



# Create your views here.
def index(request):
    return render(request, 'app/index.html', {}) 
def indexc(request):
    return render(request, 'app/indexc.html', {}) 
def indexi(request):
    return render(request, 'app/indexi.html', {}) 
def loginc(request):
    return render(request, 'registration/loginc.html', {}) 
def logini(request):
    return render(request, 'registration/logini.html', {}) 
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
def quienes(request):
    return render(request, 'app/quienes.html', {})
def quienesc(request):
    return render(request, 'app/quienesc.html', {})
def quienesi(request):
    return render(request, 'app/quienesi.html', {})
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

def registro(request):
    data = {
        'form':CreationForm()
    }

    if request.method == 'POST':
        formulario = CreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            data["mensaje"] = "Usuario Registrado exitosamente"
            return redirect(to="index")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

def weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=17c8f96424c265befcd1aa5a0b92c876'
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'app/weather.html', context)