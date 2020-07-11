# Generated by Django 3.0.5 on 2020-06-26 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('rut', models.BigIntegerField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=20)),
                ('apaterno', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'administrador',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id_boleta', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.BigIntegerField()),
            ],
            options={
                'db_table': 'boleta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id_ciudad', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'ciudad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut_cliente', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apaterno', models.CharField(max_length=50)),
                ('amaterno', models.CharField(max_length=50)),
                ('telefono', models.BigIntegerField()),
                ('telefono_2', models.BigIntegerField(blank=True, null=True)),
                ('correo', models.CharField(max_length=50)),
                ('rut_empresa', models.BigIntegerField(blank=True, null=True)),
                ('razon_social', models.CharField(blank=True, max_length=50, null=True)),
                ('giro', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'comuna',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleBoleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.BigIntegerField()),
            ],
            options={
                'db_table': 'detalle_boleta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.BigIntegerField()),
            ],
            options={
                'db_table': 'detalle_factura',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleOc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.BigIntegerField()),
            ],
            options={
                'db_table': 'detalle_oc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'detalle_pedido',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'detalle_venta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id_direccion', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.BigIntegerField()),
                ('calle', models.CharField(max_length=20)),
                ('piso', models.BigIntegerField(blank=True, null=True)),
                ('codigo_postal', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'direccion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DireccionCli',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'direccion_cli',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DireccionEmp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'direccion_emp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('rut_empleado', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apaterno', models.CharField(max_length=50)),
                ('amaterno', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('telefono_2', models.BigIntegerField(blank=True, null=True)),
                ('correo', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoAdmin',
            fields=[
                ('id_estado', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'estado_admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoCli',
            fields=[
                ('id_estado_cli', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'estado_cli',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoEmpleado',
            fields=[
                ('id_estado_emp', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'estado_empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoOrden',
            fields=[
                ('id_estado', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'estado_orden',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoPedido',
            fields=[
                ('id_estado_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'estado_pedido',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoVenta',
            fields=[
                ('id_estado_venta', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'estado_venta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id_factura', models.AutoField(primary_key=True, serialize=False)),
                ('sub_total', models.BigIntegerField()),
                ('iva', models.BigIntegerField()),
                ('giro', models.CharField(max_length=50)),
                ('total', models.BigIntegerField()),
            ],
            options={
                'db_table': 'factura',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FamiliaProducto',
            fields=[
                ('id_fam_prod', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'familia_producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrdenCompra',
            fields=[
                ('id_orden_compra', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_solicitud', models.DateField()),
                ('total', models.BigIntegerField()),
                ('neto', models.BigIntegerField()),
                ('iva', models.BigIntegerField()),
            ],
            options={
                'db_table': 'orden_compra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_recepcion', models.DateField()),
                ('fecha_pedido', models.DateField()),
                ('descripcion', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=100)),
                ('total', models.BigIntegerField()),
                ('documento', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'pedido',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProdProveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'prod_proveedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('fecha_vencimiento', models.DateField()),
                ('nombre', models.CharField(max_length=200)),
                ('stock', models.BigIntegerField()),
                ('stock_critico', models.BigIntegerField()),
                ('precio', models.BigIntegerField()),
                ('marca', models.CharField(max_length=20)),
                ('valor_producto_compra', models.BigIntegerField()),
                ('imagen', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.AutoField(primary_key=True, serialize=False)),
                ('rut_proveedor', models.BigIntegerField()),
                ('nombre_proveedor', models.CharField(max_length=50)),
                ('telefono', models.BigIntegerField()),
                ('telefono_2', models.BigIntegerField(blank=True, null=True)),
                ('correo', models.CharField(max_length=50)),
                ('giro', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'proveedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RespaldoVenta',
            fields=[
                ('id_respaldo', models.AutoField(primary_key=True, serialize=False)),
                ('nro_venta', models.BigIntegerField()),
                ('fecha_venta', models.DateField()),
                ('nro_boleta', models.BigIntegerField(blank=True, null=True)),
                ('nro_factura', models.BigIntegerField(blank=True, null=True)),
                ('nro_pedido', models.BigIntegerField(blank=True, null=True)),
                ('total', models.BigIntegerField()),
                ('id_producto', models.CharField(max_length=20)),
                ('cantidad', models.BigIntegerField()),
            ],
            options={
                'db_table': 'respaldo_venta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoEmpleado',
            fields=[
                ('id_tipo_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tipo_empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id_tipo_producto', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'tipo_producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoVivienda',
            fields=[
                ('id_tipo_vivienda', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tipo_vivienda',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsuarioCliente',
            fields=[
                ('id_usuario_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'usuario_cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsuarioEmpleado',
            fields=[
                ('id_usuario_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'usuario_empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_venta', models.DateField()),
            ],
            options={
                'db_table': 'venta',
                'managed': False,
            },
        ),
    ]
