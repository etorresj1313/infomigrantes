from django.test import TestCase
from .forms import *   # import all forms
from .models import Users, Agregar

# Test 1 - Sitio Principal (View 1)

class TestServerViews(TestCase):
    def test_main_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('http://127.0.0.1:8000')
        self.assertEqual(response.status_code, 200)

# Test 2 - Formulario Users (Form 1) - Contacto
 
class TestUsersForm(TestCase):
    def test_UsersForm_valid(self):
        form = UsersForm(data={'correo': "user@mp.com", 'nombres': "user", 'apellidos': "test", 'pais': "chile", 'consulta': "test de formulario"})
        self.assertTrue(form.is_valid())


# Test 3 - Formulario Agregar (Form 2) - Usuarios Sitio
 
class TestAgregarForm(TestCase):
    def test_AgregarForm_valid(self):
        form = AgregarForm(data={'rut': "25949655-9", 'nombres': "user", 'apellidos': "test", 'edad': 22, 'fecha_creacion': "2020-12-08", 'nacionalidad': "chileno", 'direccion': "calle nº 123", 'correo': "test@test.cl", 'telefono': 25258778})
        self.assertTrue(form.is_valid())
