from django.shortcuts import render
from .models import Cobranca
from django.contrib.auth.decorators import login_required

@login_required
def lista_cobrancas(request):
    cobrancas = Cobranca.objects.filter(socio__usuario=request.user)
    return render(request, 'cobrancas/lista_cobrancas.html', {'cobrancas': cobrancas})