# Generated by Django 5.0.3 on 2024-03-22 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0011_alter_produto_colecao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='colecao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.colecoes'),
        ),
    ]