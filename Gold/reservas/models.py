from django.db import models
from clientes.models import Cliente
from cabañas.models import Cabaña

class Reserva(models.Model):   
    fecha = models.DateField()
    total = models.IntegerField()
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    status = models.BooleanField(default=True)
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.fecha


# Create your models here.
