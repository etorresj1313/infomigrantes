from django.contrib import admin
from .models import Users, Agregar


class AgregarAdmin(admin.ModelAdmin):
    list_display = ["rut", "nombres", "apellidos", "edad", "fecha_nacimiento", "nacionalidad", "direccion", "correo", "telefono"]

admin.site.register(Users)
admin.site.register(Agregar, AgregarAdmin)



