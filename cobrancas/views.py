from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cobranca
from usuarios.models import Usuario

@login_required
def lista_cobrancas(request):
    if request.user.tipo_usuario == Usuario.IS_SOCIO:
        cobrancas = Cobranca.objects.filter(socio__usuario=request.user)
    else:
        cobrancas = Cobranca.objects.all()  # Funcionários veem todas
    return render(request, 'cobrancas/lista_cobrancas.html', {'cobrancas': cobrancas})

@login_required
def nova_cobranca(request):
    if request.user.tipo_usuario != Usuario.IS_FUNCIONARIO:
        messages.error(request, 'Acesso negado.')
        return redirect('dashboard_socio')
    
    from socios.models import Socio  # Import aqui para evitar circular
    socios = Socio.objects.all()
    if request.method == 'POST':
        socio_id = request.POST.get('socio')
        servico = request.POST.get('servico')
        valor = request.POST.get('valor')
        vencimento = request.POST.get('vencimento')
        observacao = request.POST.get('observacao', '')
        socio = Socio.objects.get(id=socio_id)
        Cobranca.objects.create(socio=socio, servico=servico, valor=valor, vencimento=vencimento, observacao=observacao)
        messages.success(request, 'Cobrança criada com sucesso!')
        return redirect('lista_cobrancas')
    return render(request, 'cobrancas/nova_cobranca.html', {'socios': socios})

@login_required
def editar_cobranca(request, cobranca_id):
    cobranca = get_object_or_404(Cobranca, id=cobranca_id)
    if request.user.tipo_usuario != Usuario.IS_FUNCIONARIO:
        messages.error(request, 'Acesso negado.')
        return redirect('lista_cobrancas')
    
    from socios.models import Socio
    socios = Socio.objects.all()
    if request.method == 'POST':
        cobranca.socio_id = request.POST.get('socio')
        cobranca.servico = request.POST.get('servico')
        cobranca.valor = request.POST.get('valor')
        cobranca.vencimento = request.POST.get('vencimento')
        cobranca.pago = 'pago' in request.POST
        cobranca.observacao = request.POST.get('observacao', '')
        cobranca.save()
        messages.success(request, 'Cobrança atualizada!')
        return redirect('lista_cobrancas')
    return render(request, 'cobrancas/editar_cobranca.html', {'cobranca': cobranca, 'socios': socios})

@login_required
def deletar_cobranca(request, cobranca_id):
    cobranca = get_object_or_404(Cobranca, id=cobranca_id)
    if request.user.tipo_usuario != Usuario.IS_FUNCIONARIO:
        messages.error(request, 'Acesso negado.')
        return redirect('lista_cobrancas')
    
    cobranca.delete()
    messages.success(request, 'Cobrança deletada!')
    return redirect('lista_cobrancas')