from django.db import models

class Remedio(models.Model):
    nome = models.CharField(max_length=100)
    tarja = models.CharField(max_length=20)
    precisa_receita = models.CharField(max_length=3, default="Não")
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

# Create your models here.
