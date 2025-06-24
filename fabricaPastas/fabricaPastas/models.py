from django.db import models

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)

class MetodoPago(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField()

class Cobro(models.Model):
    idMetodoPago=models.ForeignKey(MetodoPago)
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
    idRol=models.ForeignKey(RolEmpleado)

class Sector(models.Model):
    nombre=models.CharField()
    descripcion=models.TextField()

class Mesa(models.Model):
    numero=models.IntegerField(unique=True)
    capacidad=models.IntegerField()
    idSector=models.ForeignKey(Sector,unique=True)

class Pedido(models.Model):
    idMesa=models.ForeignKey(Mesa)
    idEmpleado=models.ForeignKey(Empleado)
    fechaHoraEntrega=models.DateTimeField()
    fechaHoraPedido=models.DateTimeField()

class Turno(models.Model):
    idHorarioTurno=models.ForeignKey(HorarioTurno)
    idServicio=models.ForeignKey(Servicio)

class Plato(models.Model):
    nombre=models.CharField(max_length=50,unique=True)
    descripcion=models.TextField()
    idTipoPlato=models.ForeignKey(TipoPlato)
    precioUnitario=models.FloatField()

class Factura(models.Model):
    fecha=models.DateField()
    hora=models.TimeField()
    idCliente=models.ForeignKey(Cliente)
    idCobro=models.ForeignKey(Cobro)
    total=models.FloatField()
    idPedido=models.ForeignKey(unique=True)

class EstadoReserva(models.Model):
    nombre=models.CharField()

class Reserva(models.Model):
    fechaRealizacionReserva=models.DateField()
    idCliente=models.ForeignKey(Cliente)
    idTurno=models.ForeignKey(Turno)
    idEstadoReserva=models.ForeignKey(EstadoReserva)


class DetalleReserva(models.Model):
    idReserva=models.ForeignKey(unique=True)
    idMesa=models.ForeignKey(unique=True)

class DetallePedido(models.Model):
    idPlato=models.ForeignKey(Plato)
    idPedido=models.ForeignKey(Pedido)
    cantidad=models.IntegerField()
    subTotal=models.FloatField()

class DetalleFactura(models.Model):
    idPlato=models.ForeignKey(Plato)
    idFactura=models.ForeignKey(Factura)
    cantidad=models.IntegerField()
    subTotal=models.FloatField()

class ExS(models.Model):
    idEmpleado=models.ForeignKey(Empleado)
    idSector=models.ForeignKey(Sector)