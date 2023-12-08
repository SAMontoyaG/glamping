from django.db import models
from reservas.models import Reserva
from servicios.models import Servicio

class Reservaservicio (models.Model):
    cantidad = models.IntegerField()
    valor = models.IntegerField()
    idReserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)   
    idServicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

# Create your models here.