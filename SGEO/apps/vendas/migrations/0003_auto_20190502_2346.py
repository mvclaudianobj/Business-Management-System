# Generated by Django 2.0.5 on 2019-05-03 02:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0002_auto_20190502_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condicaopagamento',
            name='dia_pagamento',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(31)]),
        ),
    ]
