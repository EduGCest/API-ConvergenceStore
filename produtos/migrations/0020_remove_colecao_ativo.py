# Generated by Django 5.0.3 on 2024-03-27 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0019_remove_colecao_imagem_remove_colecao_imagem2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colecao',
            name='ativo',
        ),
    ]
