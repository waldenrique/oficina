from django.db import models
from clientes.models import Clientes

class Carros(models.Model):
    nome = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    carro = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)


