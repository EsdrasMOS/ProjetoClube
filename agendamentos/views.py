from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Agendamento, Servico
from usuarios.models import Usuario
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import AgendamentoForm
from cobrancas.models import Cobranca

@login_required
def novo_agendamento(request):
    print("View novo_agendamento chamada")  
    if request.user.tipo_usuario != Usuario.IS_SOCIO:
        messages.error(request, 'Acesso negado.')
        return redirect('dashboard_funcionario')
    
    servicos = Servico.objects.all()
    print(f"Serviços disponíveis: {servicos}") 
    
    if request.method == 'POST':
        print(f"POST data: {request.POST}")  # Debug
        servico_id = request.POST.get('servico')
        print(f"Servico ID recebido: {servico_id}")
        data_hora = request.POST.get('data_hora')
        observacao = request.POST.get('observacao', '')
        servico = Servico.objects.get(id=servico_id)
        socio = request.user.socio
        agendamento = Agendamento.objects.create(socio=socio, servico=servico, data_hora=data_hora, observacao=observacao)
        
        from django.utils import timezone
        vencimento = timezone.now().date() + timezone.timedelta(days=30) 
        Cobranca.objects.create(
            socio=socio,
            servico=servico,
            vencimento=vencimento,
            observacao=f'Cobrança gerada do agendamento {agendamento.id}'
        )
        
        messages.success(request, 'Agendamento criado e cobrança gerada!')
        return redirect('lista_agendamentos')
    return render(request, 'agendamentos/novo_agendamento.html', {'servicos': servicos})

@login_required
def lista_agendamentos(request):
    if request.user.tipo_usuario == Usuario.IS_SOCIO:
        agendamentos_list = Agendamento.objects.filter(socio__usuario=request.user).order_by('-data_hora')  # Adicione order_by
    else:
        agendamentos_list = Agendamento.objects.all().order_by('-data_hora')
    paginator = Paginator(agendamentos_list, 10)
    page_number = request.GET.get('page')
    agendamentos = paginator.get_page(page_number)
    return render(request, 'agendamentos/lista_agendamentos.html', {'agendamentos': agendamentos})

@login_required
def editar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    if not (request.user == agendamento.socio.usuario or request.user.tipo_usuario == Usuario.IS_FUNCIONARIO):
        messages.error(request, 'Acesso negado.')
        return redirect('lista_agendamentos')
    
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Agendamento atualizado!')
            return redirect('lista_agendamentos')
    else:
        form = AgendamentoForm(instance=agendamento)
    return render(request, 'agendamentos/editar_agendamento.html', {'form': form})

@login_required
def deletar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    if agendamento.socio.usuario != request.user and request.user.tipo_usuario != Usuario.IS_FUNCIONARIO:
        messages.error(request, 'Acesso negado.')
        return redirect('lista_agendamentos')
    
    agendamento.delete()
    messages.success(request, 'Agendamento deletado!')
    return redirect('lista_agendamentos')