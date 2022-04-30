from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('cadastro_paciente/', views.cadastro_p,name='paciente'),
    path('perfil/<str:id>', views.paciente, name="perfil_paciente"),
  
    
]
