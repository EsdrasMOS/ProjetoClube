from django.shortcuts import render, redirect
from .models import Agendamento, Servico
from socios.models import Socio
from django.contrib.auth.decorators import login_required

@login_required
def lista_agendamentos(request):
    agendamentos = Agendamento.objects.filter(socio__usuario=request.user)
    return render(request, 'agendamentos/lista_agendamentos.html', {'agendamentos': agendamentos})

@login_required
def novo_agendamento(request):
    servicos = Servico.objects.all()
    if request.method == 'POST':
        socio = request.user.socio
        servico_id = request.POST.get('servico')
        data_hora = request.POST.get('data_hora')
        observacao = request.POST.get('observacao', '')
        servico = Servico.objects.get(id=servico_id)
        Agendamento.objects.create(socio=socio, servico=servico, data_hora=data_hora, observacao=observacao)
        return redirect('lista_agendamentos')
    return render(request, 'agendamentos/novo_agendamento.html', {'servicos': servicos})