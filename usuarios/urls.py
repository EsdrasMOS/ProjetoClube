from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('login/socio/', views.login_socio, name='login_socio'),
    path('login/funcionario/', views.login_funcionario, name='login_funcionario'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/socio/', views.registro_socio, name='registro_socio'),
    path('registro/funcionario/', views.registro_funcionario, name='registro_funcionario'),
    path('dashboard/socio/', views.dashboard_socio, name='dashboard_socio'),
    path('dashboard/funcionario/', views.dashboard_funcionario, name='dashboard_funcionario'),
]