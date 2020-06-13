# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import cx_Oracle


class Administrador(models.Model):
    rut = models.BigIntegerField(primary_key=True)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'administrador'


class Boleta(models.Model):
    id_boleta = models.BigAutoField(primary_key=True)
    total = models.BigIntegerField()
    estado_venta_id_estado_venta = models.ForeignKey('EstadoVenta', models.DO_NOTHING, db_column='estado_venta_id_estado_venta')


    @classmethod
    def traerUltimoIdBoleta(self):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
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
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("insertar_detalle_boleta",[id_boleta,id_producto,cantidad])
        conn.commit()
        cur.close()
        conn.close()


    @classmethod
    def agregarVentaBoleta(self, rut_empleado, id_boleta, fecha_venta):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("insertar_venta_boleta",[rut_empleado, id_boleta, fecha_venta])
        conn.commit()
        cur.close()
        conn.close()
    
    @classmethod
    def traerProductosBoleta(self, id_boleta):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
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
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
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
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("eliminar_producto_boleta",[id_boleta, id_producto, cantidad, id_venta, total])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def actualizarBoleta(self, id_boleta, total, estado):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("modificar_boleta",[id_boleta,total,estado])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def anular_boleta(self, id_boleta):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("anular_boleta",[id_boleta])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def reporteBoleta(self, mes, anio):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.execute("SELECT A.ID_BOLETA , A.TOTAL, TO_CHAR(C.FECHA_VENTA, 'DD/Mon/YYYY') FECHA_VENTA, B.DESCRIPCION FROM BOLETA A JOIN ESTADO_VENTA B ON A.ESTADO_VENTA_ID_ESTADO_VENTA = B.ID_ESTADO_VENTA JOIN VENTA C ON C.BOLETA_ID_BOLETA = A.ID_BOLETA where extract(MONTH from fecha_venta) = '"+ mes +"' and extract(YEAR from fecha_venta) = '" + anio + "'")
        columns = [column[0] for column in cur.description]
        ventasBoleta = []
        for row in cur.fetchall():
            ventasBoleta.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        return ventasBoleta

    class Meta:
        managed = False
        db_table = 'boleta'


class Ciudad(models.Model):
    id_ciudad = models.BigAutoField(primary_key=True)
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
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("insertar_cliente",[rut, nombres, apaterno, amaterno, telefono, telefono2, correo, rutEmpresa, razonSocial, giro, estado])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod 
    def agregarDireccionCliente(self, id_direccion, rut):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("insertar_detalle_direccion_cli",[id_direccion, rut])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod 
    def actualizar_pass_cliente(self, rut_cliente, new_password):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("actualizar_pass_cliente",[rut_cliente, new_password])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def traerDireccionCliente(self, rut_cliente):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
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
    id_comuna = models.BigAutoField(primary_key=True)
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


class DetalleVenta(models.Model):
    venta_id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='venta_id_venta')
    producto_id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_id_producto')

    class Meta:
        managed = False
        db_table = 'detalle_venta'


class Direccion(models.Model):
    id_direccion = models.BigAutoField(primary_key=True)
    numero = models.BigIntegerField()
    calle = models.CharField(max_length=20)
    piso = models.BigIntegerField(blank=True, null=True)
    codigo_postal = models.BigIntegerField(blank=True, null=True)
    tipo_vivienda_id_tipo_vivienda = models.ForeignKey('TipoVivienda', models.DO_NOTHING, db_column='tipo_vivienda_id_tipo_vivienda')
    comuna_id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='comuna_id_comuna')

    @classmethod
    def traerUltimoIdDireccion(self):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
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
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("insertar_usuario_empleado",[rut_empleado, usuario, password ])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod 
    def agregarDireccionEmpleado(self, id_direccion, rut_empleado):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("insertar_detalle_direccion_emp",[id_direccion, rut_empleado])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod 
    def modificarDatosEmpleado(self, nombre, apellido, email, rut_empleado):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("modificar_datos_empleado",[nombre, apellido, email, rut_empleado])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod 
    def modificarUsuarioCliente(self, old_name, new_name):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("modificar_usuario_empleado",[old_name, new_name])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def traerDireccionEmpleado(self, rut_empleado):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
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
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("modificar_direccion_empleado",[id_direccion, numero_direccion, calle_direccion, piso_direccion, codigo_postal, tipo_vivienda, comuna])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod 
    def actualizar_pass_empleado(self, rut_empleado, new_password):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("actualizar_pass_empleado",[rut_empleado, new_password])
        conn.commit()
        cur.close()
        conn.close()

    def __str__(self):
        return self.nombres

    class Meta:
        managed = False
        db_table = 'empleado'


