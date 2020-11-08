from django.db import models

class Users(models.Model):
    rutpass = models.CharField(max_length=200, default='', blank=False)
    apellidos = models.CharField(max_length=200, default='', blank=False)
    nombres = models.CharField(max_length=200, default='', blank=False)
    fechanac = models.DateField(default='', blank=False)
    pais = models.CharField(max_length=200, default='')
    correo = models.EmailField(max_length=200, default='')
    foto = models.ImageField(upload_to='images/', default='')

    def __str__(self):
        return self.rutpass

class Agregar(models.Model):
    rut = models.CharField(max_length=200, default='', blank=False)
    nombres = models.CharField(max_length=200, default='', blank=False)
    apellidos = models.CharField(max_length=200, default='', blank=False)    
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField(default='', blank=False)    
    nacionalidad = models.CharField(max_length=200, default='')
    direccion = models.CharField(max_length=200, default='')
    correo = models.EmailField(max_length=200, default='')
    telefono = models.IntegerField()

    def __str__(self):
        return self.rut



