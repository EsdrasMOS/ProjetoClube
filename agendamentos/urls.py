from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_agendamentos, name='lista_agendamentos'),
    path('novo/', views.novo_agendamento, name='novo_agendamento'),
    path('editar/<int:agendamento_id>/', views.editar_agendamento, name='editar_agendamento'),
    path('deletar/<int:agendamento_id>/', views.deletar_agendamento, name='deletar_agendamento'),
]