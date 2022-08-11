from django.db import models


# Create your models here.

class Times(models.Model):
    nome = models.CharField(max_length=64)

    def __str__(self):
        return self.nome
