from django.db import models
 
class Departamento(models.Model):
 # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
 nombre = models.CharField(max_length=50)
 telefono = models.IntegerField()
 def __str__(self):
        return self.nombre

class Habilidad(models.Model):
 # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
 nombre = models.CharField(max_length=50)
 def __str__(self):
        return self.nombre
 
class Empleado(models.Model):
 # Campo para la relación one-to-many
 departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
 habilidades = models.ManyToManyField(Habilidad)
 nombre = models.CharField(max_length=40)
 fecha_nacimiento = models.DateField()
 # Es posible indicar un valor por defecto mediante 'default'
 antiguedad = models.IntegerField(default=0)
 # Para permitir propiedades con valor null, añadiremos las opciones null=True, blank=True.        	
 foto = models.ImageField(upload_to='img',blank=True,null=True,verbose_name='Image')
 def __str__(self):
        return self.nombre