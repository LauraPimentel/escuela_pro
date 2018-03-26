from django.db import models

# Create your models here.
class Maestra(models.Model):
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=50)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    domicilio = models.CharField(max_length=40)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)
