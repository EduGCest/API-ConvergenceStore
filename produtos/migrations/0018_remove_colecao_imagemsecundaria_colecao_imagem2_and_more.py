# Generated by Django 5.0.3 on 2024-03-27 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0017_colecao_ativo_colecao_imagem_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colecao',
            name='imagemSecundaria',
        ),
        migrations.AddField(
            model_name='colecao',
            name='imagem2',
            field=models.ImageField(blank=True, default='https://convergence-store.s3.sa-east-1.amazonaws.com/static/images/Estatico/ImagemDefault.png', null=True, upload_to='images/fotos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='colecao',
            name='imagem',
            field=models.ImageField(default='https://convergence-store.s3.sa-east-1.amazonaws.com/static/images/Estatico/ImagemDefault.png', upload_to='images/fotos/%Y/%m/%d/'),
        ),
    ]
