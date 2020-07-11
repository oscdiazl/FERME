# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import cx_Oracle


def conectarbd():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
    conn = cx_Oracle.connect(user=r'c##testfermefinal2', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
    return conn



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


    @classmethod
    def traerUltimoIdBoleta(self):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute('select max(id_boleta) id_max from boleta')
        columns = [column[0] for column in cur.description]
        ultimoId = []
        for row in cur.fetchall():
            ultimoId.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        return ultimoId[0]

    @classmethod
    def agregarDetalleBoleta(self, id_boleta, id_producto, cantidad):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_insertar_detalle_Boleta",[id_boleta,id_producto,cantidad])
        conn.commit()
        cur.close()
        conn.close()


    @classmethod
    def agregarVentaBoleta(self, rut_cliente, rut_empleado, id_boleta, fecha_venta):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_insertar_venta_boleta",[rut_cliente,rut_empleado, id_boleta, fecha_venta])
        conn.commit()
        cur.close()
        conn.close()


    @classmethod
    def actualizar_venta_boleta(self, rut_cliente,rut_empleado, id_boleta, fecha_venta):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_actualizar_venta_boleta",[rut_cliente,rut_empleado, id_boleta, fecha_venta])
        conn.commit()
        cur.close()
        conn.close()
    
    @classmethod
    def traerProductosBoleta(self, id_boleta):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("select a.boleta_id_boleta, b.id_producto, b.nombre, a.cantidad, b.precio, (a.cantidad * b.precio ) total   from detalle_boleta a join producto b on a.producto_id_producto = b.id_producto where a.boleta_id_boleta =" + id_boleta)
        columns = [column[0] for column in cur.description]
        productosBoleta = []
        for row in cur.fetchall():
            productosBoleta.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        return productosBoleta

    @classmethod
    def idVentaBoleta(self, id_boleta):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute('select b.id_venta from boleta a join venta b on a.id_boleta = b.boleta_id_boleta where a.id_boleta =' + id_boleta)
        columns = [column[0] for column in cur.description]
        idVenta = []
        for row in cur.fetchall():
            idVenta.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        return idVenta[0]


    @classmethod
    def eliminarProductoBoleta(self, id_boleta, id_producto, cantidad, id_venta, total):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_eliminar_producto_boleta",[id_boleta, id_producto, cantidad, id_venta, total])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def actualizarBoleta(self, id_boleta, total, estado):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_modificar_boleta",[id_boleta,total,estado])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def anular_boleta(self, id_boleta):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_anular_boleta",[id_boleta])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def reporteBoleta(self, mes, anio):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("SELECT A.ID_BOLETA , A.TOTAL, TO_CHAR(C.FECHA_VENTA, 'DD/Mon/YYYY') FECHA_VENTA, B.DESCRIPCION FROM BOLETA A JOIN ESTADO_VENTA B ON A.ESTADO_VENTA_ID_ESTADO_VENTA = B.ID_ESTADO_VENTA JOIN VENTA C ON C.BOLETA_ID_BOLETA = A.ID_BOLETA where extract(MONTH from fecha_venta) = '"+ mes +"' and extract(YEAR from fecha_venta) = '" + anio + "'")
        columns = [column[0] for column in cur.description]
        ventasBoleta = []
        for row in cur.fetchall():
            ventasBoleta.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        return ventasBoleta

    @classmethod
    def traerClienteBoleta(self, id):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("select  b.cliente_rut_cliente rut_cliente from boleta a join venta b  on a.id_boleta = b.boleta_id_boleta where a.id_boleta =" + id)
        res=cur.fetchone()
        column = [row[0] for row in cur.description]
        obj = {column[0] :res[0]}
        cur.close()
        conn.close()
        return obj

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

    @classmethod
    def agregarCliente(self, rut, nombres, apaterno, amaterno, telefono, telefono2, correo, rutEmpresa, razonSocial, giro, estado):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_insertar_cliente",[rut, nombres, apaterno, amaterno, telefono, telefono2, correo, rutEmpresa, razonSocial, giro, estado])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod 
    def agregarDireccionCliente(self, id_direccion, rut):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_insertar_detalle_direccion_cli",[id_direccion, rut])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod 
    def actualizar_pass_cliente(self, rut_cliente, new_password):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_actualizar_pass_cliente",[rut_cliente, new_password])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def traerDireccionCliente(self, rut_cliente):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("select * from direccion_cli a join direccion b on a.direccion_id_direccion = b.id_direccion where a.cliente_rut_cliente =" + rut_cliente)
        res=cur.fetchone()
        column = [row[0] for row in cur.description]
        obj = {column[0] :res[0], column[1]:res[1], column[2]:res[2],column[3]:res[3], column[4]:res[4], column[5]:res[5],column[6]:res[6],column[7]:res[7],column[8]:res[8]}
        cur.close()
        conn.close()
        return obj

    class Meta:
        managed = False
        db_table = 'cliente'


