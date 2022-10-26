from django.db import models

class Carros(models.Model):
    carro = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)


