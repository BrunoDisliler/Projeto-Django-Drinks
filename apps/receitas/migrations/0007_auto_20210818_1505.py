# Generated by Django 3.2.6 on 2021-08-18 18:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0006_alter_receita_data_receita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 18, 15, 5, 1, 256987)),
        ),
        migrations.AlterField(
            model_name='receita',
            name='ingredientes',
            field=models.CharField(max_length=500),
        ),
    ]
