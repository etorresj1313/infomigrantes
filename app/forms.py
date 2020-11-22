from django import forms
from .models import Users, Agregar
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UsersForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = '__all__'

class AgregarForm(forms.ModelForm):

    class Meta:
        model = Agregar
        fields = '__all__'

        widgets = {
            "fecha_creacion": forms.widgets.SelectDateWidget()
        }

class CreationForm(UserCreationForm):
     
     class Meta:
         model = User
         fields = ['username', "first_name", "last_name", "email", "password1", "password2"]