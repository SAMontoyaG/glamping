from django.db import models

class Servicio(models.Model):
    nombre = models.CharField(max_length=40)
    valor = models.IntegerField()
    status = models.BooleanField(default=True)

def __str__(self):
        return self.nombre


# Create your models here.
