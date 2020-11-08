from django.db import models


class User(models.Model):
    rutpass = models.CharField(max_length=200, default='', blank=False)
    apellidos = models.CharField(max_length=200, default='', blank=False)
    nombres = models.CharField(max_length=200, default='', blank=False)
    fechanac = models.DateField(default='', blank=False)
    pais = models.CharField(max_length=200, default='')
    correo = models.EmailField(max_length=200, default='')
    foto = models.ImageField(upload_to='images/', default='')

    def __str__(self):
        return self.modelo