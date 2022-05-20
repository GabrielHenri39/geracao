
from email import contentmanager
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Paciente
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.messages import constants
from plataforma.forms import CadastroP

# Create your views here.
@login_required(login_url='/auth/logar')
def home(request):
   pacientes= Paciente.objects.all()
   
   return render(request, 'home.html',{'pacientes':pacientes})


def cadastro_p(request):
   if request.method == "GET":
      form = CadastroP()
    
      
      
      context = {
            'form':form
         }
      
      
      return render(request,'cadastrop.html', context=context)
   else:
      form = CadastroP(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         messages.add_message(request, constants.SUCCESS, 'Cadastro do paciente realizado com sucesso')
         return redirect('/')
      else:
          form = CadastroP()
          context = {'form':form}
          messages.add_message(request, constants.ERROR, 'Tem alguem dado já exite')
          return render(request,'cadastrop.html', context=context)


def paciente(request, id):
   paciente = get_object_or_404(Paciente, id=id)
   return render(request, 'perfil_paciente.html', {'paciente': paciente, 'id': id})


def robot(request):
   return render(request,'robots.txt')