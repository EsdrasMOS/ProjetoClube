from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def pagina_inicial(request):
    return render(request, 'index.html')

def login_socio(request):
    if request.method == 'POST':
        pass
    return render(request, 'login_socio.html')

def login_funcionario(request):
    return render(request, 'login_funcionario.html')

def logout_view(request):
    logout(request)
    return redirect('pagina_inicial')

def registro_socio(request):
    return render(request, 'registro_socio.html')

def registro_funcionario(request):
    return render(request, 'registro_funcionario.html')

@login_required
def dashboard_socio(request):
    return render(request, 'dashboard_socio.html')

@login_required
def dashboard_funcionario(request):
    return render(request, 'dashboard_funcionario.html')