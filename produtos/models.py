from datetime import datetime
from django.db import models

class Colecao(models.Model):

    titulo = models.CharField(max_length=100)
    descricao = models.TextField(default='Descrição da Coleção')  # Substitua 'Descrição do produto' pelo valor padrão desejado
    imagem = models.ImageField(upload_to='images/fotos/%Y/%m/%d/', default='https://convergence-store.s3.sa-east-1.amazonaws.com/static/images/Estatico/ImagemDefault.png')
    imagemSecundaria = models.ImageField(upload_to='images/fotos/%Y/%m/%d/', blank=True, null=True, default='https://convergence-store.s3.sa-east-1.amazonaws.com/static/images/Estatico/ImagemDefault.png')
    lancamento = models.DateTimeField(default=datetime.now)  # Default para data e hora atual
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class Produto(models.Model):
    TIPO_CHOICES = [
        ('Oversized', 'OVERSIZED'),
        ('Sweater', 'SWEATERS'),
    ]
    titulo = models.CharField(max_length=100)
    colecao = models.ForeignKey(Colecao, on_delete=models.CASCADE)
    descricao = models.TextField(default='Descrição do produto')  # Substitua 'Descrição do produto' pelo valor padrão desejado
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default=None)

    def __str__(self):
        return self.titulo

class VariacaoProduto(models.Model):

    COR_CHOICES = [
        ("PRETO", "Preto"),
        ("BRANCO", "Branco"),
        ("MARROM", "Marrom"),
    ]
    titulo = models.CharField(max_length=100)
    Produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cor = models.CharField(max_length=20, choices=COR_CHOICES, default="PRETO")  # Adicionando o campo cor

    imagemFrente = models.ImageField(upload_to='images/fotos/%Y/%m/%d/', blank=True, null=True)
    imagemCostas = models.ImageField(upload_to='images/fotos/%Y/%m/%d/', blank=True, null=True)
    imagemModelo = models.ImageField(upload_to='images/fotos/%Y/%m/%d/', blank=True, null=True)

    estoque = models.PositiveIntegerField(default=0)
    outlet = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo