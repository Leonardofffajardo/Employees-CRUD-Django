from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.
admin.site.register(Habilidades)#EmpleadoAdmin)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'job',
        'departamento',
        'full_name',
        'id'
    )
    # Funcion del Full name
    def full_name (self, obj):
        return obj.first_name + ' ' + obj.last_name
    
    search_fields = ('first_name',)
    
    list_filter = ('job','departamento')
    #
    filter_horizontal = ('habilidades',)
    


admin.site.register(Empleado,EmpleadoAdmin)
