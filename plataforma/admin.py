from django.contrib import admin
from .models import Bairro, Cidade, Paciente
# Register your models here.


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display= ('nome_do_paciente','id')


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display =('cidade','id')


admin.site.register(Bairro)
