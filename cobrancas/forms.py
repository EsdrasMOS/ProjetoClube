from django import forms
from .models import Cobranca
from django.utils import timezone

class CobrancaForm(forms.ModelForm):
    pago = forms.BooleanField(required=False, label="Marcar como paga")

    class Meta:
        model = Cobranca
        fields = ['socio', 'servico', 'vencimento', 'observacao', 'pago']
        widgets = {
            'vencimento': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_vencimento(self):
        vencimento = self.cleaned_data.get('vencimento')
        if vencimento and vencimento < timezone.now().date():
            raise forms.ValidationError('A data de vencimento não pode ser no passado.')
        return vencimento