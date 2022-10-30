from logging import PlaceHolder
from django.db import models
from clientes.models import Clientes


class Carros(models.Model):
    nome = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    carro = models.CharField(max_length=50)
    Placa = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    Modelo = models.CharField(max_length=50)
    Versão = models.CharField(max_length=50)
    Ano_fabricação = models.CharField(max_length=50)
    chassi = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)
    obs_carro = models.TextField()
  
    def __str__(self) :
        return self.carro
    
