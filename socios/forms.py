from django import forms
from .models import Socio

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['nome', 'cpf', 'telefone', 'email', 'data_nascimento']