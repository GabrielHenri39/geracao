

from django import forms
from django.db.models import fields
from .models import Paciente, Cidade, Bairro, Escolas 
from django.db import models    
from datetime import date


class TelInput(forms.DateInput):
    input_type = 'tel'
    


class DateInput(forms.DateInput):
    input_type = 'date'


class CadastroP(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = "__all__"
        widgets = {
            'data_nascimento': DateInput(),
            'telefone': TelInput(),
            'cpf': forms.TextInput(attrs={'data-mask':"000.000.000-00"}),
            'rg': forms.TextInput(attrs={'data-mask':"00.000.000-0"}),
        

        }
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
       
        # self.helper.layout = Layout(
        #     Row(
        #         Column('foto', css_class='form-group col-md-6 mb-0'),
        #         Column('nome_do_paciente', css_class='form-group col-md-6 mb-0'),
        #         css_class='form-row'
        #     ),
        #     # 'address_1',
        #     # 'address_2',
        #     # Row(
        #     #     Column('city', css_class='form-group col-md-6 mb-0'),
        #     #     Column('state', css_class='form-group col-md-4 mb-0'),
        #     #     Column('zip_code', css_class='form-group col-md-2 mb-0'),
        #     #     css_class='form-row'
        #     # ),
        #     # 'check_me_out',
        #     Submit('submit', 'Sign in')
        # )
    def __getitem__(self, name: str):
        return super().__getitem__(name)

class EscolaForm(forms.ModelForm):
    
     class Meta:
        model= Escolas
        fields ='__all__'