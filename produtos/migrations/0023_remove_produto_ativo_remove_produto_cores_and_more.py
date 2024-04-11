# Generated by Django 5.0.3 on 2024-04-08 23:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0022_rename_imagem2_colecao_imagemsecundaria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='ativo',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='cores',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='estoque',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='imagem',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='imagemSecundaria',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='lancamento',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='outlet',
        ),
        migrations.CreateModel(
            name='VariacaoProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('imagemFrente', models.ImageField(blank=True, null=True, upload_to='images/fotos/%Y/%m/%d/')),
                ('imagemCostas', models.ImageField(blank=True, null=True, upload_to='images/fotos/%Y/%m/%d/')),
                ('imagemModelo', models.ImageField(blank=True, null=True, upload_to='images/fotos/%Y/%m/%d/')),
                ('estoque', models.PositiveIntegerField(default=0)),
                ('outlet', models.BooleanField(default=False)),
                ('ativo', models.BooleanField(default=True)),
                ('Produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.produto')),
            ],
        ),
    ]
