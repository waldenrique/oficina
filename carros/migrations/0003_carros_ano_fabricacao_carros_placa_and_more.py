# Generated by Django 4.1.2 on 2022-10-30 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0002_carros_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='carros',
            name='Ano_fabricacao',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carros',
            name='Placa',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carros',
            name='carro',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='carros',
            name='marca',
            field=models.CharField(max_length=50),
        ),
    ]
