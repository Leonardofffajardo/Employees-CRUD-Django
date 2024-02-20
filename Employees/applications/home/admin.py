from django.contrib import admin
from .models import prueba, Fprueba, Cprueba

admin.site.register(prueba)

class prueba_admin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'subtitulo',
        'cantidad',
    )

class FpruebaAdmin (admin.ModelAdmin):
    list_display = (
        'Ftitulo',
        'Fsubtitulo',
        'Fcantidad',
    )
    
class CpruebaAdmin (admin.ModelAdmin):
    list_display = (
        'Ctitulo',
        'Csubtitulo',
        'Ccantidad',
    )
    
admin.site.register(Cprueba,CpruebaAdmin)
admin.site.register(Fprueba,FpruebaAdmin)