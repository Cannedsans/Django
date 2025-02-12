from django.db import models

# Create your models here.
class Produto(models.Model):
    id = models.BigAutoField(primary_key= True)
    nome = models.CharField(max_length= 20)
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    estoque = models.IntegerField(default=0)