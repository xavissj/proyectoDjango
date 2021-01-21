from django.db import models
from django.utils import timezone

class Persona(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField()
    fecha_creado = models.DateTimeField(blank=True, null=True)

    def creacion(self):
        self. fecha_creado = timezone.now()
        self.save()
