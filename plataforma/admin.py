from django.contrib import admin
from .models import Bairro, Cidade, Paciente, Escolas

# Register your models here.
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display= ('nome_do_paciente','id')

admin.site.register(Cidade)
admin.site.register(Escolas)
admin.site.register(Bairro)
