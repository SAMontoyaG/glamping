from django.db import models
from cabañas.models import Cabaña
from clientes.models import Cliente

class Hospedaje(models.Model):
    fecha = models.DateField()
    total = models.IntegerField()
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    Cabaña = models.ForeignKey(Cabaña, on_delete=models.CASCADE)
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)