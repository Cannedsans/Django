from django.db import models
# se eu soubresse que a próxima atv era basseada nisso tinha feito menor 

# Create your models here.
class Autor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    nacionalidade = models.CharField(max_length=30, null=True, blank=True)
    biografia = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

class Livro(models.Model):
    id = models.BigAutoField(primary_key = True)
    titulo = models.CharField(max_length=20)
    sub_titulo = models.CharField(max_length=20, null=True)
    genero = models.CharField(max_length=10)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.titulo} {self.sub_titulo}"
    
class Cliente(models.Model):
    cpf = models.CharField(primary_key=True, max_length=14)
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    idade = models.IntegerField()
    endereco = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"


class Emprestismo(models.Model):
    id = models.BigAutoField(primary_key= True)
    idlivro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    idcliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()

#INSERT INTO biblioteca_autor (nome, sobrenome, nacionalidade) VALUES(
#    "Gustavo", "Azevedo", "brasileiro"
#);
#INSERT INTO biblioteca_livro (titulo, genero, autor_id) VALUES(
#    "Lendas do mar mediterrâneo", "ficção", 2
#);
# SELECT * FROM biblioteca_livro;
#UPDATE biblioteca_livro set autor_id = 1 WHERE autor_id = 2;
# SELECT * FROM biblioteca_livro;
#DELETE FROM biblioteca_autor WHERE id = 2;
