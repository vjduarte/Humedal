from django.db import models
from applications.inicio.models import Humedal
# Create your models here.
class socio(models.Model):
    nombre=models.CharField('Nombre del socio',max_length=100)
    pagina=models.URLField(null=True)
    humedal=models.ForeignKey(Humedal,on_delete=models.CASCADE)

    class Meta:
        verbose_name='Socio del humedal'
        verbose_name_plural="Socios"
        ordering=['nombre']
        unique_together=('nombre','pagina')
        

    def __str__(self):
        return str(self.id)+self.nombre
    
class proyectos(models.Model):
    nombre=models.CharField('Nombre del proyecto',max_length=100)
    enlace=models.URLField()
    year=models.DateField()
    socio_proyecto=models.ForeignKey(socio,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)+self.nombre