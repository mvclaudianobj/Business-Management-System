# Generated by Django 2.0.5 on 2019-06-17 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_auto_20190501_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='mod_frete',
            field=models.CharField(choices=[('0', 'Por conta do remetente'), ('1', 'Por conta do destinatário'), ('2', 'Por conta de terceiros'), ('3', 'Transporte próprio do remetente'), ('4', 'Transporte próprio do destinatário'), ('9', 'Sem frete')], default='9', max_length=1),
        ),
    ]
