from django.db import models


class Banner(models.Model):

    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='images/banner/')
    ativo = models.BooleanField()

    def __str__(self):
        return self.titulo
    
class Lancamento(models.Model):

    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='images/lancamentos/')
    ativo = models.BooleanField()
    posicao = models.BooleanField(default=True)


    def __str__(self):
        return self.titulo

class Secao(models.Model):

    titulo = models.CharField(max_length=100)
    imagem1 = models.ImageField(upload_to='images/secoes/', default=None)
    imagem2 = models.ImageField(upload_to='images/secoes/', default=None)
    imagem3 = models.ImageField(upload_to='images/secoes/', default=None)
    ativo = models.BooleanField()


    def __str__(self):
        return self.titulo