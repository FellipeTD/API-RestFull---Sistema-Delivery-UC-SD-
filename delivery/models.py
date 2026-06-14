from django.db import models

# Create your models here.
'''Id 
Nome 
E-mail 
Não pode estar em branco 
CPF 
Máximo de 11 caracteres 
Data de Nascimento 
Número de Celular 
Máximo de 14 caracteres'''

class user(models.Model):
    nome = models.CharField(max_length = 100)
    email = models.EmailField(blank = False, max_length = 30)
    cpf = models.CharField(max_length = 11)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length = 14)

def __str__(self):
        return self.nome

''' 
Id 
Código 
  Máximo de 10 caracteres 
Descrição 
  Não pode estar em Branco 
Categoria (Filme, Série e Documentário) 
  Não pode estar em Branco 
  Não pode ser Nulo 
  Por padrão deve ser Filme'''