# Generated by Django 5.0.3 on 2024-03-22 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('imagem', models.ImageField(upload_to='images/')),
                ('imagemSecundaria', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipo', models.CharField(choices=[('camisa', 'Camisa'), ('calca', 'Calça')], max_length=10)),
            ],
        ),
    ]
