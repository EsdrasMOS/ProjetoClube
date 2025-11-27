from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
    path('socios/', include('socios.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('agendamentos/', include('agendamentos.urls')),
    path('cobrancas/', include('cobrancas.urls')),
]