# Generated by Django 3.2.6 on 2021-08-21 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0010_client_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
            ],
        ),
    ]
