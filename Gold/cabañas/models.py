from django.db import models
from servicios.models import Servicio
from comodidades.models import Comodidad
from tipocabañas.models import Tipocabaña


class Cabaña(models.Model):
    nombre = models.CharField(max_length=25)
    capacidad = models.IntegerField()
    descripcion = models.CharField(max_length=25)
    status = models.BooleanField(default=True)
    comodidades = models.ForeignKey('comodidades.Comodidad', on_delete=models.DO_NOTHING, null=True)
    tipocabaña = models.ForeignKey('tipocabañas.Tipocabaña', on_delete=models.DO_NOTHING, null=True)

# Create your models here
