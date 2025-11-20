from django import forms
from .models import Socio
from datetime import timezone
import re

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['nome', 'cpf', 'telefone', 'email', 'data_nascimento']

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):  # Formato básico
            raise forms.ValidationError('CPF deve estar no formato XXX.XXX.XXX-XX.')
        if Socio.objects.filter(cpf=cpf).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('CPF já cadastrado.')
        return cpf

    def clean_data_nascimento(self):
        data = self.cleaned_data.get('data_nascimento')
        if data and data > timezone.now().date():
            raise forms.ValidationError('Data de nascimento não pode ser futura.')
        return data