# Generated by Django 3.2.6 on 2021-08-21 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0012_car'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='plate',
        ),
    ]