from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
        # cpf, genero, estado civil, doador, observacoes, foto.

class Client(models.Model):
    MASCULINO = 'm'
    FEMININO = 'f'
    GENDER_CHOICES = [
        (MASCULINO, 'Masculino'),
        (FEMININO, 'Feminino')
    ]
    SOLTEIRO = 'sol'
    CASADO = 'cas'
    DIVORCIADO = 'div'
    VIUVO = 'viu'
    ESTADO_CIVIL_CHOICES = [
        (SOLTEIRO, 'Solteiro'),
        (CASADO, 'Casado'),
        (DIVORCIADO, 'Divorciado'),
        (VIUVO, 'Viuvo')
    ]
    name = models.CharField(max_length=200, verbose_name='Nome')
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    social_name = models.CharField(max_length=200, blank=True, verbose_name='Nome Social', help_text='Nome que o cliente quer ser chamado.')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Gênero' )
    estado_civil = models.CharField(max_length=3, choices= ESTADO_CIVIL_CHOICES )
    organ_donor = models.BooleanField(verbose_name='doador de órgãos')
    observation = models.TextField(max_length=500, verbose_name='observações')
    picture = models.ImageField(verbose_name='foto')

    def __str__(self):
        return self.name

class Instructor(models.Model):
     name = models.CharField(max_length=200, verbose_name='Nome')


     def __str__(self):
        return self.name

class Car(models.Model):
     model = models.CharField(max_length=200, verbose_name='Modelo')
     plate = models.CharField(max_length=7, verbose_name='Placa', unique=True)
     year = models.CharField(max_length=4, verbose_name='Ano')

     def __str__(self):
        return self.model

class AutoClass(models.Model):
     car = models.ForeignKey(Car, verbose_name='Carro', on_delete = CASCADE)
     instructor = models.ForeignKey(Instructor, verbose_name='Instrutor', on_delete = CASCADE)
     client = models.ForeignKey(Client, verbose_name='Cliente', on_delete = CASCADE)
     date = models.DateField(verbose_name='Data')

  




