from django.contrib import admin

# Register your models here.

from .models import Ciudad,Cliente,Comuna,Boleta,DetalleBoleta,DetalleOc,DetalleVenta,Direccion,DireccionCli,DireccionEmp,Empleado,EstadoOrden,EstadoPedido,EstadoVenta,Factura,FamiliaProducto,OrdenCompra,Pedido,Producto,Proveedor,RespaldoVenta,TipoEmpleado,TipoProducto,TipoVivienda,UsuarioCliente,UsuarioEmpleado,Venta, EstadoEmpleado, EstadoCli
# Register your models here.

admin.site.register(Ciudad)
admin.site.register(Cliente)
admin.site.register(Comuna)
admin.site.register(Boleta)
admin.site.register(DetalleBoleta)
admin.site.register(DetalleOc)

admin.site.register(DetalleVenta)
admin.site.register(Direccion)
admin.site.register(DireccionCli)
admin.site.register(DireccionEmp)
admin.site.register(Empleado)
admin.site.register(EstadoOrden)
admin.site.register(EstadoPedido)
admin.site.register(EstadoVenta)
admin.site.register(Factura)
admin.site.register(FamiliaProducto)
admin.site.register(OrdenCompra)

admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(RespaldoVenta)
admin.site.register(TipoEmpleado)
admin.site.register(TipoProducto)
admin.site.register(TipoVivienda)

admin.site.register(UsuarioCliente)
admin.site.register(UsuarioEmpleado)
admin.site.register(Venta)

admin.site.register(EstadoEmpleado)
admin.site.register(EstadoCli)
