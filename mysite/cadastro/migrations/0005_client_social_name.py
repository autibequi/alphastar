# Generated by Django 3.2.6 on 2021-08-21 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_alter_client_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='social_name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
