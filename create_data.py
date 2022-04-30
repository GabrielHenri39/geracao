import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "geracao.settings")
django.setup()

import string
import timeit
from random import choice, randint, random

from plataforma.models import Bairro, Cidade 

class CidadeClass:

    @staticmethod
    def criar_produtos(cidades):
        Cidade.objects.all().delete()
        aux = []
        for bairro in cidades :
            
            data = dict(
                cidade=bairro,
               
            )
            obj = Cidade(**data)
            aux.append(obj)
        Cidade.objects.bulk_create(aux)


class BairroClass:

    @staticmethod
    def criar_produtos(bairros):
        Bairro.objects.all().delete()
        aux = []
        for bairro in bairros :
            
            data = dict(
                bairro=bairro,
               
            )
            obj = Bairro(**data)
            aux.append(obj)
        Bairro.objects.bulk_create(aux)


bairros = [
    'Centro Histórico',
    'Jardim Higienópolis',
    'Jardim Petrópolis',
    'Jardim Quebec',
    'Vila Brasil',
    'Vila Casoni',
    'Vila Ipiranga',
    'Vila Nova',
    'Vila Recreio',
    'Aeroporto',
    'Cidade Industrial 2',
    'Conjunto Ernani Moura Lima',
    'Gleba Lindoia',
    'HU',
    'Jardim Antares',
    'Jardim Brasília',
    'Jardim Califórnia',
    'Jardim Ideal',
    'Jardim Interlagos',
    'Lon Rita',
    'Parque das Indústrias Leves',
    'Vila Fraternidade',
    'Heimtal',
    'Cidade Industrial 1',
    'Cinco Conjuntos',
    'Conjunto Parigot de Souza',
    'Conjunto Vivi Xavier',
    'Jardim Coliseu',
    'Jardim dos Alpes',
    'Jardim Pacaembu',
    'Parque Ouro Verde',
    'Perobinha',
    'Chácaras Esperança',
    'Cilo 2',
    'Cilo 3',
    'Shangri-lá',
    'Jardim Bandeirantes',
    'Jardim Champagnat',
    'Jardim Jamaica',
    'Jardim Leonor',
    'Jardim Olímpico',
    'Jardim Presidente',
    'Jardim Sabará',
    'Parque Universidade',
    'Alto do Cafezal',
    'Esperança',
    'Nova Esperança',
    'Acapulco',
    'Bela Suíça',
    'Cafezal',
    'Jardim Inglaterra',
    'Jardim Piza',
    'Parque Guanabara',
    'Saltinho',
    'Tucanos',
    'União da Vitória',
    'Vivendas do Arvoredo',
    'Cilo 1',
    'Jardim Morumbi'
]
bairros.sort()
cidade =('Londrina',)

tic = timeit.default_timer()

BairroClass.criar_produtos(bairros)

CidadeClass.criar_produtos(cidade)

toc = timeit.default_timer()

print('Tempo:', toc - tic)