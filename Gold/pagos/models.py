from django.db import models


class Pago(models.Model):
    fecha = models.DateField()
    valor = models.IntegerField()
    status = models.BooleanField(default=True)


# Create your models here.
