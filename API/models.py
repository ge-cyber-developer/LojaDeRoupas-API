from django.db import models


class Peca(models.Model):
    nome = models.CharField(max_length=30)
    tamanho = models.CharField(max_length=30)