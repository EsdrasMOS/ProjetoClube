from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_cobrancas, name='lista_cobrancas'),
]