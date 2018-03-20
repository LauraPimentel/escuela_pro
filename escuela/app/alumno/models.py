from django.db import models
from app.docente.models import Maestra
# Create your models here.

class Alumno(models.Model):
    folio = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido_p = models.CharField(max_length=20)
    apellido_m = models.CharField(max_length=20)
    edad = models.IntegerField()
    fecha_nac = models.DateField()
    tutor = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    
