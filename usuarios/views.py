from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from socios.models import Socio
from funcionarios.models import Funcionario
from .forms import UsuarioCreationForm  # Adicione esta importação

def registro_socio(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.tipo_usuario = Usuario.IS_SOCIO
            user.save()
            
            Socio.objects.create(
                usuario=user,
                nome=request.POST.get('nome'),
                cpf=request.POST.get('cpf'),
                telefone=request.POST.get('telefone', ''),
                email=request.POST.get('email', ''),
                data_nascimento=request.POST.get('data_nascimento') or None
            )
            
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('dashboard_socio')
    else:
        form = UsuarioCreationForm()
    return render(request, 'socios/registro_socio.html', {'form': form})

def registro_funcionario(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.tipo_usuario = Usuario.IS_FUNCIONARIO
            user.save()
            
            Funcionario.objects.create(
                usuario=user,
                nome=request.POST.get('nome'),
                funcao=request.POST.get('funcao'),
                identificacao=request.POST.get('identificacao')
            )
            
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('dashboard_funcionario')
    else:
        form = UsuarioCreationForm()
    return render(request, 'funcionarios/registro_funcionario.html', {'form': form})

def pagina_inicial(request):
    return render(request, 'index.html')

def login_socio(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.tipo_usuario == Usuario.IS_SOCIO:
            login(request, user)
            return redirect('dashboard_socio')
        else:
            messages.error(request, 'Credenciais inválidas ou acesso negado.')
    return render(request, 'socios/login_socio.html')

def login_funcionario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.tipo_usuario == Usuario.IS_FUNCIONARIO:
            login(request, user)
            return redirect('dashboard_funcionario')
        else:
            messages.error(request, 'Credenciais inválidas ou acesso negado.')
    return render(request, 'funcionarios/login_funcionario.html')

def logout_view(request):
    logout(request)
    return redirect('pagina_inicial')

@login_required
def dashboard_socio(request):
    return render(request, 'socios/dashboard_socio.html')

@login_required
def dashboard_funcionario(request):
    return render(request, 'funcionarios/dashboard_funcionario.html')