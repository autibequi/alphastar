# Generated by Django 3.2.6 on 2021-08-21 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_client_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='cpf',
            field=models.CharField(max_length=11),
        ),
    ]