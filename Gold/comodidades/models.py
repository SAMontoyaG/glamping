from django.db import models
class Comodidad(models.Model):
    nombre = models.CharField(max_length=40)
    status = models.BooleanField(default=True)
    
def __str__(self):
    return self.nombre


# Create your models here.
