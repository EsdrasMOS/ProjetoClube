from django.shortcuts import render, get_object_or_404
from .models import Socio

def lista_socios(request):
    socios = Socio.objects.all()
    return render(request, 'socios/lista_socios.html', {'socios': socios})

def detalhe_socio(request, socio_id):
    socio = get_object_or_404(Socio, id=socio_id)
    return render(request, 'socios/detalhe_socio.html', {'socio': socio})

def perfil_socio(request, socio_id):
    socio = get_object_or_404(Socio, id=socio_id)
    return render(request, 'socios/perfil_socio.html', {'socio': socio})