class EstadoCli(models.Model):
    id_estado_cli = models.FloatField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion

    class Meta:
        managed = False
        db_table = 'estado_cli'


class EstadoEmpleado(models.Model):
    id_estado_emp = models.FloatField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion

    class Meta:
        managed = False
        db_table = 'estado_empleado'


class EstadoOrden(models.Model):
    id_estado = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion

    class Meta:
        managed = False
        db_table = 'estado_orden'


class EstadoPedido(models.Model):
    id_estado_pedido = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion

    class Meta:
        managed = False
        db_table = 'estado_pedido'


class EstadoVenta(models.Model):
    id_estado_venta = models.FloatField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion

    class Meta:
        managed = False
        db_table = 'estado_venta'


class Factura(models.Model):
    id_factura = models.BigAutoField(primary_key=True)
    sub_total = models.BigIntegerField()
    iva = models.BigIntegerField()
    giro = models.CharField(max_length=50)
    total = models.BigIntegerField()
    estado_venta_id_estado_venta = models.ForeignKey(EstadoVenta, models.DO_NOTHING, db_column='estado_venta_id_estado_venta')

    @classmethod
    def traerUltimoIdFactura(self):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
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
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("insertar_detalle_factura",[id_factura,id_producto,cantidad])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def agregarVentaFactura(self, rut_cliente, fecha_venta, id_factura, rut_empleado):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("insertar_venta_factura",[rut_cliente,fecha_venta,id_factura,rut_empleado])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def traerClienteFactura(self, id):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
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
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
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
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("modificar_factura",[id_factura,subtotal,iva, giro, total, estado])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def idVentaFactura(self, id_factura):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
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
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("insertar_detalle_venta_factura",[id_venta, id_producto])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def eliminarProductoFactura(self, id_factura, id_producto, cantidad, id_venta, total):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("eliminar_producto_factura",[id_factura, id_producto, cantidad, id_venta, total])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def traerFactura(self, id):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
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
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("anular_factura",[id_factura])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def reporteFactura(self, mes, anio):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
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
    id_fam_prod = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion

    class Meta:
        managed = False
        db_table = 'familia_producto'


class OrdenCompra(models.Model):
    proveedor_id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='proveedor_id_proveedor')
    id_orden_compra = models.BigAutoField(primary_key=True)
    fecha_solicitud = models.DateField()
    empleado_rut_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_rut_empleado')
    estado_orden_id_estado = models.ForeignKey(EstadoOrden, models.DO_NOTHING, db_column='estado_orden_id_estado')
    total = models.BigIntegerField()
    neto = models.BigIntegerField()
    iva = models.BigIntegerField()

    @classmethod
    def traerOrdenes(self):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
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
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
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
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
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
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("insertar_detalle_orden",[id_orden_compra,id_producto,cantidad])
        conn.commit()
        cur.close()
        conn.close()
    
    @classmethod
    def modificar_orden(self, proveedor_id_proveedor,id_orden_compra, fecha_solicitud,empleado_rut_empleado, estado_orden_id_estado, total, neto, iva):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("modificar_orden",[proveedor_id_proveedor,id_orden_compra,fecha_solicitud,empleado_rut_empleado, estado_orden_id_estado, total, neto, iva])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def productosOrden(self, id_oc):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
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
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("eliminar_producto_orden",[id_orden,id_producto,cantidad, total])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def aprobarOrdenCompra(self, id_orden_compra):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("aprobar_orden_compra",[id_orden_compra])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def rechazarOrdenCompra(self, id_orden_compra):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("rechazar_orden_compra",[id_orden_compra])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def recepcionarOrdenProveedor(self, id_orden_compra):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("recepcionar_orden_proveedor",[id_orden_compra])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def rechazarOrdenProveedor(self, id_orden_compra):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("rechazar_orden_proveedor",[id_orden_compra])
        conn.commit()
        cur.close()
        conn.close()

    class Meta:
        managed = False
        db_table = 'orden_compra'


class Pedido(models.Model):
    estado_pedido_id_estado_pedido = models.ForeignKey(EstadoPedido, models.DO_NOTHING, db_column='estado_pedido_id_estado_pedido')
    id_pedido = models.BigAutoField(primary_key=True)
    fecha_recepcion = models.DateField()
    fecha_pedido = models.DateField()
    descripcion = models.CharField(max_length=200)
    venta_id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='venta_id_venta', blank=True, null=True)
    direccion = models.CharField(max_length=100)
    comuna_id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='comuna_id_comuna')

    @classmethod
    def insertar_pedido(self, estado_pedido, fecha_recepcion, fecha_pedido, detalle_pedido, direccion_pedido, comuna_pedido):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("insertar_pedido",[estado_pedido,fecha_recepcion,fecha_pedido, detalle_pedido,direccion_pedido, comuna_pedido])
        conn.commit()
        cur.close()
        conn.close()

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
    imagen = models.ImageField(null=True, blank=True)
    nombre = models.CharField(max_length=200)
    stock = models.BigIntegerField()
    stock_critico = models.BigIntegerField()
    precio = models.BigIntegerField()
    marca = models.CharField(max_length=20)
    valor_producto_compra = models.BigIntegerField()

    @classmethod
    def agregarDetalleProductoProveedor(self, id_producto, id_proveedor):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("ingresar_detalle_pv",[id_producto,id_proveedor])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def productos_proveedor(self):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.execute("select a.id_producto, a.nombre , c.nombre_proveedor, a.precio, a.valor_producto_compra, a.stock from producto a join prod_proveedor b on a.id_producto = b.producto_id_producto join proveedor c on b.proveedor_id_proveedor = c.id_proveedor")
        columns = [column[0] for column in cur.description]
        productosOrden = []
        for row in cur.fetchall():
            productosOrden.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
        print(productosOrden)
        return productosOrden

    @classmethod
    def actualizarStockProductoRecepcion(self, sku_producto, cantidad):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("actualizar_stock_recepcion",[sku_producto,cantidad])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def descontarStockFactura(self, sku_producto, cantidad):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("descontar_stock_factura",[sku_producto,cantidad])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def sumarStockFactura(self, sku_producto, cantidad):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("agregar_stock_factura",[sku_producto,cantidad])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def traerProveedorProducto(self, id_producto):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
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
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
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
    id_proveedor = models.BigAutoField(primary_key=True)
    rut_proveedor = models.BigIntegerField()
    nombre_proveedor = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    telefono_2 = models.BigIntegerField(blank=True, null=True)
    correo = models.CharField(max_length=50)
    giro = models.CharField(max_length=50)


    @classmethod
    def ordenesProveedor(self, rut_proveedor):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.execute("select a.id_orden_compra, a.fecha_solicitud, b.rut_proveedor, b.nombre_proveedor,c.descripcion estado, a.total from orden_compra a join proveedor b on a.proveedor_id_proveedor = b.id_proveedor join estado_orden c on a.estado_orden_id_estado = c.id_estado where c.descripcion = 'Enviada a Proveedor' and b.rut_proveedor =" + rut_proveedor)
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
    id_respaldo = models.BigAutoField(primary_key=True)
    fecha = models.DateField()
    mes = models.BigIntegerField()
    hora = models.DateField()

    class Meta:
        managed = False
        db_table = 'respaldo_venta'


class TipoEmpleado(models.Model):
    id_tipo_empleado = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=20)
    
    def __str__(self):
        return self.descripcion
    class Meta:
        managed = False
        db_table = 'tipo_empleado'


class TipoProducto(models.Model):
    id_tipo_producto = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion

    class Meta:
        managed = False
        db_table = 'tipo_producto'


class TipoVivienda(models.Model):
    id_tipo_vivienda = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion

    class Meta:
        managed = False
        db_table = 'tipo_vivienda'


class UsuarioCliente(models.Model):
    id_usuario_cliente = models.BigAutoField(primary_key=True)
    usuario = models.CharField(max_length=20)
    password = models.CharField(max_length=8)
    cliente_rut_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_rut_cliente')

    @classmethod
    def agregarUsuarioCliente(self, username, password, rut_cliente):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("insertar_usuario_cliente",[username,password,rut_cliente])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def traerUsuarioEmpleado(self, usuario):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
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
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
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
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("modificar_usuario_cliente",[old_name, new_name])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod 
    def modificar_datos_cliente(self, nombre, apellido,apmaterno, email, rut_cliente):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("modificar_datos_cliente",[nombre, apellido,apmaterno, email, rut_cliente])
        conn.commit()
        cur.close()
        conn.close()

    class Meta:
        managed = False
        db_table = 'usuario_cliente'


class UsuarioEmpleado(models.Model):
    id_usuario_empleado = models.BigAutoField(primary_key=True)
    empleado_rut_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_rut_empleado')
    usuario = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'usuario_empleado'


class Venta(models.Model):
    cliente_rut_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_rut_cliente', blank=True, null=True)
    pedido_id_pedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='pedido_id_pedido', blank=True, null=True)
    boleta_id_boleta = models.ForeignKey(Boleta, models.DO_NOTHING, db_column='boleta_id_boleta', blank=True, null=True)
    id_venta = models.BigAutoField(primary_key=True)
    fecha_venta = models.DateField()
    factura_id_factura = models.ForeignKey(Factura, models.DO_NOTHING, db_column='factura_id_factura', blank=True, null=True)
    empleado_rut_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_rut_empleado', blank=True, null=True)

    @classmethod
    def traerUltimoIdVenta(self):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
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
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("insertar_detalle_venta_factura",[venta_id, id_producto])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def traerVenta(self, id):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
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
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
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
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.callproc("insertar_detalle_venta",[id_venta,id_producto])
        conn.commit()
        cur.close()
        conn.close()

    @classmethod
    def reporteVentasTotal(self, mes, anio):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
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
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl') # if needed, place an 'r' before any parameter in order to address special characters such as ''.
        conn = cx_Oracle.connect(user=r'c##fermme0', password='oracle', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as ''. For example, if your user name contains '', you'll need to place 'r' before the user name: user=r'User Name'
        cur = conn.cursor()
        cur.execute("SELECT COUNT(A.ID_VENTA) AS VENTAS FROM VENTA A JOIN DETALLE_VENTA B ON A.ID_VENTA = B.VENTA_ID_VENTA JOIN PRODUCTO C ON B.PRODUCTO_ID_PRODUCTO = C.ID_PRODUCTO WHERE EXTRACT (MONTH FROM A.FECHA_VENTA) = '"+ mes +"' AND EXTRACT (YEAR FROM A.FECHA_VENTA) = '"+ anio +"'")
        res=cur.fetchone()
        column = [row[0] for row in cur.description]
        obj = {column[0] :res[0]}
        cur.close()
        conn.close()
        return obj

    class Meta:
        managed = False
        db_table = 'venta'






