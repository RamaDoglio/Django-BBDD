from django.contrib import admin

from .models import *

admin.site.register(Cliente)
admin.site.register(MetodoPago)
admin.site.register(Cobro)
admin.site.register(TipoPlato)
admin.site.register(HorarioTurno)
admin.site.register(Servicio)
admin.site.register(RolEmpleado)
admin.site.register(Empleado)
admin.site.register(Sector)
admin.site.register(Mesa)
admin.site.register(Pedido)
admin.site.register(Turno)
admin.site.register(Plato)
admin.site.register(Factura)
admin.site.register(EstadoReserva)
admin.site.register(Reserva)
admin.site.register(DetalleReserva)
admin.site.register(DetallePedido)
admin.site.register(DetalleFactura)
admin.site.register(EmpleadoxSector)
