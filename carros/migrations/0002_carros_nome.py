# Generated by Django 4.1.2 on 2022-10-26 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
        ('carros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carros',
            name='nome',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='clientes.clientes'),
            preserve_default=False,
        ),
    ]