class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    ciudad_id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='ciudad_id_ciudad')

    def __str__(self):
        return self.descripcion


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

    @classmethod
    def traerUltimoIdDireccion(self):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute('select max(id_direccion) id_max from direccion')
        columns = [column[0] for column in cur.description]
        ultimoId = []
        for row in cur.fetchall():
            ultimoId.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        return ultimoId[0]

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

    @classmethod 
    def agregarUsuarioEmpleado(self, rut_empleado, usuario, password):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_insertar_usuario_empleado",[rut_empleado, usuario, password ])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod 
    def agregarDireccionEmpleado(self, id_direccion, rut_empleado):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_insertar_detalle_direccion_emp",[id_direccion, rut_empleado])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod 
    def modificarDatosEmpleado(self, nombre, apellido, email, rut_empleado):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_modificar_datos_empleado",[nombre, apellido, email, rut_empleado])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod 
    def modificarUsuarioCliente(self, old_name, new_name):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_modificar_usuario_empleado",[old_name, new_name])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def traerDireccionEmpleado(self, rut_empleado):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("select * from direccion_emp a join direccion b on a.direccion_id_direccion = b.id_direccion where a.empleado_rut_empleado = " + rut_empleado)
        res=cur.fetchone()
        column = [row[0] for row in cur.description]
        obj = {column[0] :res[0], column[1]:res[1], column[2]:res[2],column[3]:res[3], column[4]:res[4], column[5]:res[5],column[6]:res[6],column[7]:res[7],column[8]:res[8]}
        cur.close()
        conn.close()
        return obj

    @classmethod 
    def modificar_direccion_empleado(self, id_direccion, numero_direccion, calle_direccion, piso_direccion, codigo_postal, tipo_vivienda, comuna):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_modificar_direccion_empleado",[id_direccion, numero_direccion, calle_direccion, piso_direccion, codigo_postal, tipo_vivienda, comuna])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod 
    def actualizar_pass_empleado(self, rut_empleado, new_password):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_actualizar_pass_empleado",[rut_empleado, new_password])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod 
    def insertar_grupo_vendedor(self, nombre_usuario):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_insertar_grupo_vendedor",[nombre_usuario])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod 
    def insertar_grupo_empleado_tienda(self, nombre_usuario):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_insertar_grupo_empleado_tienda",[nombre_usuario])
        conn.commit()
        cur.close()
        conn.close()

    def __str__(self):
        return self.nombres

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

    def __str__(self):
        return self.descripcion

    class Meta:
        managed = False
        db_table = 'estado_cli'


class EstadoEmpleado(models.Model):
    id_estado_emp = models.CharField(primary_key=True, max_length=1)
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion

    class Meta:
        managed = False
        db_table = 'estado_empleado'


class EstadoOrden(models.Model):
    id_estado = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion

    class Meta:
        managed = False
        db_table = 'estado_orden'


class EstadoPedido(models.Model):
    id_estado_pedido = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion

    class Meta:
        managed = False
        db_table = 'estado_pedido'


class EstadoVenta(models.Model):
    id_estado_venta = models.CharField(primary_key=True, max_length=1)
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion

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

    @classmethod
    def traerUltimoIdFactura(self):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute('select max(id_factura) id_max from factura')
        columns = [column[0] for column in cur.description]
        ultimoId = []
        for row in cur.fetchall():
            ultimoId.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        return ultimoId[0]

    @classmethod
    def agregarDetalleFactura(self, id_factura, id_producto, cantidad):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_insertar_detalle_factura",[id_factura,id_producto,cantidad])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def agregarVentaFactura(self, rut_cliente, fecha_venta, id_factura, rut_empleado):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_insertar_venta_det_factura",[rut_cliente,fecha_venta,id_factura,rut_empleado])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def traerClienteFactura(self, id):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("select  b.cliente_rut_cliente rut_cliente from factura a join venta b  on a.id_factura = b.factura_id_factura where a.id_factura =" + id)
        res=cur.fetchone()
        column = [row[0] for row in cur.description]
        obj = {column[0] :res[0]}
        cur.close()
        conn.close()
        return obj

    @classmethod
    def traerProductosFactura(self, id_factura):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("select a.factura_id_factura, b.id_producto, b.nombre, a.cantidad, b.precio, (a.cantidad * b.precio ) total  from detalle_factura a join producto b on a.producto_id_producto = b.id_producto where a.factura_id_factura =" + id_factura)
        columns = [column[0] for column in cur.description]
        productosFactura = []
        for row in cur.fetchall():
            productosFactura.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        return productosFactura

    @classmethod
    def actualizarFactura(self, id_factura, subtotal, iva, giro, total, estado):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_modificar_factura",[id_factura,subtotal,iva, giro, total, estado])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def actualizar_venta_factura(self, id_factura,rut_cliente, rut_empleado):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_actualizar_venta_factura",[id_factura,rut_cliente,rut_empleado])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def idVentaFactura(self, id_factura):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute('select b.id_venta from factura a join venta b on a.id_factura = b.factura_id_factura where a.id_factura =' + id_factura)
        columns = [column[0] for column in cur.description]
        idVenta = []
        for row in cur.fetchall():
            idVenta.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        return idVenta[0]

    @classmethod
    def agregarDetalleVenta(self, id_venta, id_producto):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_insertar_detalle_venta_factura",[id_venta, id_producto])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def eliminarProductoFactura(self, id_factura, id_producto, cantidad, id_venta, total):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_eliminar_producto_factura",[id_factura, id_producto, cantidad, id_venta, total])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def traerFactura(self, id):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("select * from factura where id_factura =" + id)
        res=cur.fetchone()
        column = [row[0] for row in cur.description]
        obj = {column[0] :res[0], column[1]:res[1], column[2]:res[2],column[3]:res[3], column[4]:res[4], column[5]:res[5]}
        cur.close()
        conn.close()
        return obj

    @classmethod
    def anular_factura(self, id_factura):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_anular_factura",[id_factura])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def reporteFactura(self, mes, anio):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("SELECT A.ID_FACTURA, A.TOTAL, TO_CHAR(C.FECHA_VENTA, 'DD/Mon/YYYY') FECHA_VENTA, B.DESCRIPCION FROM FACTURA A JOIN ESTADO_VENTA B ON A.ESTADO_VENTA_ID_ESTADO_VENTA = B.ID_ESTADO_VENTA JOIN VENTA C ON C.FACTURA_ID_FACTURA = A.ID_FACTURA WHERE EXTRACT(MONTH FROM FECHA_VENTA) = '"+ mes +"' AND EXTRACT(YEAR FROM FECHA_VENTA) = '" + anio +"'")
        columns = [column[0] for column in cur.description]
        ventasFactura = []
        for row in cur.fetchall():
            ventasFactura.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        return ventasFactura

    class Meta:
        managed = False
        db_table = 'factura'


class FamiliaProducto(models.Model):
    id_fam_prod = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion

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

    @classmethod
    def traerOrdenes(self):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("select a.id_orden_compra, to_char(a.fecha_solicitud, 'DD-Mon-YYYY') FECHA_SOLICITUD, b.nombres ||' '|| b.apaterno nombre,c.descripcion, a.total from orden_compra a join empleado b on a.empleado_rut_empleado = b.rut_empleado join estado_orden c on a.estado_orden_id_estado = c.id_estado")
        columns = [column[0] for column in cur.description]
        ordenesDeCompra = []
        for row in cur.fetchall():
            ordenesDeCompra.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        return ordenesDeCompra



    @classmethod
    def traerOrden(self, id):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("select PROVEEDOR_ID_PROVEEDOR, ID_ORDEN_COMPRA, to_char(fecha_solicitud, 'DD-Mon-YYYY') FECHA_SOLICITUD, EMPLEADO_RUT_EMPLEADO, ESTADO_ORDEN_ID_ESTADO, TOTAL, NETO, IVA from orden_compra where id_orden_compra=" + id)
        res=cur.fetchone()
        column = [row[0] for row in cur.description]
        obj = {column[0] :res[0], column[1]:res[1], column[2]:res[2],column[3]:res[3], column[4]:res[4], column[5]:res[5],column[6]:res[6],column[7]:res[7]}
        cur.close()
        conn.close()
        return obj

    @classmethod
    def traerUltimoId(self):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute('select max(id_orden_compra) id_max from orden_compra')
        columns = [column[0] for column in cur.description]
        ultimoId = []
        for row in cur.fetchall():
            ultimoId.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        return ultimoId[0]

    @classmethod
    def agregarDetalleOrden(self, id_orden_compra, id_producto, cantidad):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_insertar_detalle_orden",[id_orden_compra,id_producto,cantidad])
        conn.commit()
        cur.close()
        conn.close()
    
    @classmethod
    def modificar_orden(self, proveedor_id_proveedor,id_orden_compra, fecha_solicitud,empleado_rut_empleado, estado_orden_id_estado, total, neto, iva):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_modificar_orden",[proveedor_id_proveedor,id_orden_compra,fecha_solicitud,empleado_rut_empleado, estado_orden_id_estado, total, neto, iva])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def productosOrden(self, id_oc):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("select a.orden_compra_id_orden_compra ID_ORDEN, a.producto_id_producto SKU_PRODUCTO, a.cantidad, b.valor_producto_compra, (a.cantidad * b.valor_producto_compra) total from detalle_oc a join producto b  on a.producto_id_producto = b.id_producto where a.orden_compra_id_orden_compra =" + id_oc)
        columns = [column[0] for column in cur.description]
        productosOrden = []
        for row in cur.fetchall():
            productosOrden.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        return productosOrden

    @classmethod
    def eliminarProductoOrden(self, id_orden, id_producto, cantidad, total):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_eliminar_producto_orden",[id_orden,id_producto,cantidad, total])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def aprobarOrdenCompra(self, id_orden_compra):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_aprobar_orden_compra",[id_orden_compra])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def rechazarOrdenCompra(self, id_orden_compra):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_rechazar_orden_compra",[id_orden_compra])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def recepcionarOrdenProveedor(self, id_orden_compra):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_recepcionar_orden_proveedor",[id_orden_compra])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def anular_oc(self, id_orden_compra):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_anular_orden_compra",[id_orden_compra])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def rechazarOrdenProveedor(self, id_orden_compra):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_rechazar_orden_proveedor",[id_orden_compra])
        conn.commit()
        cur.close()
        conn.close()

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

    @classmethod
    def traer_listado_pedidos(self):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("select a.ID_PEDIDO, a.DOCUMENTO, initcap(to_char(a.FECHA_PEDIDO, 'DD-MON-YYYY')) FECHA_PEDIDO , a.TOTAL, b.BOLETA_ID_BOLETA, b.FACTURA_ID_FACTURA, a.RUT_TITULAR from pedido a full join venta b on a.id_pedido = b.pedido_id_pedido")
        columns = [column[0] for column in cur.description]
        pedidos = []
        for row in cur.fetchall():
            pedidos.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        return pedidos

    @classmethod
    def traer_pedidos_perfil(self, rut_cliente):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute(" select pedido_id_pedido from venta where pedido_id_pedido is not null and cliente_rut_cliente =" + rut_cliente)
        columns = [column[0] for column in cur.description]
        pedidos = []
        for row in cur.fetchall():
            pedidos.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        return pedidos


    @classmethod
    def insertar_pedido(self, estado_pedido, fecha_recepcion, fecha_pedido, detalle_pedido, direccion_pedido, comuna_pedido, total_pedido, documento, rut_cliente):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_insertar_pedido",[estado_pedido,fecha_recepcion,fecha_pedido, detalle_pedido,direccion_pedido, comuna_pedido, total_pedido, documento, rut_cliente])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def insertar_producto_pedido(self, id_pedido, producto_id, cantidad):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_insertar_producto_pedido",[producto_id,id_pedido, cantidad])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def traerUltimoPedido(self):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute('select max(id_pedido) id_max from pedido')
        columns = [column[0] for column in cur.description]
        ultimoId = []
        for row in cur.fetchall():
            ultimoId.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        return ultimoId[0]

    @classmethod
    def actualizar_pedido_cliente(self, id_pedido, total):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_actualizar_pedido_cliente",[id_pedido,total])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def insertar_venta_pedido(self, id_pedido, fecha_venta, rut_cliente):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_insertar_venta_pedido",[id_pedido,fecha_venta, rut_cliente])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def insertar_boleta_pedido(self, total, estado_venta):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_insertar_boleta_pedido",[total,estado_venta])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def insertar_factura_pedido(self, subtotal, iva, giro, total, estado_venta):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_insertar_factura_pedido",[subtotal,iva, giro, total, estado_venta])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def actualizar_venta_boleta(self, id_pedido, id_boleta):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_actualizar_venta_boleta",[id_pedido,id_boleta])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def actualizar_venta_boleta_pedido(self, id_pedido, id_boleta, id_venta):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_actualizar_venta_boleta_pedido",[id_pedido,id_boleta,id_venta])
        conn.commit()
        cur.close()
        conn.close()


    @classmethod
    def agregar_venta_pedido(self, id_pedido, id_venta):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_agregar_venta_pedido",[id_pedido,id_venta])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def actualizar_venta_factura_pedido(self, id_pedido, id_boleta):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_actualizar_venta_factura_pedido",[id_pedido,id_boleta])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def actualizar_estado_pedido(self, id_pedido, estado_pedido):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_actualizar_estado_pedido",[id_pedido,estado_pedido])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def traerPedido(self, id_pedido):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("select * from pedido where id_pedido =" + id_pedido)
        res=cur.fetchone()
        column = [row[0] for row in cur.description]
        obj = {column[0] :res[0], column[1]:res[1], column[2]:res[2],column[3]:res[3], column[4]:res[4], column[5]:res[5],column[6]:res[6],column[7]:res[7],column[8]:res[8],column[9]:res[9]}
        cur.close()
        conn.close()
        return obj

    @classmethod
    def traerProductosPedido(self, id_pedido):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("select c.id_producto, c.nombre, (b.cantidad * c.precio) precio, b.CANTIDAD from pedido a join detalle_pedido b on a.id_pedido = b.pedido_id_pedido join producto c on c.id_producto = b.producto_id_producto where a.id_pedido = " + id_pedido)
        columns = [column[0] for column in cur.description]
        productosPedido = []
        for row in cur.fetchall():
            productosPedido.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        return productosPedido

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
    imagen = models.ImageField(null=True, blank=True)


    @classmethod
    def agregarDetalleProductoProveedor(self, id_producto, id_proveedor):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_ingresar_detalle_pv",[id_producto,id_proveedor])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def productos_proveedor(self):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("select a.id_producto, a.nombre , c.nombre_proveedor, a.precio, a.valor_producto_compra, a.stock from producto a join prod_proveedor b on a.id_producto = b.producto_id_producto join proveedor c on b.proveedor_id_proveedor = c.id_proveedor")
        columns = [column[0] for column in cur.description]
        productosOrden = []
        for row in cur.fetchall():
            productosOrden.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        return productosOrden

    @classmethod
    def actualizarStockProductoRecepcion(self, sku_producto, cantidad):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_actualizar_stock_recepcion",[sku_producto,cantidad])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def descontarStockFactura(self, sku_producto, cantidad):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_descontar_stock_factura",[sku_producto,cantidad])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def sumarStockFactura(self, sku_producto, cantidad):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_agregar_stock_factura",[sku_producto,cantidad])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def traerProveedorProducto(self, id_producto):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("select * from prod_proveedor where producto_id_producto =" + "'"+id_producto+"'")
        res=cur.fetchone()
        column = [row[0] for row in cur.description]
        obj = {column[0] :res[0], column[1]:res[1]}
        cur.close()
        conn.close()
        return obj

    @classmethod
    def reporteProducto(self, mes, anio):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(B.PRODUCTO_ID_PRODUCTO) AS VENDIDO, C.ID_PRODUCTO, C.NOMBRE FROM VENTA A JOIN DETALLE_VENTA B ON A.ID_VENTA = B.VENTA_ID_VENTA JOIN PRODUCTO C ON B.PRODUCTO_ID_PRODUCTO = C.ID_PRODUCTO WHERE EXTRACT (MONTH FROM A.FECHA_VENTA) = '" + mes + "' AND EXTRACT (YEAR FROM A.FECHA_VENTA) = '" + anio + "' GROUP BY C.ID_PRODUCTO, C.NOMBRE")
        columns = [column[0] for column in cur.description]
        reporteProducto = []
        for row in cur.fetchall():
            reporteProducto.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        return reporteProducto

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

    @classmethod
    def ordenesProveedor(self, rut_proveedor):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("select a.id_orden_compra, a.fecha_solicitud, b.rut_proveedor, b.nombre_proveedor,c.descripcion estado, a.total from orden_compra a join proveedor b on a.proveedor_id_proveedor = b.id_proveedor join estado_orden c on a.estado_orden_id_estado = c.id_estado where c.descripcion = 'Enviada a proveedor' and b.rut_proveedor =" + rut_proveedor)
        columns = [column[0] for column in cur.description]
        productosOrden = []
        for row in cur.fetchall():
            productosOrden.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        return productosOrden

    def __str__(self):
        return self.nombre_proveedor

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

    def __str__(self):
        return self.descripcion
    class Meta:
        managed = False
        db_table = 'tipo_empleado'


class TipoProducto(models.Model):
    id_tipo_producto = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion

    class Meta:
        managed = False
        db_table = 'tipo_producto'


class TipoVivienda(models.Model):
    id_tipo_vivienda = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion

    class Meta:
        managed = False
        db_table = 'tipo_vivienda'


class UsuarioCliente(models.Model):
    id_usuario_cliente = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    cliente_rut_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_rut_cliente')

    @classmethod
    def agregarUsuarioCliente(self, username, password, rut_cliente):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_insertar_usuario_cliente",[username,password,rut_cliente])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def traerUsuarioEmpleado(self, usuario):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("select * from usuario_empleado a join empleado b  on b.rut_empleado = a.empleado_rut_empleado where a.usuario =" + "'"+usuario+"'")
        res=cur.fetchone()
        column = [row[0] for row in cur.description]
        obj = {column[0] :res[0], column[1]:res[1], column[2]:res[2],column[3]:res[3], column[4]:res[4], column[5]:res[5],column[6]:res[6],column[7]:res[7],column[8]:res[8],column[9]:res[9],column[10]:res[10],column[11]:res[11],column[12]:res[12]}
        cur.close()
        conn.close()
        return obj

    @classmethod
    def traerUsuarioCliente(self, usuario):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("select * from usuario_cliente a join cliente b on a.cliente_rut_cliente = b.rut_cliente where a.usuario =" + "'"+usuario+"'")
        res=cur.fetchone()
        column = [row[0] for row in cur.description]
        obj = {column[0] :res[0], column[1]:res[1], column[2]:res[2],column[3]:res[3], column[4]:res[4], column[5]:res[5],column[6]:res[6],column[7]:res[7],column[8]:res[8],column[9]:res[9],column[10]:res[10],column[11]:res[11],column[12]:res[12],column[13]:res[13],column[14]:res[14]}
        cur.close()
        conn.close()
        return obj

    @classmethod 
    def modificar_usuario_cliente(self, old_name, new_name):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_modificar_usuario_cliente",[old_name, new_name])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod 
    def modificar_datos_cliente(self, nombre, apellido,apmaterno, email, rut_cliente):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_modificar_datos_cliente",[nombre, apellido,apmaterno, email, rut_cliente])
        conn.commit()
        cur.close()
        conn.close()

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

    @classmethod
    def traerUltimoIdVenta(self):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute('select max(id_venta) id_max from venta')
        columns = [column[0] for column in cur.description]
        ultimoId = []
        for row in cur.fetchall():
            ultimoId.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        return ultimoId[0]

    @classmethod
    def agregarDetalleVentaFactura(self, venta_id, id_producto):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_insertar_detalle_venta_factura",[venta_id, id_producto])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def traerVenta(self, id):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("select * from venta where factura_id_factura =" + id)
        res=cur.fetchone()
        column = [row[0] for row in cur.description]
        obj = {column[0] :res[0], column[1]:res[1], column[2]:res[2],column[3]:res[3], column[4]:res[4], column[5]:res[5],column[6]:res[6]}
        cur.close()
        conn.close()
        return obj

    @classmethod
    def traerVentaBoleta(self, id):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("select * from venta where boleta_id_boleta =" + id)
        res=cur.fetchone()
        column = [row[0] for row in cur.description]
        obj = {column[0] :res[0], column[1]:res[1], column[2]:res[2],column[3]:res[3], column[4]:res[4], column[5]:res[5],column[6]:res[6]}
        cur.close()
        conn.close()
        return obj

    @classmethod
    def agregarDetalleVenta(self, id_venta, id_producto):
        conn = conectarbd()
        cur = conn.cursor()
        cur.callproc("sp_insertar_detalle_venta",[id_venta,id_producto])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def reporteVentasTotal(self, mes, anio):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("SELECT SUM(TOTAL) AS TOTAL FROM(SELECT B.TOTAL FROM VENTA A JOIN BOLETA B ON A.BOLETA_ID_BOLETA = B.ID_BOLETA WHERE EXTRACT (MONTH FROM A.FECHA_VENTA) = '" + mes + "' AND EXTRACT (YEAR FROM A.FECHA_VENTA) = '"+ anio +"' UNION ALL SELECT B.TOTAL FROM VENTA A JOIN FACTURA B ON A.FACTURA_ID_FACTURA = B.ID_FACTURA WHERE EXTRACT (MONTH FROM A.FECHA_VENTA) = '" + mes + "' AND EXTRACT (YEAR FROM A.FECHA_VENTA) = '"+ anio +"')")
        res=cur.fetchone()
        column = [row[0] for row in cur.description]
        obj = {column[0] :res[0]}
        cur.close()
        conn.close()
        return obj

    @classmethod
    def reporteVenta(self, mes, anio):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(distinct(A.ID_VENTA)) AS VENTAS FROM VENTA A JOIN DETALLE_VENTA B ON A.ID_VENTA = B.VENTA_ID_VENTA JOIN PRODUCTO C ON B.PRODUCTO_ID_PRODUCTO = C.ID_PRODUCTO WHERE EXTRACT (MONTH FROM A.FECHA_VENTA) = '"+ mes +"' AND EXTRACT (YEAR FROM A.FECHA_VENTA) = '"+ anio +"'")
        res=cur.fetchone()
        column = [row[0] for row in cur.description]
        obj = {column[0] :res[0]}
        cur.close()
        conn.close()
        return obj

    @classmethod
    def reporte_venta_anual(self):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("select count(*) as cantidad, CASE when to_char(fecha_venta,'MM') = 01 then 'Enero' when to_char(fecha_venta,'MM') = 02 then 'Febrero' when to_char(fecha_venta,'MM') = 03 then 'Marzo' when to_char(fecha_venta,'MM') = 04 then 'Abril' when to_char(fecha_venta,'MM') = 05 then 'Mayo' when to_char(fecha_venta,'MM') = 06 then 'Junio' when to_char(fecha_venta,'MM') = 07 then 'Julio' when to_char(fecha_venta,'MM') = 08 then 'Agosto' when to_char(fecha_venta,'MM') = 09 then 'Septiembre' when to_char(fecha_venta,'MM') = 10 then 'Octubre' when to_char(fecha_venta,'MM') = 11 then 'Noviembre' when to_char(fecha_venta,'MM') = 12 then 'Diciembre' end as mes, sum(nvl(b.total,0) + nvl(c.total,0)) as total, to_char(fecha_venta,'MM') as fecha from venta a  full join boleta b on a.boleta_id_boleta = b.id_boleta full join factura c on a.factura_id_factura = c.id_factura  where to_char(fecha_venta,'yyyy') = to_char(sysdate,'yyyy') group by to_char(fecha_venta,'MM') order by fecha asc")
        columns = [column[0] for column in cur.description]
        detalle_venta_anual = []
        for row in cur.fetchall():
            detalle_venta_anual.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        return detalle_venta_anual

    @classmethod
    def top_10_productos(self):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(B.PRODUCTO_ID_PRODUCTO) AS VENDIDO, C.id_producto, C.NOMBRE  FROM VENTA A JOIN DETALLE_VENTA B ON A.ID_VENTA = B.VENTA_ID_VENTA JOIN PRODUCTO C ON B.PRODUCTO_ID_PRODUCTO = C.ID_PRODUCTO where to_char(a.fecha_venta,'MM') = to_char(sysdate,'MM') and rownum <=5 GROUP BY C.ID_PRODUCTO, C.NOMBRE order by vendido desc")
        columns = [column[0] for column in cur.description]
        top_10_productos = []
        for row in cur.fetchall():
            top_10_productos.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        return top_10_productos

    @classmethod
    def ventas_anuales_online(self):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("select count(*) as cantidad, CASE when to_char(fecha_venta,'MM') = 01 then 'Enero' when to_char(fecha_venta,'MM') = 02 then 'Febrero' when to_char(fecha_venta,'MM') = 03 then 'Marzo' when to_char(fecha_venta,'MM') = 04 then 'Abril' when to_char(fecha_venta,'MM') = 05 then 'Mayo' when to_char(fecha_venta,'MM') = 06 then 'Junio' when to_char(fecha_venta,'MM') = 07 then 'Julio' when to_char(fecha_venta,'MM') = 08 then 'Agosto' when to_char(fecha_venta,'MM') = 09 then 'Septiembre' when to_char(fecha_venta,'MM') = 10 then 'Octubre' when to_char(fecha_venta,'MM') = 11 then 'Noviembre' when to_char(fecha_venta,'MM') = 12 then 'Diciembre' end as mes, to_char(fecha_venta,'MM') as fecha from venta  where to_char(fecha_venta,'yyyy') = to_char(sysdate,'yyyy') and pedido_id_pedido is not null group by to_char(fecha_venta,'MM') order by fecha asc")
        columns = [column[0] for column in cur.description]
        ventas_anuales_online = []
        for row in cur.fetchall():
            ventas_anuales_online.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        return ventas_anuales_online

    @classmethod
    def ventas_anuales_locales(self):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("select count(*) as cantidad, CASE when to_char(fecha_venta,'MM') = 01 then 'Enero' when to_char(fecha_venta,'MM') = 02 then 'Febrero' when to_char(fecha_venta,'MM') = 03 then 'Marzo' when to_char(fecha_venta,'MM') = 04 then 'Abril' when to_char(fecha_venta,'MM') = 05 then 'Mayo' when to_char(fecha_venta,'MM') = 06 then 'Junio' when to_char(fecha_venta,'MM') = 07 then 'Julio' when to_char(fecha_venta,'MM') = 08 then 'Agosto' when to_char(fecha_venta,'MM') = 09 then 'Septiembre' when to_char(fecha_venta,'MM') = 10 then 'Octubre' when to_char(fecha_venta,'MM') = 11 then 'Noviembre' when to_char(fecha_venta,'MM') = 12 then 'Diciembre' end as mes, to_char(fecha_venta,'MM') as fecha from venta  where to_char(fecha_venta,'yyyy') = to_char(sysdate,'yyyy') and pedido_id_pedido is null group by to_char(fecha_venta,'MM') order by fecha asc")
        columns = [column[0] for column in cur.description]
        ventas_anuales_online = []
        for row in cur.fetchall():
            ventas_anuales_online.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        return ventas_anuales_online

    @classmethod
    def oc_anuales(self):
        conn = conectarbd()
        cur = conn.cursor()
        cur.execute("select count(*) as cantidad, CASE when to_char(fecha_solicitud,'MM') = 01 then 'Enero' when to_char(fecha_solicitud,'MM') = 02 then 'Febrero' when to_char(fecha_solicitud,'MM') = 03 then 'Marzo' when to_char(fecha_solicitud,'MM') = 04 then 'Abril' when to_char(fecha_solicitud,'MM') = 05 then 'Mayo' when to_char(fecha_solicitud,'MM') = 06 then 'Junio' when to_char(fecha_solicitud,'MM') = 07 then 'Julio' when to_char(fecha_solicitud,'MM') = 08 then 'Agosto' when to_char(fecha_solicitud,'MM') = 09 then 'Septiembre' when to_char(fecha_solicitud,'MM') = 10 then 'Octubre' when to_char(fecha_solicitud,'MM') = 11 then 'Noviembre' when to_char(fecha_solicitud,'MM') = 12 then 'Diciembre' end as mes, to_char(fecha_solicitud,'MM') as mes_compra from orden_compra where to_char(fecha_solicitud,'yyyy') = to_char(sysdate,'yyyy') group by to_char(fecha_solicitud,'MM') order by mes_compra asc")
        columns = [column[0] for column in cur.description]
        ventas_anuales_online = []
        for row in cur.fetchall():
            ventas_anuales_online.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        return ventas_anuales_online

    

    class Meta:
        managed = False
        db_table = 'venta'






