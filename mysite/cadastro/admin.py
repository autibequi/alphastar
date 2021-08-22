from django.contrib import admin
from .models import AutoClass, Client, Instructor, Car
from django import forms
from django.core.exceptions import ValidationError

class ClientForm(forms.ModelForm):
    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if len(cpf) != 11:
            raise ValidationError(('Este campo deve conter 11 caracteres'), code='invalid')

        return cpf
        
    class Meta:
        model = Client
        fields = '__all__'


@admin.register(Client)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf',)
    form = ClientForm

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    pass
class CarForm(forms.ModelForm):
    def clean_year(self):
        year = self.cleaned_data['year']
        if int(year) < 2015:
            raise ValidationError(('Este carro é muito velho para ser usado em uma auto escola'), code='invalid')

        return year    
    class Meta:
        model = Car
        fields = '__all__'

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    form = CarForm

@admin.register(AutoClass)
class AutoClassAdmin(admin.ModelAdmin):
     list_display = ('client', 'date',)
    

  

    # modelo instrutor campo nome
    # modelo carro campo modelo, placa
    # modelo aula campo instrutor, carro, cliente, data