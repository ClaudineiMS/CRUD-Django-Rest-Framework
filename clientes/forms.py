from dataclasses import field
from .models import Usuarios
from .models import Grupos
from django.forms import ModelForm
from django import forms

class GruposForm(ModelForm):
    class Meta:
        model = Grupos
        fields = '__all__'


class UsuariosForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'


class GruposFormEdit(forms.ModelForm):
    class Meta:
        model = Grupos
        fields = '__all__'


class UsuariosFormEdit(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'
