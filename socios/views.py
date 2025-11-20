from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Socio
from .forms import SocioForm 
from django.db.models import Q

def lista_socios(request):
    query = request.GET.get('q', '')
    socios_list = Socio.objects.filter(
        Q(nome__icontains=query) | Q(cpf__icontains=query) | Q(email__icontains=query)
    )
    paginator = Paginator(socios_list, 10)
    page_number = request.GET.get('page')
    socios = paginator.get_page(page_number)
    return render(request, 'socios/lista_socios.html', {'socios': socios, 'query': query})

def detalhe_socio(request, socio_id):
    socio = get_object_or_404(Socio, id=socio_id)
    return render(request, 'socios/detalhe_socio.html', {'socio': socio})

def perfil_socio(request, socio_id):
    socio = get_object_or_404(Socio, id=socio_id)
    return render(request, 'socios/perfil_socio.html', {'socio': socio})

@login_required
def editar_perfil_socio(request):
    socio = request.user.socio
    if request.method == 'POST':
        form = SocioForm(request.POST, instance=socio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('dashboard_socio')
    else:
        form = SocioForm(instance=socio)
    return render(request, 'socios/editar_perfil_socio.html', {'form': form})