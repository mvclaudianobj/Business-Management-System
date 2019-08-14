# Generated by Django 2.0.5 on 2019-06-21 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Relatorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('acessar_relatorio_clientes', 'Acessar Clientes'), ('acessar_relatorio_entradas', 'Acessar Entradas'), ('acessar_relatorio_saidas', 'Acessar Saídas'), ('acessar_relatorio_produtos', 'Acessar Produtos'), ('acessar_relatorio_vendas', 'Acessar Vendas'), ('acessar_relatorio_dre', 'Acessar DRE')),
                'managed': False,
            },
        ),
    ]