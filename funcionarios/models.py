from django.db import models
from usuarios.models import Usuario

class Funcionario(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)
    identificacao = models.CharField(max_length=50)

    def __str__(self):
        return self.nome