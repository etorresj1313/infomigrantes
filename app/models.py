from django.db import models


class Users(models.Model):
    correo = models.EmailField(max_length=200, default='')
    nombres = models.CharField(max_length=200, default='', blank=False)
    apellidos = models.CharField(max_length=200, default='', blank=False)
    pais = models.CharField(max_length=200, default='', blank=False)
    consulta = models.TextField(max_length=500, default='')

    def __str__(self):
        return self.correo

class Agregar(models.Model):
    rut = models.CharField(max_length=200, default='', blank=False)
    nombres = models.CharField(max_length=200, default='', blank=False)
    apellidos = models.CharField(max_length=200, default='', blank=False)    
    edad = models.IntegerField()
    fecha_creacion = models.DateField(default='', blank=False)    
    nacionalidad = models.CharField(max_length=200, default='')
    direccion = models.CharField(max_length=200, default='')
    correo = models.EmailField(max_length=200, default='')
    telefono = models.IntegerField()

    def __str__(self):
        return self.rut

class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'









