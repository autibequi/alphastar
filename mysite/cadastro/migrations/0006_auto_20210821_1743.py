# Generated by Django 3.2.6 on 2021-08-21 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0005_client_social_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='gender',
            field=models.CharField(choices=[('m', 'Masculino'), ('f', 'Feminino')], default='m', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='social_name',
            field=models.CharField(blank=True, help_text='Nome que o cliente quer ser chamado.', max_length=200, verbose_name='Nome Social'),
        ),
    ]