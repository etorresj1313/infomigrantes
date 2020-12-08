from django.contrib import admin
from .models import Users, Agregar
from .models import City

class AgregarAdmin(admin.ModelAdmin):
    list_display = ["rut", "nombres", "apellidos", "edad", "fecha_creacion", "nacionalidad", "direccion", "correo", "telefono"]

admin.site.register(Users)
admin.site.register(Agregar, AgregarAdmin)
admin.site.register(City)


