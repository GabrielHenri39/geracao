from django.db import models
from datetime import datetime, date

choices_uf = (
                ('01','AC'),
                ('02','AL'),
                ('03','AP'),
                ('04','AM'),
                ('05','BA'),
                ('06','DF'),
                ('07','CE'),
                ('08','ES'),
                ('09','GO'),
                ('10','MA'),
                ('11','MT'),
                ('12','MS'),
                ('13','MG'),
                ('14','PA'),
                ('15','PB'),
                ('16','PR'),
                ('17','PE'),
                ('18','PI'),
                ('19','RJ'),
                ('20','RN'),
                ('21','RS'),
                ('22','RO'),
                ('23','RR'),
                ('24','SC'),
                ('25','SP'),
                ('26','SE'),
                ('27','TO')
                )


choices = (('01', 'Acre'),
            ('02','Alagoas'),
            ('03','Amapá'),
            ('04','Amazonas'),
            ('05','Bahia'),
            ('06','Distrito Federal'),
            ('07','Ceará'),
            ('08','Espírito Santo'),
            ('09','Goiás'),
            ('10','Maranhão'),
            ('11','Mato Grosso'),
            ('12','Mato Grosso do Sul'),
            ('13','Minas Gerais'),
            ('14','Pará'),
            ('15','Paraíba'),
            ('16','Paraná'),
            ('17','Pernambuco'),
            ('18','Piauí'),
            ('19','Rio de Janeiro'),
            ('20','Rio Grande do Norte'),
            ('21','Rio Grande do Sul'),
            ('22','Rondônia'),
            ('23','Roraima'),
            ('24','Santa Catarina'),
            ('25', 'Sâo Paulo'),
            ('26','Sergipe'),
            ('27','Tocantins')
            )


sexo_choices = (    
                ('f','Feminino'),
                ('m','Masculino')
                )

class Cidade(models.Model):
    cidade = models.CharField(max_length=60)


    def __str__(self):
        return self.cidade
  
    
class Bairro(models.Model):
    bairro = models.CharField(max_length=100,unique=True)


    class Meta:
        ordering =['bairro']
    

    def __str__(self):
        return self.bairro 




# class NivelDeEscolaridade()

class Paciente(models.Model):
    foto = models.ImageField(upload_to=f'img', blank=True,null=True)
    nome_do_paciente = models.CharField(max_length=100, verbose_name='Nome do Paciente' )
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    naturalidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2, choices=choices,default='16')
    uf = models.CharField(max_length=2, choices=choices_uf , default='16', verbose_name='UF')
    cidade =  models.ForeignKey(Cidade,on_delete=models.DO_NOTHING)
    bairro = models.ForeignKey(Bairro,on_delete=models.DO_NOTHING)
    endereco= models.CharField(max_length=100, verbose_name='Endereço')
    cpf = models.CharField(max_length=15, unique=True, blank=True, null=True, verbose_name='CPF' )
    rg= models.CharField(max_length=14,  blank=True, null=True, verbose_name='RG')
    gerero = models.CharField(max_length=1,choices=sexo_choices,verbose_name='Gênero')
    cns= models.IntegerField( unique=True,verbose_name='CNS')
    ubs= models.CharField(max_length=100, verbose_name='UBS',)
    cipac= models.IntegerField(verbose_name='CIPAC')
    nome_da_mae= models.CharField(max_length=100, verbose_name='Nome da Mãe',null=True,blank=True)
    nome_do_pai = models.CharField(max_length=100, verbose_name='Nome do Pai',null=True,blank=True)
    nome_do_responsavel = models.CharField(max_length=100, verbose_name='Nome do Responsável')
    telefone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Nº Telefone')
    celular_whatsapp = models.BooleanField(default=False ,verbose_name='Celular WhatsApp')
    telefone_para_recado = models.CharField(max_length=20, blank=True, null=True,verbose_name='Telefone para Recado')
    instituicao_de_ensino = models.CharField(max_length=225,verbose_name='Instituição de Ensino' ,null=True,blank=True)
    diagnotico = models.TextField(null=True,blank=True,verbose_name='Diagnóstico')
    nivel_de_escolaridade = models.CharField(max_length=255,verbose_name='Nível de Escolaridade')
    inicio_do_tratamento=models.DateField(default=date.today)


    

    class Meta:
        ordering =['nome_do_paciente']
        verbose_name_plural = "Pacientes"


    def __str__(self):
        return f'{self.nome_do_paciente}|{self.gerero}'
   
   
    