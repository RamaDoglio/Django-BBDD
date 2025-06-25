from django.db import models

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)

class MetodoPago(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField()

class Cobro(models.Model):
    idMetodoPago=models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    fecha=models.DateField()
    hora=models.TimeField()
    total=models.FloatField()

class TipoPlato(models.Model):
    nombre=models.CharField()
    descripcion=models.TextField()

class HorarioTurno(models.Model):
    horaInicio=models.TimeField()
    horaFin=models.TimeField()

class Servicio(models.Model):
    nombre=models.CharField()
    descripcion=models.TextField()

class RolEmpleado(models.Model):
    nombre=models.CharField(unique=True)

class Empleado(models.Model):
    idRol=models.ForeignKey(RolEmpleado, on_delete=models.CASCADE)

class Sector(models.Model):
    nombre=models.CharField()
    descripcion=models.TextField()

class Mesa(models.Model):
    numero=models.IntegerField(unique=True)
    capacidad=models.IntegerField()
    idSector=models.ForeignKey(Sector, on_delete=models.CASCADE,unique=True)

class Pedido(models.Model):
    idMesa=models.ForeignKey(Mesa,on_delete=models.CASCADE)
    idEmpleado=models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fechaHoraEntrega=models.DateTimeField()
    fechaHoraPedido=models.DateTimeField()

class Turno(models.Model):
    idHorarioTurno=models.ForeignKey(HorarioTurno, on_delete=models.CASCADE)
    idServicio=models.ForeignKey(Servicio, on_delete=models.CASCADE)

class Plato(models.Model):
    nombre=models.CharField(max_length=50,unique=True)
    descripcion=models.TextField()
    idTipoPlato=models.ForeignKey(TipoPlato, on_delete=models.CASCADE)
    precioUnitario=models.FloatField()

class Factura(models.Model):
    fecha=models.DateField()
    hora=models.TimeField()
    idCliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idCobro=models.ForeignKey(Cobro, on_delete=models.CASCADE)
    total=models.FloatField()
    idPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, unique=True)
class EstadoReserva(models.Model):
    nombre=models.CharField()

class Reserva(models.Model):
    fechaRealizacionReserva=models.DateField()
    idCliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idTurno=models.ForeignKey(Turno, on_delete=models.CASCADE)
    idEstadoReserva=models.ForeignKey(EstadoReserva, on_delete=models.CASCADE)


class DetalleReserva(models.Model):
    idReserva=models.ForeignKey(Reserva, on_delete=models.CASCADE, unique=True)
    idMesa=models.ForeignKey(Mesa, on_delete=models.CASCADE, unique=True)

class DetallePedido(models.Model):
    idPlato=models.ForeignKey(Plato, on_delete=models.CASCADE)
    idPedido=models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad=models.IntegerField()
    subTotal=models.FloatField()

class DetalleFactura(models.Model):
    idPlato=models.ForeignKey(Plato,on_delete=models.CASCADE)
    idFactura=models.ForeignKey(Factura, on_delete=models.CASCADE)
    cantidad=models.IntegerField()
    subTotal=models.FloatField()

class ExS(models.Model):
    idEmpleado=models.ForeignKey(Empleado, on_delete=models.CASCADE)
    idSector=models.ForeignKey(Sector, on_delete=models.CASCADE)