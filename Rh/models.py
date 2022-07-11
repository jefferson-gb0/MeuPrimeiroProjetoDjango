
from mailbox import NotEmptyError
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Departamento(models.Model):
    nome = models.CharField(max_length=20) 


    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    CARGO = [
        ('ES','ESTAGIARIO'),
        ('AS', 'ASSISTENTE'),
        ('JR','JUNIOR'),
        ('PL', 'PLENO'),
        ('SN', 'SENIOR'),
        ('GR', 'GERENTE'),
        
    ]
    matricula = models.IntegerField()
    nome = models.CharField(max_length=50)
    cargo = models.CharField(max_length=2,choices=CARGO)
    departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    data_nascimento = models.DateField(null=True)


