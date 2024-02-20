from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Create your models here.

"""" Modelo para tabla Habilidades"""

class Habilidades(models.Model):
    
    habilidad = models.CharField('Habilidad', max_length=50)
    
    class meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'
        
    def __str__(self):
        
        return str(self.id) + '-' + self.habilidad

"""" Modelo para tabla Empleado"""
class Empleado (models.Model):
    
    Job_Choices = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Computación'),
    )
    
    first_name = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    full_name = models.CharField('Nombre completo',
                                 max_length=120,
                                 blank= True
                                 )
    
    job = models.CharField ('Trabajo', max_length=1, choices= Job_Choices)
    #Departamento (foreing key) (FK)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    #avatar
    habilidades = models.ManyToManyField(Habilidades)
    Hoja_Vida = RichTextField ()
    
    
    class Meta :
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['-first_name']
        unique_together = ('first_name','last_name')
    
    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name
    