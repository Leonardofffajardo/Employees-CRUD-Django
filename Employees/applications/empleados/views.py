from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
# MODELS 
from .models import Empleado
#FORMS
from .forms import EmpleadoForm

#Pantalla de inicio del proyecto

class InicioView(TemplateView):
    template_name = "inicio.html"




#Actidad de ListView
#Lista de todos los empleados / utilizar vistas en general

class List_AllempleadosListView(ListView):
    
    template_name = "empleados/list_all.html"
    paginate_by = 3
    ordering = 'first_name'
    context_object_name= 'empleados'
    def get_queryset(self):
        print ('++++++++++++++++++++++++')
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name__icontains=palabra_clave
        )
        print('Lista resultado:', lista)
        return lista   
    
#View para cada empleado en detalle

class Detail_EmpleadoListView(DetailView):
    model = Empleado
    template_name = 'empleados/detail.html'

# Lista de los empleados de un area
#Diferentes formas de listar mientras hacemos un filtro

class List_byempleadosListView(ListView):
    model = Empleado
    template_name = "empleados/List_area.html"
    context_object_name = 'empleados'
    #1 forma de hacer el filtro
    '''queryset = Empleado.objects.filter(
        departamento__shor_name = 'Informática'
    )'''
    
    #Filtro con funcion:
    def get_queryset(self):
        #aqui pondriamos el codigo que necesitamos
            #definimos el area
        area = self.kwargs ['shorname']
        lista = Empleado.objects.filter(
        departamento__shor_name = area
    )
        return lista
    
#ADMINISTRAR

class List_Empleados_admin(ListView):
    template_name = "empleados/lista_empleados.html"
    context_object_name = 'empleados'
    ordering= 'id'
    context_object_name= 'empleados'
    model= Empleado
    paginate_by = 5
    
# Listar los empleados por trabajo   
# Practica, similar a la anterior 

class Byjob_ListView(ListView):
    model = Empleado
    template_name = "empleados/list_job.html"
    context_object_name = 'Empleado'
    
    def get_queryset(self):
        
        jobs = self.kwargs ['jobs']
        lista = Empleado.objects.filter(    
        job = jobs
    )
        
        return lista

# Listar empleados por Kword
#utilizar peticiones Get y filtrar con ellas
class ByKwordListView(ListView):

    template_name = 'empleados/k_word.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print ('++++++++++++++++++++++++')
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        print('Lista resultado:', lista)
        return lista    

#Listar habilidades de un empleado 
#many to many

class Habilidades_empleadosListView(ListView):
    template_name = "empleados/habilidades.html"
    context_object_name = 'habilidades' 
    
    def get_queryset(self):
        empleado = Empleado.objects.get(id=7)
        print (empleado.habilidades.all())
        return (empleado.habilidades.all())

#Detail view

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleados/detail_empleado.html"
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        #todo un proceso
        context["titulo"] = 'empleado del mes'
        return context
    
#View para cuando un empleado se registre exitosamente

class SuccessView(TemplateView):
    template_name = "empleados/success.html"

#Create View

class EmpleadoCreateView(CreateView):
    
    model = Empleado
    template_name = "empleados/add.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy ('persona_app:list_admin')
    
    def form_valid(self, form):
        #logica del proceso
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView,self).form_valid(form)

#Para editar o eliminar el modelo de un empleado
#Update View

class EmpleadoUpdateView(UpdateView):
            
    template_name = "empleados/update.html"
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy ('persona_app:list_admin')
    
    def post(self,request,*args,**kwargs):
        self.object = self.get_object
        return super().post(request,*args,**kwargs)
    

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleados/delete.html"
    success_url = reverse_lazy('persona_app:list_admin')
