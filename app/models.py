from django.db import models


<<<<<<< HEAD
class User(models.Model):
    rutpass = models.CharField(max_length=200, default='', blank=False)
    apellidos = models.CharField(max_length=200, default='', blank=False)
    nombres = models.CharField(max_length=200, default='', blank=False)
    fechanac = models.DateField(default='', blank=False)
    pais = models.CharField(max_length=200, default='')
=======
class Users(models.Model):
>>>>>>> develop
    correo = models.EmailField(max_length=200, default='')
    nombres = models.CharField(max_length=200, default='', blank=False)
    apellidos = models.CharField(max_length=200, default='', blank=False)
    pais = models.CharField(max_length=200, default='', blank=False)
    consulta = models.TextField(max_length=500, default='')

    def __str__(self):
<<<<<<< HEAD
        return self.modelo
=======
        return self.correo

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











>>>>>>> develop
