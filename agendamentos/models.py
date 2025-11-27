from django.db import models
from socios.models import Socio

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)  # Novo campo

    def __str__(self):
        return f"{self.nome} - R$ {self.valor}"

class Agendamento(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Agendamento: {self.socio.nome} - {self.servico.nome} em {self.data_hora.strftime('%d/%m/%Y %H:%M')}"