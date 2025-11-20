from django import forms
from .models import Agendamento, Servico
from django.utils import timezone

class AgendamentoForm(forms.ModelForm):
    servico = forms.ModelChoiceField(queryset=Servico.objects.all(), empty_label="Selecione um serviço")

    class Meta:
        model = Agendamento
        fields = ['servico', 'data_hora', 'observacao']
        widgets = {
            'data_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean_data_hora(self):
        data_hora = self.cleaned_data.get('data_hora')
        if data_hora and data_hora <= timezone.now():
            raise forms.ValidationError('A data e hora devem ser futuras.')
        return data_hora