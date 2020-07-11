# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrador(models.Model):
    rut = models.BigIntegerField(primary_key=True)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    correo = models.CharField(max_length=50)
    estado_admin_id_estado = models.ForeignKey('EstadoAdmin', models.DO_NOTHING, db_column='estado_admin_id_estado')
    nombre = models.CharField(max_length=20)
    apaterno = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'administrador'


class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    total = models.BigIntegerField()
    estado_venta_id_estado_venta = models.ForeignKey('EstadoVenta', models.DO_NOTHING, db_column='estado_venta_id_estado_venta')

    class Meta:
        managed = False
        db_table = 'boleta'


class Ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ciudad'


class Cliente(models.Model):
    rut_cliente = models.BigIntegerField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apaterno = models.CharField(max_length=50)
    amaterno = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    telefono_2 = models.BigIntegerField(blank=True, null=True)
    correo = models.CharField(max_length=50)
    rut_empresa = models.BigIntegerField(blank=True, null=True)
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    giro = models.CharField(max_length=50, blank=True, null=True)
    estado_cli_id_estado_cli = models.ForeignKey('EstadoCli', models.DO_NOTHING, db_column='estado_cli_id_estado_cli')

    class Meta:
        managed = False
        db_table = 'cliente'


class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    ciudad_id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='ciudad_id_ciudad')

    class Meta:
        managed = False
        db_table = 'comuna'


class DetalleBoleta(models.Model):
    boleta_id_boleta = models.ForeignKey(Boleta, models.DO_NOTHING, db_column='boleta_id_boleta')
    producto_id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_id_producto')
    cantidad = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'detalle_boleta'


class DetalleFactura(models.Model):
    factura_id_factura = models.ForeignKey('Factura', models.DO_NOTHING, db_column='factura_id_factura')
    producto_id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_id_producto')
    cantidad = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'detalle_factura'


class DetalleOc(models.Model):
    orden_compra_id_orden_compra = models.ForeignKey('OrdenCompra', models.DO_NOTHING, db_column='orden_compra_id_orden_compra')
    producto_id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_id_producto')
    cantidad = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'detalle_oc'


class DetallePedido(models.Model):
    pedido_id_pedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='pedido_id_pedido')
    producto_id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_id_producto')

    class Meta:
        managed = False
        db_table = 'detalle_pedido'


class DetalleVenta(models.Model):
    venta_id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='venta_id_venta')
    producto_id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_id_producto')

    class Meta:
        managed = False
        db_table = 'detalle_venta'


class Direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    numero = models.BigIntegerField()
    calle = models.CharField(max_length=20)
    piso = models.BigIntegerField(blank=True, null=True)
    codigo_postal = models.BigIntegerField(blank=True, null=True)
    tipo_vivienda_id_tipo_vivienda = models.ForeignKey('TipoVivienda', models.DO_NOTHING, db_column='tipo_vivienda_id_tipo_vivienda')
    comuna_id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='comuna_id_comuna')

    class Meta:
        managed = False
        db_table = 'direccion'


class DireccionCli(models.Model):
    direccion_id_direccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='direccion_id_direccion')
    cliente_rut_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_rut_cliente')

    class Meta:
        managed = False
        db_table = 'direccion_cli'


class DireccionEmp(models.Model):
    direccion_id_direccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='direccion_id_direccion')
    empleado_rut_empleado = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='empleado_rut_empleado')

    class Meta:
        managed = False
        db_table = 'direccion_emp'


class Empleado(models.Model):
    rut_empleado = models.BigIntegerField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apaterno = models.CharField(max_length=50)
    amaterno = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    telefono_2 = models.BigIntegerField(blank=True, null=True)
    correo = models.CharField(max_length=50)
    tipo_empleado_id_tipo_empleado = models.ForeignKey('TipoEmpleado', models.DO_NOTHING, db_column='tipo_empleado_id_tipo_empleado')
    estado_empleado_id_estado_emp = models.ForeignKey('EstadoEmpleado', models.DO_NOTHING, db_column='estado_empleado_id_estado_emp')

    class Meta:
        managed = False
        db_table = 'empleado'


class EstadoAdmin(models.Model):
    id_estado = models.CharField(primary_key=True, max_length=1)
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado_admin'


class EstadoCli(models.Model):
    id_estado_cli = models.CharField(primary_key=True, max_length=1)
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado_cli'


class EstadoEmpleado(models.Model):
    id_estado_emp = models.CharField(primary_key=True, max_length=1)
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado_empleado'


class EstadoOrden(models.Model):
    id_estado = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado_orden'


class EstadoPedido(models.Model):
    id_estado_pedido = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado_pedido'


