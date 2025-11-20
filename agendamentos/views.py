from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Agendamento, Servico
from usuarios.models import Usuario
from django.core.paginator import Paginator

@login_required
def lista_agendamentos(request):
    if request.user.tipo_usuario == Usuario.IS_SOCIO:
        agendamentos_list = Agendamento.objects.filter(socio__usuario=request.user)
    else:
        agendamentos_list = Agendamento.objects.all()
    paginator = Paginator(agendamentos_list, 10)
    page_number = request.GET.get('page')
    agendamentos = paginator.get_page(page_number)
    return render(request, 'agendamentos/lista_agendamentos.html', {'agendamentos': agendamentos})

@login_required
def novo_agendamento(request):
    if request.user.tipo_usuario != Usuario.IS_SOCIO:
        messages.error(request, 'Acesso negado.')
        return redirect('dashboard_funcionario')
    
    servicos = Servico.objects.all()
    if request.method == 'POST':
        servico_id = request.POST.get('servico')
        data_hora = request.POST.get('data_hora')
        observacao = request.POST.get('observacao', '')
        servico = Servico.objects.get(id=servico_id)
        socio = request.user.socio
        Agendamento.objects.create(socio=socio, servico=servico, data_hora=data_hora, observacao=observacao)
        messages.success(request, 'Agendamento criado com sucesso!')
        return redirect('lista_agendamentos')
    return render(request, 'agendamentos/novo_agendamento.html', {'servicos': servicos})

@login_required
def editar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    if agendamento.socio.usuario != request.user and request.user.tipo_usuario != Usuario.IS_FUNCIONARIO:
        messages.error(request, 'Acesso negado.')
        return redirect('lista_agendamentos')
    
    servicos = Servico.objects.all()
    if request.method == 'POST':
        agendamento.servico_id = request.POST.get('servico')
        agendamento.data_hora = request.POST.get('data_hora')
        agendamento.observacao = request.POST.get('observacao', '')
        agendamento.save()
        messages.success(request, 'Agendamento atualizado!')
        return redirect('lista_agendamentos')
    return render(request, 'agendamentos/editar_agendamento.html', {'agendamento': agendamento, 'servicos': servicos})

@login_required
def deletar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    if agendamento.socio.usuario != request.user and request.user.tipo_usuario != Usuario.IS_FUNCIONARIO:
        messages.error(request, 'Acesso negado.')
        return redirect('lista_agendamentos')
    
    agendamento.delete()
    messages.success(request, 'Agendamento deletado!')
    return redirect('lista_agendamentos')