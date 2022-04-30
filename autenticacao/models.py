from django.db import models
from django.contrib.auth.models import AbstractUser


cargos_choice = (('Adminidado','Adminidado'),
                    ())


class User(AbstractUser):
    #cargo = models.CharField(max_length=100,unique=False,choices=None)
    pass