class EstadoVenta(models.Model):
    id_estado_venta = models.CharField(primary_key=True, max_length=1)
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado_venta'


class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    sub_total = models.BigIntegerField()
    iva = models.BigIntegerField()
    giro = models.CharField(max_length=50)
    total = models.BigIntegerField()
    estado_venta_id_estado_venta = models.ForeignKey(EstadoVenta, models.DO_NOTHING, db_column='estado_venta_id_estado_venta')

    class Meta:
        managed = False
        db_table = 'factura'


class FamiliaProducto(models.Model):
    id_fam_prod = models.FloatField(primary_key=True)
    descripcion = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'familia_producto'


class OrdenCompra(models.Model):
    proveedor_id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='proveedor_id_proveedor')
    id_orden_compra = models.AutoField(primary_key=True)
    fecha_solicitud = models.DateField()
    empleado_rut_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_rut_empleado')
    estado_orden_id_estado = models.ForeignKey(EstadoOrden, models.DO_NOTHING, db_column='estado_orden_id_estado')
    total = models.BigIntegerField()
    neto = models.BigIntegerField()
    iva = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'orden_compra'


class Pedido(models.Model):
    estado_pedido_id_estado_pedido = models.ForeignKey(EstadoPedido, models.DO_NOTHING, db_column='estado_pedido_id_estado_pedido')
    id_pedido = models.AutoField(primary_key=True)
    fecha_recepcion = models.DateField()
    fecha_pedido = models.DateField()
    descripcion = models.CharField(max_length=200)
    venta_id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='venta_id_venta', blank=True, null=True)
    direccion = models.CharField(max_length=100)
    comuna_id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='comuna_id_comuna')
    total = models.BigIntegerField()
    documento = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'pedido'


class ProdProveedor(models.Model):
    producto_id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_id_producto')
    proveedor_id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='proveedor_id_proveedor')

    class Meta:
        managed = False
        db_table = 'prod_proveedor'


class Producto(models.Model):
    tipo_producto_id_tipo_producto = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='tipo_producto_id_tipo_producto')
    id_producto = models.CharField(primary_key=True, max_length=20)
    fecha_vencimiento = models.DateField()
    familia_producto_id_fam_prod = models.ForeignKey(FamiliaProducto, models.DO_NOTHING, db_column='familia_producto_id_fam_prod')
    nombre = models.CharField(max_length=200)
    stock = models.BigIntegerField()
    stock_critico = models.BigIntegerField()
    precio = models.BigIntegerField()
    marca = models.CharField(max_length=20)
    valor_producto_compra = models.BigIntegerField()
    imagen = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    rut_proveedor = models.BigIntegerField()
    nombre_proveedor = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    telefono_2 = models.BigIntegerField(blank=True, null=True)
    correo = models.CharField(max_length=50)
    giro = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'proveedor'


class RespaldoVenta(models.Model):
    id_respaldo = models.AutoField(primary_key=True)
    nro_venta = models.BigIntegerField()
    fecha_venta = models.DateField()
    nro_boleta = models.BigIntegerField(blank=True, null=True)
    nro_factura = models.BigIntegerField(blank=True, null=True)
    nro_pedido = models.BigIntegerField(blank=True, null=True)
    total = models.BigIntegerField()
    id_producto = models.CharField(max_length=20)
    cantidad = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'respaldo_venta'


class TipoEmpleado(models.Model):
    id_tipo_empleado = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_empleado'


class TipoProducto(models.Model):
    id_tipo_producto = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'tipo_producto'


class TipoVivienda(models.Model):
    id_tipo_vivienda = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_vivienda'


class UsuarioCliente(models.Model):
    id_usuario_cliente = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    cliente_rut_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_rut_cliente')

    class Meta:
        managed = False
        db_table = 'usuario_cliente'


class UsuarioEmpleado(models.Model):
    id_usuario_empleado = models.AutoField(primary_key=True)
    empleado_rut_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_rut_empleado')
    usuario = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'usuario_empleado'


class Venta(models.Model):
    cliente_rut_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_rut_cliente', blank=True, null=True)
    pedido_id_pedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='pedido_id_pedido', blank=True, null=True)
    boleta_id_boleta = models.ForeignKey(Boleta, models.DO_NOTHING, db_column='boleta_id_boleta', blank=True, null=True)
    id_venta = models.AutoField(primary_key=True)
    fecha_venta = models.DateField()
    factura_id_factura = models.ForeignKey(Factura, models.DO_NOTHING, db_column='factura_id_factura', blank=True, null=True)
    empleado_rut_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_rut_empleado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venta'
