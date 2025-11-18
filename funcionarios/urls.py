from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_funcionarios, name='lista_funcionarios'),
    path('detalhe/<int:funcionario_id>/', views.detalhe_funcionario, name='detalhe_funcionario'),
    path('perfil/<int:funcionario_id>/', views.perfil_funcionario, name='perfil_funcionario'),
]