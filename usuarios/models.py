from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    IS_SOCIO = 'socio'
    IS_FUNCIONARIO = 'funcionario'
    TIPOS = [
        (IS_SOCIO, 'Sócio'),
        (IS_FUNCIONARIO, 'Funcionário'),
    ]
    tipo_usuario = models.CharField(max_length=20, choices=TIPOS)
