from django.db import models
from usuarios.models import Usuario

class Socio(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    data_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome