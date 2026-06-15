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
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=14)


    def __str__(self):
        return self.nome


''' 
Id 
Código 
  Máximo de 10 caracteres 
Descrição 
  Não pode estar em Branco 
Categoria (Restaurante, Pizzaria, Hamburgueria, Food Truck) 
  Não pode estar em Branco 
  Não pode ser Nulo 
  Por padrão deve ser Restaurante'''


class estabelecimento(models.Model):
    CATEGORIA = (
        ('R', 'Restaurante'),
        ('P', 'Pizzaria'),
        ('H', 'Hamburgueria'),
        ('F', 'Food Truck'),
    )

    codigo = models.CharField(max_length=15)
    descricao = models.CharField(max_length=100, blank=False)
    categoria = models.CharField(
        max_length=1,
        choices=CATEGORIA,
        blank=False,
        null=False,
        default='R'
    )


    def __str__(self):
        return self.codigo

    """lista de usuário"""

class lista(models.Model):
    user = models.ForeignKey(user,on_delete = models.CASCADE)
    estabelecimento = models.ForeignKey(estabelecimento,on_delete = models.CASCADE)

class produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estabelecimento = models.ForeignKey(
        estabelecimento,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nome

class pedido(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)

class endereco(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
