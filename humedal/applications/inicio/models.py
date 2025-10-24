from django.db import models

# Create your models here.

class Humedal(models.Model):
    nombre=models.CharField('Nombre Humedal',max_length=150,null=False)
    localizacion=models.CharField('Localización',max_length=200,null=False)
    Descripcion=models.TextField("Descripción",null=False)
    #foto=models.ImageField()

    def __str__(self):
        return str(self.id)+'-'+self.nombre

class Evento(models.Model):
    nombre_evento=models.CharField('Nombre del evento',max_length=200,null=False)
    Descripcion=models.TextField('Descripción del evento',null=False)
    fecha=models.DateField('Fecha del evento')
    url_evento=models.URLField()
    humedal=models.ForeignKey(Humedal,on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.id)+'-'+self.nombre_evento

  
