from django.db import models
from clientes.models import Clientes
from carros.models import Carros

class Ordens(models.Model):
    nome = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    carro = models.ForeignKey(Carros, on_delete=models.CASCADE)
    ordem = models.CharField(max_length=50)
    data_entrada = models.CharField(max_length=50)
    data_saida = models.CharField(max_length=50)
    km = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)
    situacao = models.CharField(max_length=50)
    localizacao = models.CharField(max_length=50)
    reboque = models.CharField(max_length=50)
    retorno = models.CharField(max_length=50)
    obs_int = models.TextField()
    obs_cliente = models.TextField()
  
    def __str__(self) :
        return self.ordem
    
