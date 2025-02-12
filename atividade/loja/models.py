from django.db import models

# Create your models here.
class Vendedor(models.Model):
    cnpj = models.CharField(max_length=14, primary_key=True, verbose_name= "CNPJ")
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True,  verbose_name="E-mail")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")

class Produto(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Preço")
    estoque = models.IntegerField(default=0)
    fornecedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)

