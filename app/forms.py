from django import forms
from .models import Users, Agregar


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