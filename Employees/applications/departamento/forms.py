from django import forms

class NewDepartamentoForm (forms.Form):
    Nombre = forms.CharField(max_length=50)
    Apellidos = forms.CharField(max_length=50)
    departamento= forms.CharField(max_length=50)
    Shorname = forms.CharField(max_length=50)