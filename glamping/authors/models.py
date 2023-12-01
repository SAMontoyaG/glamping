from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    document = models.CharField(max_length=20, unique=True)
    nationality = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
# Create your models here.
class TipoCabaña(models.Model):
    Nombre = models.CharField(max_length=25)

class Cabaña(models.Model):
    Name = models.CharField(max_length=25)
    Capacity = models.IntegerField()
    Descripcion = models.CharField(max_length=25)
    IdTipoCabaña = models.ForeignKey(TipoCabaña, on_delete=models.CASCADE)

class Comodidad(models.Model):
    Nombre = models.CharField(max_length=40)

class Cabaña_comodidad(models.Model):
    IdCabaña = models.ForeignKey(Cabaña, on_delete=models.CASCADE)
    IdComodidad = models.ForeignKey(Comodidad, on_delete=models.CASCADE)
    Cantidad = models.IntegerField()

class Cliente(models.Model):
    Nombre = models.CharField(max_length=255)
    Apellido = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)
    Telefono = models.CharField(max_length=20)

class ReservaVenta(models.Model):
    IdCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Fecha = models.DateField()
    IdCabaña = models.ForeignKey(Cabaña, on_delete=models.CASCADE)
    Total = models.IntegerField()
    FechaInicio = models.DateField()
    FechaFin = models.DateField()

class Servicio(models.Model):
    Nombre = models.CharField(max_length=40)
    Valor = models.IntegerField()

class Reserva_Servicio(models.Model):
    IdReservaVenta = models.ForeignKey(ReservaVenta, on_delete=models.CASCADE)
    IdServicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    Cantidad = models.IntegerField()
    Valor = models.IntegerField()

class Pago(models.Model):
    Fecha = models.DateField()
    Valor = models.IntegerField()
    IdReservaVenta = models.ForeignKey(ReservaVenta, on_delete=models.CASCADE)

class Calificacion(models.Model):
    IdReservaVenta = models.ForeignKey(ReservaVenta, on_delete=models.CASCADE)
    Puntuacion = models.IntegerField()

class Reserva_Cabaña(models.Model):
    IdReservaVenta = models.ForeignKey(ReservaVenta, on_delete=models.CASCADE)
    IdCabaña = models.ForeignKey(Cabaña, on_delete=models.CASCADE)