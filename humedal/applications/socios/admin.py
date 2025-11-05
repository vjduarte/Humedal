from django.contrib import admin

from .models import *
# Register your models here.
class SocioAdmin(admin.ModelAdmin):
    list_display=(
        'nombre',
        'pagina',
        'humedal'
    )
    search_fields=('nombre',)
    fieldsets = (
        ("general", {"fields": ("humedal", )}),
       
    )
    list_filter = ("nombre",)

    # Render filtered options only after 5 characters were entered
    filter_input_length = {
        "nombre": 5,
    }
    

admin.site.register(socio,SocioAdmin)
admin.site.register(proyectos)
