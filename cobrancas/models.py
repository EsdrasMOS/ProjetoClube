from django.db import models
from socios.models import Socio
from agendamentos.models import Servico

class Cobranca(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    vencimento = models.DateField()
    pago = models.BooleanField(default=False)
    observacao = models.TextField(blank=True, null=True)

    @property
    def valor(self):
        return self.servico.valor

    def __str__(self):
        return f"Cobrança {self.id} - {self.socio.nome} - {self.servico.nome}"