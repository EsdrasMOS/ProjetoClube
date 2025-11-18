from django.shortcuts import render, get_object_or_404
from .models import Funcionario

def lista_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionarios/lista_funcionarios.html', {'funcionarios': funcionarios})

def detalhe_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    return render(request, 'funcionarios/detalhe_funcionario.html', {'funcionario': funcionario})

def perfil_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    return render(request, 'funcionarios/perfil_funcionario.html', {'funcionario': funcionario})