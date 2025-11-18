from django.db import models
from socios.models import Socio

class Cobranca(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    servico = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    vencimento = models.DateField()
    pago = models.BooleanField(default=False)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Cobrança {self.id} - {self.socio.nome}"