from django.shortcuts import render
from .models import prueba, Fprueba
from django.views.generic import (
    CreateView,
)
# Create your views here.

class PruebaCreateView(CreateView):
    model = prueba
    template_name = "home/add.html"
    fields = ('__all__')
    success_url= '/'


class FpruebaCreateView(CreateView):
    model = Fprueba
    template_name = "home/fadd.html"
    fields = ('__all__')
    success_url = '/'

