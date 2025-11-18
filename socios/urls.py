from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_socios, name='lista_socios'),
    path('detalhe/<int:socio_id>/', views.detalhe_socio, name='detalhe_socio'),
    path('perfil/<int:socio_id>/', views.perfil_socio, name='perfil_socio'),
]