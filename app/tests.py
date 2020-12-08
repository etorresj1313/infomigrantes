from django.test import TestCase
from .forms import *   # import all forms
from .models import Users, Agregar

class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('http://127.0.0.1:8000')
        self.assertEqual(response.status_code, 200)

class TestAgregarForm(TestCase):
    def test_UsersForm_valid(self):
        form = UsersForm(data={'correo': "user@mp.com", 'nombres': "user", 'apellidos': "test", 'pais': "chile", 'consulta': "test de formulario"})
        self.assertTrue(form.is_valid())