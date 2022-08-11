from django.db import models


# Create your models here.
from brasileirao.times.models import Times


class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    time = models.ForeignKey(Times, on_delete=models.CASCADE)
    idade = models.IntegerField()
    posicao = models.CharField(max_length=25)

    def __str__(self):
        return self.nome
