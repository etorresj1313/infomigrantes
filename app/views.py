from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app/index.html', {}) 
def contacto(request):
    return render(request, 'app/contacto.html', {}) 
def galeria(request):
    return render(request, 'app/galeria.html', {})