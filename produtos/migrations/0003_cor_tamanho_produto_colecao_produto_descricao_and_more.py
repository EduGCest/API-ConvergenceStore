# Generated by Django 5.0.3 on 2024-03-22 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_alter_produto_imagem_alter_produto_imagemsecundaria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tamanho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='produto',
            name='colecao',
            field=models.CharField(choices=[('none', 'Nenhuma'), ('colecao2', 'Coleção 2')], default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='produto',
            name='descricao',
            field=models.TextField(default='Descrição do produto'),
        ),
        migrations.AddField(
            model_name='produto',
            name='estoque',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='produto',
            name='lancamento',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('camisa', 'Camisa'), ('calca', 'Calça')], default='camisa', max_length=10),
        ),
        migrations.AddField(
            model_name='produto',
            name='coresDisponiveis',
            field=models.ManyToManyField(to='produtos.cor'),
        ),
        migrations.AddField(
            model_name='produto',
            name='tamanhosDisponiveis',
            field=models.ManyToManyField(to='produtos.tamanho'),
        ),
    ]