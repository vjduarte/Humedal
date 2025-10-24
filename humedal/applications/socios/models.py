from django.db import models
from applications.inicio.models import Humedal
# Create your models here.
class socio(models.Model):
    nombre=models.CharField('Nombre del socio',max_length=100)
    humedal=models.ForeignKey(Humedal,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)+self.nombre