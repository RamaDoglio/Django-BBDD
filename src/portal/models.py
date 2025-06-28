from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class MetodoPago(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Cobro(models.Model):
    idMetodoPago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    total = models.FloatField()

    def __str__(self):
        return (
            f"{self.fecha} {self.hora} - {self.idMetodoPago.nombre} - ${self.total:.2f}"
        )


class TipoPlato(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class HorarioTurno(models.Model):
    horaInicio = models.TimeField()
    horaFin = models.TimeField()

    def __str__(self):
        return f"{self.horaInicio} - {self.horaFin}"


class Servicio(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class RolEmpleado(models.Model):
    nombre = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return self.nombre


class Empleado(models.Model):
    idRol = models.ForeignKey(RolEmpleado, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20, default=True)

    def __str__(self):
        return f"{self.nombre} ({self.idRol.nombre})"


class Sector(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Mesa(models.Model):
    numero = models.IntegerField(unique=True)
    capacidad = models.IntegerField()
    idSector = models.OneToOneField(Sector, on_delete=models.CASCADE)

    def __str__(self):
        return (
            f"Mesa {self.numero} ({self.capacidad} personas) - {self.idSector.nombre}"
        )


class Pedido(models.Model):
    idMesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fechaHoraEntrega = models.DateTimeField()
    fechaHoraPedido = models.DateTimeField()

    def __str__(self):
        return f"Pedido {self.id} - Mesa {self.idMesa.numero} - {self.fechaHoraPedido.strftime('%Y-%m-%d %H:%M')}"


class Turno(models.Model):
    idHorarioTurno = models.ForeignKey(HorarioTurno, on_delete=models.CASCADE)
    idServicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.idServicio.nombre} ({self.idHorarioTurno})"


class Plato(models.Model):
    nombre = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField()
    idTipoPlato = models.ForeignKey(TipoPlato, on_delete=models.CASCADE)
    precioUnitario = models.FloatField()

    def __str__(self):
        return f"{self.nombre} (${self.precioUnitario:.2f})"


class Factura(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idCobro = models.ForeignKey(Cobro, on_delete=models.CASCADE)
    total = models.FloatField()
    idPedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return (
            f"Factura {self.id} - {self.idCliente} - ${self.total:.2f} ({self.fecha})"
        )


class EstadoReserva(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    fechaRealizacionReserva = models.DateField()
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idTurno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    idEstadoReserva = models.ForeignKey(EstadoReserva, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reserva {self.id} - {self.idCliente} - {self.fechaRealizacionReserva} ({self.idEstadoReserva.nombre})"


class DetalleReserva(models.Model):
    idReserva = models.OneToOneField(Reserva, on_delete=models.CASCADE)
    idMesa = models.OneToOneField(Mesa, on_delete=models.CASCADE)

    def __str__(self):
        return f"DetalleReserva {self.id} - {self.idReserva} - {self.idMesa}"


class DetallePedido(models.Model):
    idPlato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    idPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subTotal = models.FloatField()

    def __str__(self):
        return f"{self.cantidad} x {self.idPlato.nombre} (Pedido {self.idPedido.id}) - Subtotal: ${self.subTotal:.2f}"


class DetalleFactura(models.Model):
    idPlato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    idFactura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subTotal = models.FloatField()

    def __str__(self):
        return f"{self.cantidad} x {self.idPlato.nombre} (Factura {self.idFactura.id}) - Subtotal: ${self.subTotal:.2f}"


class EmpleadoxSector(models.Model):
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    idSector = models.ForeignKey(Sector, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.idEmpleado} en {self.idSector.nombre}"
