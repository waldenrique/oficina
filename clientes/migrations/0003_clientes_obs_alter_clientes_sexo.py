# Generated by Django 4.1.2 on 2022-10-30 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_clientes_sexo_clientes_cpf_clientes_endereço_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='obs',
            field=models.TextField(default=2022),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientes',
            name='Sexo',
            field=models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino')], default='M', max_length=1),
        ),
    ]
