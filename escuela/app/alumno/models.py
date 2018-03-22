from django.db import models
from app.docente.models import Maestra
# Create your models here.

class Alumno(models.Model):
    folio = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    tutor = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    maestra = models.ForeignKey(Maestra, null=True, blank=True, on_delete=models.CASCADE)
