from django.contrib import admin
from .models import *

# Register your models here.
class HumedalAdmin(admin.ModelAdmin):
    list_display=(
       'nombre', 
       'Descripcion',
       'localizacion',
    )
    search_fields=('nombre',)

admin.site.register(Humedal,HumedalAdmin)
admin.site.register(Evento)
admin.site.register(especies)
