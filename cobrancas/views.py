from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cobranca
from usuarios.models import Usuario
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import CobrancaForm

@login_required
def nova_cobranca(request):
    if request.user.tipo_usuario != Usuario.IS_FUNCIONARIO:
        messages.error(request, 'Acesso negado.')
        return redirect('dashboard_socio')
    
    if request.method == 'POST':
        socio_id = request.POST.get('socio')
        servico_id = request.POST.get('servico')
        vencimento = request.POST.get('vencimento')
        observacao = request.POST.get('observacao', '')
        socio = Socio.objects.get(id=socio_id)
        servico = Servico.objects.get(id=servico_id)
        Cobranca.objects.create(socio=socio, servico=servico, vencimento=vencimento, observacao=observacao)
        messages.success(request, 'Cobrança criada com sucesso!')
        return redirect('lista_cobrancas')
    else:
        form = CobrancaForm()
    return render(request, 'cobrancas/nova_cobranca.html', {'form': form})

@login_required
def editar_cobranca(request, cobranca_id):
    cobranca = get_object_or_404(Cobranca, id=cobranca_id)
    if request.user.tipo_usuario != Usuario.IS_FUNCIONARIO:
        messages.error(request, 'Acesso negado.')
        return redirect('lista_cobrancas')
    
    if request.method == 'POST':
        form = CobrancaForm(request.POST, instance=cobranca)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cobrança atualizada!')
            return redirect('lista_cobrancas')
    else:
        form = CobrancaForm(instance=cobranca)
    return render(request, 'cobrancas/editar_cobranca.html', {'form': form})


@login_required
def lista_cobrancas(request):
         query = request.GET.get('query', '')  
         status_filter = request.GET.get('status', '')  
         cobrancas = Cobranca.objects.all()
         
         if query:
             cobrancas = cobrancas.filter(description__icontains=query)  
         if status_filter:
             cobrancas = cobrancas.filter(status=status_filter)
         
         return render(request, 'cobrancas/lista_cobrancas.html', {
             'cobrancas': cobrancas,
             'query': query,  
             'status_filter': status_filter, 
         })
     

@login_required
def deletar_cobranca(request, cobranca_id):
    cobranca = get_object_or_404(Cobranca, id=cobranca_id)
    if request.user.tipo_usuario != Usuario.IS_FUNCIONARIO:
        messages.error(request, 'Acesso negado.')
        return redirect('lista_cobrancas')
    
    cobranca.delete()
    messages.success(request, 'Cobrança deletada!')
    return redirect('lista_cobrancas')