# Generated by Django 5.0.3 on 2024-03-27 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0018_remove_colecao_imagemsecundaria_colecao_imagem2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colecao',
            name='imagem',
        ),
        migrations.RemoveField(
            model_name='colecao',
            name='imagem2',
        ),
    ]
