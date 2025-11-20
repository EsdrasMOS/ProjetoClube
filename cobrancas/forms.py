from django import forms
from .models import Cobranca
from django.utils import timezone

class CobrancaForm(forms.ModelForm):
    pago = forms.BooleanField(required=False, label="Marcar como paga")

    class Meta:
        model = Cobranca
        fields = ['socio', 'servico', 'valor', 'vencimento', 'observacao', 'pago']
        widgets = {
            'vencimento': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_valor(self):
        valor = self.cleaned_data.get('valor')
        if valor and valor <= 0:
            raise forms.ValidationError('O valor deve ser positivo.')
        return valor

    def clean_vencimento(self):
        vencimento = self.cleaned_data.get('vencimento')
        if vencimento and vencimento < timezone.now().date():
            raise forms.ValidationError('A data de vencimento não pode ser no passado.')
        return vencimento