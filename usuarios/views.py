from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Usuario

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

def registro_socio(request):
    return render(request, 'socios/registro_socio.html')

def registro_funcionario(request):
    return render(request, 'funcionarios/registro_funcionario.html')

@login_required
def dashboard_socio(request):
    return render(request, 'socios/dashboard_socio.html')

@login_required
def dashboard_funcionario(request):
    return render(request, 'funcionarios/dashboard_funcionario.html')