from django.db import models
from cabañas.models import Cabaña
from comodidades.models import Comodidad

class Tipocomodidad (models.Model):
    cantidad = models.IntegerField()
    idCabaña = models.ForeignKey(Cabaña, on_delete=models.CASCADE )
    idComodidad = models.ForeignKey(Comodidad, on_delete=models.CASCADE)
    
    
# Create your models here.
