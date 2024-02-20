from django.db import models

# Create your models here.

class prueba(models.Model):
    titulo= models.CharField(("Titulo"), max_length=70),
    subtitulo= models.CharField(("Subtitulo"), max_length=70, blank= True),
    cantidad= models.CharField(("Cantidad"), max_length=70),
    
    def __str__(self) -> str:
        return str(self.id) + '-' + self.titulo + '-' + self.subtitulo + '-' + self.cantidad 
    
class Fprueba (models.Model):
    Ftitulo= models.CharField(("Titulo"), max_length=70),
    Fsubtitulo= models.CharField(("Subtitulo"), max_length=70, blank= True),
    Fcantidad= models.CharField(("Cantidad"), max_length=70),
    
    def __str__(self) -> str:
        return str(self.id) + '-' + self.Ftitulo + '-' + self.Fsubtitulo + '-' + self.Fcantidad
    
class Cprueba (models.Model):
    Ctitulo= models.CharField(("Titulo"), max_length=70),
    Csubtitulo= models.CharField(("Subtitulo"), max_length=70, blank= True),
    Ccantidad= models.CharField(("Cantidad"), max_length=70),
    
    def __str__(self) -> str:
        return str(self.id) + '-' + self.Ctitulo + '-' + self.Csubtitulo + '-' + self.Ccantidad