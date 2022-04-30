from django import template
from datetime import datetime,date

register = template.Library()

estatos = { '01': 'Acre',
            '02':'Alagoas',
            '03':'Amapá',
            '04':'Amazonas',
            '05':'Bahia',
            '06':'Distrito Federal',
            '07':'Ceará',
            '08':'Espírito Santo',
            '09':'Goiás',
            '10':'Maranhão',
            '11':'Mato Grosso',
            '12':'Mato Grosso do Sul',
            '13':'Minas Gerais',
            '14':'Pará',
            '15':'Paraíba',
            '16':'Paraná',
            '17':'Pernambuco',
            '18':'Piauí',
            '19':'Rio de Janeiro',
            '20':'Rio Grande do Norte',
            '21':'Rio Grande do Sul',
            '22':'Rondônia',
            '23':'Roraima',
            '24':'Santa Catarina',
            '25':'Sâo Paulo',
            '26':'Sergipe',
            '27':'Tocantins'
            }

uf = {'01':'AC',
        '02':'AL',
        '03':'AP',
        '04':'AM',
        '05':'BA',
        '06':'DF',
        '07':'CE',
        '08':'ES',
        '09':'GO',
        '10':'MA',
        '11':'MT',
        '12':'MS',
        '13':'MG',
        '14':'PA',
        '15':'PB',
        '16':'PR',
        '17':'PE',
        '18':'PI',
        '19':'RJ',
        '20':'RN',
        '21':'RS',
        '22':'RO',
        '23':'RR',
        '24':'SC',
        '25':'SP',
        '26':'SE',
        '27':'TO'
       }

@register.filter
def idade(data_nascimento):
    
    data = data_nascimento
   
    hoje = date.today()
    idade =hoje.year - data.year - ((hoje.month, hoje.day) < (data.month, data.day))
    texto = 'Anos'
    if idade == 1:
        texto = 'Ano'
    return f"{idade} {texto}."

@register.filter
def mostar_estados(estato):
    
    for k, v in estatos.items():
      if k == estato:
          return v


@register.filter
def mostar_uf(uf_p):
    
    for k, v in uf.items():
      if k == uf_p:
          return v

    