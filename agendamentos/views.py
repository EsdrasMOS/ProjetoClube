from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Agendamento, Servico
from usuarios.models import Usuario
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import AgendamentoForm

@login_required
def novo_agendamento(request):
    if request.user.tipo_usuario != Usuario.IS_SOCIO:
        messages.error(request, 'Acesso negado.')
        return redirect('dashboard_funcionario')
    
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.socio = request.user.socio
            agendamento.save()
            messages.success(request, 'Agendamento criado com sucesso!')
            return redirect('lista_agendamentos')
    else:
        form = AgendamentoForm()
    return render(request, 'agendamentos/novo_agendamento.html', {'form': form})

@login_required
def lista_agendamentos(request):
    query = request.GET.get('q', '')
    if request.user.tipo_usuario == Usuario.IS_SOCIO:
        agendamentos_list = Agendamento.objects.filter(socio__usuario=request.user)
    else:
        agendamentos_list = Agendamento.objects.all()
    
    agendamentos_list = agendamentos_list.filter(
        Q(servico__nome__icontains=query) | Q(observacao__icontains=query)
    )
    paginator = Paginator(agendamentos_list, 10)
    page_number = request.GET.get('page')
    agendamentos = paginator.get_page(page_number)
    return render(request, 'agendamentos/lista_agendamentos.html', {'agendamentos': agendamentos, 'query': query})

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