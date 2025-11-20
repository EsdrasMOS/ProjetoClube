from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Funcionario
from .forms import FuncionarioForm 
from django.core.paginator import Paginator

def lista_funcionarios(request):
    funcionarios_list = Funcionario.objects.all()
    paginator = Paginator(funcionarios_list, 10)  
    page_number = request.GET.get('page')
    funcionarios = paginator.get_page(page_number)
    return render(request, 'funcionarios/lista_funcionarios.html', {'funcionarios': funcionarios})

def detalhe_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    return render(request, 'funcionarios/detalhe_funcionario.html', {'funcionario': funcionario})

def perfil_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    return render(request, 'funcionarios/perfil_funcionario.html', {'funcionario': funcionario})

@login_required
def editar_perfil_funcionario(request):
    funcionario = request.user.funcionario
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('dashboard_funcionario')
    else:
        form = FuncionarioForm(instance=funcionario)
    return render(request, 'funcionarios/editar_perfil_funcionario.html', {'form': form})
