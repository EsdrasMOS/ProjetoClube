from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_cobrancas, name='lista_cobrancas'),
    path('nova/', views.nova_cobranca, name='nova_cobranca'),
    path('editar/<int:cobranca_id>/', views.editar_cobranca, name='editar_cobranca'),
    path('deletar/<int:cobranca_id>/', views.deletar_cobranca, name='deletar_cobranca'),
]