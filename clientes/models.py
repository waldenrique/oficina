from django.db import models


class Clientes(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    endereço = models.CharField(max_length=100)
    obs = models.TextField()
   
    Feminino = 'F'
    Masculino = 'M'
    
    sexo_op = [
        (Feminino, 'Feminino'),
        (Masculino, 'Masculino'),
       
    ]
    Sexo = models.CharField(
        max_length=1,
        choices=sexo_op,
        default=Masculino,
    )
    def __str__(self) :
        return self.nome


