from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('usuarios.urls')),  
    path('socios/', include('socios.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('agendamentos/', include('agendamentos.urls')),
    path('cobrancas/', include('cobrancas.urls')),
    path('admin/', admin.site.urls),
]