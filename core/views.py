from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from .models import Proveedor, Empleado, OrdenCompra, Producto, DetalleOc, EstadoOrden, Producto, Cliente, Direccion, EstadoCli, UsuarioCliente, Factura, Venta, Boleta, Venta, DireccionEmp, TipoVivienda, Comuna, EstadoPedido, Pedido
from .forms import ProveedorForm, EmpleadoForm,OrdenDeCompraForm, ProductoForm, CustomUserForm, DireccionForm, ClienteForm,UserEditForm, FacturaForm, BoletaForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate
import bcrypt
import json
from datetime import date
from passlib.hash import pbkdf2_sha256
from django.contrib.auth.hashers import make_password
# Create your views here.

def home(request):
    prod_tipo_taladro = Producto.objects.filter(tipo_producto_id_tipo_producto=2)
    data ={
        'prod_tipo_taladro': prod_tipo_taladro
    }
    return render(request, 'core/home.html', data)

def productos(request):
    prod_cerraduras = Producto.objects.filter(tipo_producto_id_tipo_producto=21)
    prod_herramientas_manuales = Producto.objects.filter(tipo_producto_id_tipo_producto=22)
    productos = Producto.objects.all()
    data ={
        'prod_tipo_cerradura': prod_cerraduras, 
        'prod_herramientas_manuales': prod_herramientas_manuales, 
        'productos': productos
    }
    return render(request, 'core/productos.html', data)

@login_required
def listado_proveedor(request):
    proveedores = Proveedor.objects.all()
    data = {
        'proveedores' : proveedores,
        'form': ProveedorForm()
    }

    if request.method == 'POST':
        formulario = ProveedorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado Correctamente"
    return render(request, 'core/listado_proveedor.html', data)

def listado_empleados(request): 
    empleados = Empleado.objects.all()

    data = {
        'empleados': empleados, 
        'form' : EmpleadoForm(),
        'formDir':DireccionForm(),
        'userForm':CustomUserForm()
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(request.POST)
        userFormulario = CustomUserForm(request.POST)
        formularioDir = DireccionForm(request.POST)
        if formulario.is_valid() and userFormulario.is_valid() and formularioDir.is_valid():
            formulario.save()
            userFormulario.save()
            formularioDir.save()

            username = userFormulario.cleaned_data['username']
            password = userFormulario.cleaned_data['password1']
            rut_empleado = formulario.cleaned_data['rut_empleado']

            max = Direccion.traerUltimoIdDireccion()

            password_1 = make_password(password)

            print(password_1)

            print(max)
            Empleado.agregarDireccionEmpleado(max['ID_MAX'], rut_empleado)
            Empleado.agregarUsuarioEmpleado(rut_empleado, username, password_1)

            data['mensaje'] = "Guardado Correctamente"

    return render(request, 'core/listado_empleados.html', data)





def listado_orden_compra(request): 
    ordenesDeCompra = OrdenCompra.objects.all()
    productos = Producto.objects.all()

    ordenesDeCompra = OrdenCompra.traerOrdenes()

    productos_proveedor = Producto.productos_proveedor()
    print(productos_proveedor)
    
    data={
        'ordenesDeCompra': ordenesDeCompra, 
        'form': OrdenDeCompraForm(), 
        'productos' : productos_proveedor
    }
    if request.method == 'POST':
        formulario = OrdenDeCompraForm(request.POST)
        if formulario.is_valid():
            id_producto = request.POST.get('id_producto')
            cantidad = request.POST.get('id_cantidad')
            formulario.save()
            data['mensaje'] = "Guardado Correctamente"

            max = OrdenCompra.traerUltimoId()
            OrdenCompra.agregarDetalleOrden(max['ID_MAX'],id_producto, cantidad)
            print(id_producto, max, cantidad)
            productosOrden = OrdenCompra.productosOrden(str(max['ID_MAX']))
            data['productos_orden'] = productosOrden
            print(data['productos_orden'])
            
            return redirect('modificar_orden', id=max['ID_MAX'])



            """"
            id_producto = request.POST.get('id_producto')
            max = OrdenCompra.traerUltimoId()

            cantidad = request.POST.get('id_cantidad')
            total = request.POST.get('id_precio')

            OrdenCompra.agregarDetalleOrden(max['ID_MAX'],id_producto, cantidad)
            productosOrden = OrdenCompra.productosOrden(str(max['ID_MAX']))
            data['productos_orden'] = productosOrden
            print(data['productos_orden'])
            
            return redirect('modificar_orden', id=max['ID_MAX'])"""

    return render(request, 'core/listado_orden_compra.html', data)

def modificar_orden(request, id):
    orden = OrdenCompra.traerOrden(id)
    productos = Producto.objects.all()
    productosOrden = OrdenCompra.productosOrden(id)

    proveedores = Proveedor.objects.all()
    empleados = Empleado.objects.all()
    estadosOrden = EstadoOrden.objects.all()

    productos_proveedor = Producto.productos_proveedor()

    data = {
        'orden' : orden, 
        'productos' : productos_proveedor,
        'productos_orden':productosOrden, 
        'proveedores' : proveedores, 
        'empleados' : empleados, 
        'estadosOrden': estadosOrden
    }

    if request.method == 'POST': 

        id_producto = request.POST.get('id_producto')
        cantidad = request.POST.get('id_cantidad')
        total = request.POST.get('id_precio')
        OrdenCompra.agregarDetalleOrden(id,id_producto, cantidad)
        data['productos_orden'] = OrdenCompra.productosOrden(id)

        proveedor_id_proveedor = request.POST.get('cboProveedor')


        id_orden_compra = request.POST.get('txtId')
        fecha_solicitud = request.POST.get('txtFechaSolicitud')
        empleado_rut_empleado = request.POST.get('cboEmpleado')
        estado_orden_id_estado = request.POST.get('cboEstado')

        print(estado_orden_id_estado)

        total = request.POST.get('txtTotal')
        neto = request.POST.get('txtNeto')
        iva = request.POST.get('txtIva')

        print(proveedor_id_proveedor)
                    
        OrdenCompra.modificar_orden(proveedor_id_proveedor,id_orden_compra, fecha_solicitud, empleado_rut_empleado, estado_orden_id_estado, total, neto, iva )
        data['orden'] = OrdenCompra.traerOrden(id)
    return render(request, 'core/modificar_orden.html', data)

def modificar_empleado(request, id):
    empleado = Empleado.objects.get(rut_empleado=id)

    direccion_empleado = Empleado.traerDireccionEmpleado(id)

    tipo_viviendas = TipoVivienda.objects.all()

    comunas = Comuna.objects.all()

    print(direccion_empleado)

    data={
        'form': EmpleadoForm(instance=empleado), 
        'direccion_emp': direccion_empleado, 
        'tipo_vivienda': tipo_viviendas, 
        'comuna': comunas
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(data=request.POST, instance=empleado)
        if formulario.is_valid():

            numero = request.POST.get('id_calle_numero')
            calle = request.POST.get('id_calle_direccion')
            piso = request.POST.get('id_piso')
            codigo_postal = request.POST.get('id_codigo_postal')
            tipo_vivienda = request.POST.get('cboTipoVivienda')
            comuna = request.POST.get('cboComuna')

            id_direccion = request.POST.get('id_dir')

            try:
                Empleado.modificar_direccion_empleado(id_direccion, numero, calle, piso, codigo_postal, tipo_vivienda, comuna)
                print("Se Actualizo Empleado")
            except Exception as e:
                print("No se Actualizo Empleado" + e)

            formulario.save()
            data['direccion_emp'] = Empleado.traerDireccionEmpleado(id)
            data ["mensaje"] = "Modificado Correctamente"
            data['form']  = formulario
            


    return render(request,  'core/modificar_empleado.html', data)

def modificar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id_proveedor=id)
    data = {
        'form': ProveedorForm(instance=proveedor)
    }

    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST, instance=proveedor)
        if formulario.is_valid():
            formulario.save()
            data['form']  = formulario
            data ["mensaje"] = "Modificado Correctamente"
    return render(request, 'core/modificar_proveedor.html', data)

def eliminar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id_proveedor=id)
    proveedor.delete()

    return redirect(to="listado_proveedor")

def eliminar_empleado(request, id): 
    empleado = Empleado.objects.get(rut_empleado=id)
    empleado.delete()

    return redirect(to="listado_empleados")

def sobre_nosotros(request):
    return render(request, 'core/sobre_nosotros.html')


@login_required
def listado_producto(request): 
    productos = Producto.objects.all()
    proveedores = Proveedor.objects.all()
    data = {
        'productos': productos,
        'form': ProductoForm(),
        'proveedores':proveedores
    }

    numero = '105'
    nuevo_numero = numero.zfill(3)
    print(nuevo_numero)

    if request.method == 'POST':

        id_proveedor = request.POST.get('cboProveedor')
        id_producto = request.POST.get('id_producto')
        formulario = ProductoForm(request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            Producto.agregarDetalleProductoProveedor(id_producto,id_proveedor)
            data['mensaje'] = "Guardado Correctamente"
        else: 
            data['mensaje'] = "No se pudo Guardar"

        
    return render(request, 'core/listado_productos.html', data)

def modificar_producto(request, id): 
    producto = Producto.objects.get(id_producto=id)
    proveedores = Proveedor.objects.all()
    prod_proveedor = Producto.traerProveedorProducto(str(id))

    print(prod_proveedor)
    data = {
        'producto': producto,
        'form' : ProductoForm(instance=producto),
        'proveedores':proveedores, 
        'prod_proveedor': prod_proveedor
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['form']  = formulario
            data ["mensaje"] = "Modificado Correctamente"
    return render(request, 'core/modificar_producto.html', data)

def registro_usuario(request):

    estado_clientes = EstadoCli.objects.all()

    data = {
        'form':CustomUserForm(),
        'formDir':DireccionForm(),
        'estados_cliente':estado_clientes
    }

    if request.method == 'POST':

        rut =request.POST.get('txtRutCliente')
        nombres = request.POST.get('txtNombres')
        apaterno = request.POST.get('txtaPaterno')
        amaterno = request.POST.get('txtaMaterno')
        telefono = request.POST.get('txtTelefono')

        telefono_2 = request.POST.get('txtTelefono2')
        correo = request.POST.get('txtCorreo')
        rut_empresa = request.POST.get('txtRutEmpresa')
        razon_social = request.POST.get('txtRazonSocial')
        giro = request.POST.get('txtGiro')
        estado = request.POST.get('cboEstado')


        try:
            Cliente.agregarCliente(rut, nombres, apaterno,amaterno, telefono, telefono_2, correo, rut_empresa, razon_social, giro, '1')
            formulario = CustomUserForm(request.POST)
            formularioDir = DireccionForm(request.POST)
            if formulario.is_valid() and formularioDir.is_valid():

                try:
                    formulario.save()
                    formularioDir.save()
                    max = Direccion.traerUltimoIdDireccion()
                    username = formulario.cleaned_data['username']
                    password = formulario.cleaned_data['password1']

                    print(username, password, rut)

                    password_1 = make_password(password)

                    UsuarioCliente.agregarUsuarioCliente(username, password_1, rut)
                    Cliente.agregarDireccionCliente(max['ID_MAX'], rut)

                    user = authenticate(username=username, password=password)
                    login(request, user)
                    return redirect(to='home')
                except Exception  as e:
                    print(e)
            else:
                data['mensaje'] = "No se pudo guardar"
        except:
            data['mensaje'] = "No se pudo guardar"

        


            
    return render(request, 'registration/registrar.html', data)


def change_password(request):

    data={}

    user = request.user

    if request.method =='POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        data = {'form' : form}

        if form.is_valid():
            try:
                usuario_bd = UsuarioCliente.traerUsuarioEmpleado(str(user).lower())
                print(usuario_bd)
                new_pass = request.POST.get('new_password2')
                print("Es usuario Empleado")

                try:
                    password_1 = make_password(new_pass)
                    Empleado.actualizar_pass_empleado(usuario_bd['EMPLEADO_RUT_EMPLEADO'], password_1)
                    print("Password Fue Actualizada")
                    data['mensaje'] = "Contrasenia de empleoado fue Modificada Correctamente"
                except Exception as e:
                    print("No fue actualizada la pass" + e)
            except Exception as e:
                print("No Es usuario Empleado")
                print(e)

                try:
                    usuario_bd_cliente = UsuarioCliente.traerUsuarioCliente(str(user).lower())
                    print("Es Usuario Cliente")
                    print(usuario_bd_cliente)

                    try:
                        new_pass = request.POST.get('new_password2')
                        password_1 = make_password(new_pass)

                        Cliente.actualizar_pass_cliente(usuario_bd_cliente['CLIENTE_RUT_CLIENTE'], password_1)
                        print("la pass de cliente se actualizo")
                        data['mensaje'] = "Contrasenia de cliente fue Modificada Correctamente"
                    except Exception as e:
                        print("No Se pudo actualizar la pass")
                except Exception as e: 
                    print("No Es usuario Cliente")
                    print(e)
            form.save()
            update_session_auth_hash(request, form.user)
            
    else: 
        form = PasswordChangeForm(user=request.user)
        data = {'form' : form}
    return render(request, 'registration/change_password.html', data)

def edit_profile(request):

    data={
    }

    user = request.user

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        new_name = request.POST.get('username')
        try:
            try:
                Empleado.modificarUsuarioCliente(str(user),new_name)
                usuario_bd = UsuarioCliente.traerUsuarioEmpleado(str(new_name).lower())
                print("Existe Usuario Empleado")
                nombre = request.POST.get('first_name')
                apellido = request.POST.get('last_name').split(" ")
                email = request.POST.get('email')

                print(nombre, apellido, email, usuario_bd['EMPLEADO_RUT_EMPLEADO'], new_name)

                try:
                    Empleado.modificarDatosEmpleado(nombre, apellido[0], email, usuario_bd['EMPLEADO_RUT_EMPLEADO'])
                except Exception as e:
                    print(e)
            except Exception as e: 
                print(e)
                print("No Existe Usuario Empleado")
                try:
                    UsuarioCliente.modificar_usuario_cliente(str(user),new_name)
                    usuario_bd_cliente = UsuarioCliente.traerUsuarioCliente(str(new_name).lower())
                    print("Si es usuario Cliente")

                    try:
                        nombre = request.POST.get('first_name')
                        apellido = request.POST.get('last_name').split(" ") 
                        email = request.POST.get('email')
                        UsuarioCliente.modificar_datos_cliente(nombre, apellido[0],apellido[1], email, usuario_bd_cliente['CLIENTE_RUT_CLIENTE'])
                        print("Se Guardadron los datos del cliente")
                    except Exception as e:
                        print("No se guardaron los nuevos datos del cliente")
                        print(e)
                except Exception as e:
                    print("No Es usuario Cliente")
        except Exception as e:
            print(e)

        if form.is_valid():
            form.save()
            data['mensaje'] = "Guardado Correctamente"
            return redirect('edit_profile')
    else: 
        form = UserEditForm(instance=request.user)
        data = {'form' : form}
        
    return render(request, 'registration/edit_profile.html', data)


def listado_factura(request):

    productos = Producto.productos_proveedor()
    facturas = Factura.objects.all()
    clientes = Cliente.objects.all()

    empleados = Empleado.objects.all()

    data = { 
        'form' : FacturaForm(), 
        'productos' : productos, 
        'facturas' : facturas, 
        'clientes': clientes, 
        'empleados': empleados
    } 

    if request.method == 'POST':
        formulario = FacturaForm(request.POST)
        if formulario.is_valid():
            formulario.save()

            ultima_factura = Factura.traerUltimoIdFactura()
            print(ultima_factura['ID_MAX'])

            id_producto = request.POST.get('id_producto')
            cantidad = request.POST.get('id_cantidad')

            rut_cliente = request.POST.get('id_rut_cliente')
            empleado_rut_empleado = request.POST.get('cboEmpleado')
            fecha_venta = date.today()

            Factura.agregarDetalleFactura(ultima_factura['ID_MAX'],id_producto, cantidad)
            Factura.agregarVentaFactura(rut_cliente, fecha_venta,ultima_factura['ID_MAX'], empleado_rut_empleado)

            ultima_venta = Venta.traerUltimoIdVenta()

            Venta.agregarDetalleVentaFactura(ultima_venta['ID_MAX'], id_producto)

            Producto.descontarStockFactura(id_producto, cantidad)
            data['mensaje'] = "Guardado Correctamente"

            return redirect('modificar_factura', id=ultima_factura['ID_MAX'])
        else: 
            data['mensaje'] = "No se pudo guardar"


    return render(request, 'core/listado_factura.html', data)

def modificar_factura(request, id): 
    factura = Factura.objects.get(id_factura=id)
    clientes = Cliente.objects.all()
    productos = Producto.productos_proveedor()
    venta = Venta.traerVenta(id)

    empleados = Empleado.objects.all()

    cliente_factura_actual = Factura.traerClienteFactura(id)
    productos_factura = Factura.traerProductosFactura(id)

    print(cliente_factura_actual)

    data = {
        'form': FacturaForm(instance=factura),
        'clientes': clientes,
        'cliente_actual' : cliente_factura_actual,
        'productos' : productos,
        'productos_factura' : productos_factura, 
        'empleados': empleados, 
        'venta': venta, 
        'factura':factura
    }

    if request.method == 'POST': 
        id_producto = request.POST.get('id_producto')
        cantidad = request.POST.get('id_cantidad')

        id_venta = Factura.idVentaFactura(id)

        Factura.agregarDetalleFactura(int(id),id_producto, cantidad)
        Factura.agregarDetalleVenta(int(id_venta['ID_VENTA']), id_producto)

        Producto.descontarStockFactura(id_producto, cantidad)

        subtotal = request.POST.get('sub_total')
        iva = request.POST.get('iva')
        giro = request.POST.get('giro')
        total = request.POST.get('total')

        estado_factura = request.POST.get('estado_venta_id_estado_venta')

        Factura.actualizarFactura(id,subtotal, iva, giro, total, estado_factura )

        factura = Factura.objects.get(id_factura=id)
        data['productos_factura'] = Factura.traerProductosFactura(id)
        data['productos'] = Producto.productos_proveedor()
        data['form'] = FacturaForm(instance=factura)

    return render(request, 'core/modificar_factura.html', data)


def eliminar_producto_factura(request, id, sku, cantidad, total):
    id_venta = Factura.idVentaFactura(id)
    try:
        print(id, sku, cantidad, id_venta)
        Factura.eliminarProductoFactura(id, sku, cantidad, id_venta['ID_VENTA'], total)
        Producto.sumarStockFactura(sku, cantidad)
        print("se elimino")
    except:
        print("Hubo un error")
    return redirect('modificar_factura', id)

def eliminar_producto_oc(request, id, sku, cantidad, total):

    print(id, sku, cantidad, total)

    try:
        OrdenCompra.eliminarProductoOrden(id, sku, cantidad, total)
        print("Se Elimino")
    except Exception as e:
        print(e)

    return redirect('modificar_orden', id)


def listado_boleta(request):

    productos = Producto.productos_proveedor()
    boletas = Boleta.objects.all()

    empleados = Empleado.objects.all()
    data = {
        'form' : BoletaForm(),
        'productos' : productos,
        'boletas' : boletas, 
        'empleados' : empleados
    }

    if request.method == 'POST':
        formulario = BoletaForm(request.POST)
        if formulario.is_valid():
            formulario.save()

            ultima_boleta = Boleta.traerUltimoIdBoleta()
            print(ultima_boleta['ID_MAX'])
            id_producto = request.POST.get('id_producto')
            cantidad = request.POST.get('id_cantidad')
            fecha_venta = date.today()
            rut_empleado = request.POST.get('cboEmpleado')

            Boleta.agregarDetalleBoleta(ultima_boleta['ID_MAX'],id_producto,cantidad)
            Boleta.agregarVentaBoleta(rut_empleado,ultima_boleta['ID_MAX'],fecha_venta)
        
            ultima_venta = Venta.traerUltimoIdVenta()

            Venta.agregarDetalleVenta(ultima_venta['ID_MAX'],id_producto)

            Producto.descontarStockFactura(id_producto, cantidad)
            data['mensaje'] = "Guardado Correctamente"

            return redirect('modificar_boleta', id=ultima_boleta['ID_MAX'])
        else:
            data['mensaje'] = "No se pudo guardar"


    return render(request, 'core/listado_boleta.html', data)



def modificar_boleta(request, id):

    boleta = Boleta.objects.get(id_boleta=id)
    productos = Producto.productos_proveedor()
    productosBoleta = Boleta.traerProductosBoleta(id)
    venta = Venta.traerVentaBoleta(id)

    empleados = Empleado.objects.all()

    id_factura = id

    data = {
        'form': BoletaForm(instance=boleta),
        'productos' : productos,
        'productos_boleta' : productosBoleta,
        'empleados': empleados, 
        'venta' : venta, 
        'boleta':boleta
    }

    if request.method == 'POST':
        id_producto = request.POST.get('id_producto')
        cantidad = request.POST.get('id_cantidad')
        fecha_venta = date.today()
        rut_empleado = request.POST.get('cboEmpleado')

        estado_boleta = request.POST.get('estado_venta_id_estado_venta')

        total = request.POST.get('total')

        id_venta = Boleta.idVentaBoleta(id)

        Boleta.agregarDetalleBoleta(int(id),id_producto,cantidad)
        Boleta.agregarVentaBoleta(rut_empleado,int(id),fecha_venta)
        Venta.agregarDetalleVenta(int(id_venta['ID_VENTA']), id_producto)
        Boleta.actualizarBoleta(id, total,estado_boleta)

        Producto.descontarStockFactura(id_producto, cantidad)

        print(total)

        boleta = Boleta.objects.get(id_boleta=id)
        data['productos'] = Producto.productos_proveedor()
        data['productos_boleta'] = Boleta.traerProductosBoleta(id)
        data['form'] = BoletaForm(instance=boleta)
    else:
        print("No se Modifico")


    return render(request, 'core/modificar_boleta.html', data)


def eliminar_producto_boleta(request, id, sku, cantidad, total):
    id_venta = Boleta.idVentaBoleta(id)
    try:
        print(id, sku, cantidad, id_venta)
        Boleta.eliminarProductoBoleta(id, sku, cantidad, id_venta['ID_VENTA'], total)
        Producto.sumarStockFactura(sku, cantidad)
        print("se elimino")
    except:
        print("Hubo un error")
    return redirect('modificar_boleta', id)


def recepcion_orden_compra(request): 

    ordenesDeCompra = OrdenCompra.traerOrdenes()
    

    data = {
        'ordenesDeCompra' : ordenesDeCompra
    }

    return render(request, 'core/recepcion_orden.html', data)

def modificar_recepcion_orden(request, id): 

    orden = OrdenCompra.traerOrden(id)
    proveedores = Proveedor.objects.all()
    empleados = Empleado.objects.all()
    estadosOrden = EstadoOrden.objects.all()

    productosOrden = OrdenCompra.productosOrden(id)

    data = {
        'orden': orden,
        'proveedores' : proveedores,
        'empleados' : empleados,
        'estadosOrden': estadosOrden,
        'productos_orden':productosOrden
    }

    return render(request, 'core/modificar_recepcion_orden.html', data)


def actualizar_stock_recepcion(request, id, sku, cantidad): 
    print(id, sku, cantidad)
    try:
        Producto.actualizarStockProductoRecepcion(sku, cantidad)
        print("Se actualizo el stock")
    except Exception as e:
        print(e)

    return redirect('modificar_recepcion_orden', id)

def aprobar_orden(request, id): 
    try:
        OrdenCompra.aprobarOrdenCompra(id)
        print("Se aprobo la orden")
    except Exception as e:
        print(e)
    return redirect('modificar_recepcion_orden', id)

def rechazar_orden(request, id):
    try:
        OrdenCompra.rechazarOrdenCompra(id)
        print("Se rechazo la orden")
    except Exception as e:
        print(e)
        print("No se rechazo la orden")
    return redirect('modificar_recepcion_orden', id)


def consultar_proveedor(request): 

    data = {

    }

    if request.method == 'POST':
        rut_proveedor = request.POST.get('rut_proveedor')

        ordenes_proveedor = Proveedor.ordenesProveedor(rut_proveedor)
        if len(ordenes_proveedor) > 0:
            data['ordenes_prov'] = ordenes_proveedor
        else:
            data['error'] = "No Hay Ordenes Asociadas al Proveedor"

    return render(request, 'core/consulta_proveedor.html', data)

def modificar_consultar_proveedor(request, id):
    orden = OrdenCompra.traerOrden(id)
    proveedores = Proveedor.objects.all()
    empleados = Empleado.objects.all()
    estadosOrden = EstadoOrden.objects.all()

    productosOrden = OrdenCompra.productosOrden(id)

    data = {
        'orden': orden,
        'proveedores' : proveedores,
        'empleados' : empleados,
        'estadosOrden': estadosOrden,
        'productos_orden':productosOrden
    }

    return render(request, 'core/modificar_consulta_proveedor.html', data)

def eliminar_producto_orden_prov(request, id, sku, cantidad, total):

    print(id, sku, cantidad, total)

    try:
        OrdenCompra.eliminarProductoOrden(id, sku, cantidad, total)
        print("Se Elimino")
    except Exception as e:
        print(e)

    return redirect('modificar_consultar_proveedor', id)


def recepcionar_orden_proveedor(request, id): 
    try:
        OrdenCompra.recepcionarOrdenProveedor(id)
        print("Se Recepciono La orden")
    except Exception as e:
        print(e)
    return redirect('modificar_consultar_proveedor', id)

def rechazar_orden_proveedor(request,id):
    try:
        OrdenCompra.rechazarOrdenProveedor(id)
        print("Se Recepciono La orden")
    except Exception as e:
        print(e)
    return redirect('modificar_consultar_proveedor', id)


def anular_stock_factura(request, id, sku, cantidad):
    Producto.sumarStockFactura(sku, cantidad)
    return redirect('modificar_factura', id)

def anular_factura(request, id):
    try:
        Factura.anular_factura(id)
        print("Se anulo")
    except Exception as e:
        print(e)

    return redirect('modificar_factura', id)

def anular_stock_boleta(request, id, sku, cantidad):
    try:
        Producto.sumarStockFactura(sku, cantidad)
    except Exception as e:
        print(e)
    return redirect('modificar_boleta', id)

def anular_boleta(request, id):

    try:
        Boleta.anular_boleta(id)
        print("Se Anulo")
    except Exception as e:
        print(e)

    return redirect('modificar_boleta', id)

def listado_clientes(request): 

    clientes = Cliente.objects.all()

    data={
        'clientes': clientes
    }

    return render(request, 'core/listado_clientes.html', data)

def modificar_cliente(request, id):

    cliente = Cliente.objects.get(rut_cliente=id)
    direccion_cliente = Cliente.traerDireccionCliente(id)

    tipo_viviendas = TipoVivienda.objects.all()
    comunas = Comuna.objects.all()

    data ={
        'form' : ClienteForm(instance=cliente),
        'direccion_cliente': direccion_cliente, 
        'tipo_vivienda': tipo_viviendas, 
        'comuna': comunas
    }

    if request.method == 'POST': 
        formulario = ClienteForm(data=request.POST, instance=cliente)
        if formulario.is_valid():
            numero = request.POST.get('id_numero')
            calle = request.POST.get('id_calle')
            piso = request.POST.get('id_piso')
            codigo_postal = request.POST.get('id_codigo_postal')
            tipo_vivienda = request.POST.get('cboTipoVivienda')
            comuna = request.POST.get('cboComuna')
            id_direccion = request.POST.get('id_dir')

            try:
                Empleado.modificar_direccion_empleado(id_direccion, numero, calle, piso, codigo_postal, tipo_vivienda, comuna)
                print("Se Actualizo Cliente")
            except Exception as e:
                print(e)

            formulario.save()
            data['direccion_cliente'] = Cliente.traerDireccionCliente(id)
            data['mensaje'] = "Modificado Correctamente"
            data['form'] = formulario

    return render(request, 'core/modificar_cliente.html', data)


def pedido(request): 
    estados_pedido = EstadoPedido.objects.all()
    comunas = Comuna.objects.all()

    user = request.user

    

    data = {
        'estado_ped' : estados_pedido, 
        'comunas': comunas
    }

    if request.method == 'POST': 
        estado_pedido = request.POST.get('cboEstadoPedido')
        fecha_recepcion = request.POST.get('fecha_recep')
        fecha_pedido = request.POST.get('fecha_ped')
        detalle_pedido = request.POST.get('txtDetallePedido')
        direccion_pedido = request.POST.get('txtDireccion')
        comuna_pedido = request.POST.get('cboComuna')

        print(estado_pedido, fecha_recepcion, fecha_pedido, detalle_pedido, direccion_pedido, comuna_pedido)

        try:
            usuario_bd_cliente = UsuarioCliente.traerUsuarioCliente(str(user).lower())
            print("Datos Del CLiente")
            print(usuario_bd_cliente)
            Pedido.insertar_pedido(estado_pedido, fecha_recepcion, fecha_pedido, detalle_pedido, direccion_pedido, comuna_pedido)
            data['mensaje'] = "Pedido Agregado Correctamente"
        except Exception as e: 
            print(e)
            data['error'] = "Pedido no pudo ser agregado"


    return render(request, 'core/pedido.html', data)

def reportes(request):
    data = {}

    if request.method == 'POST' and 'btnVentasAcumuladas' in request.POST:
        getMes = request.POST.get('nombre_mes')
        anio = getMes.split('-')[0]
        mes = getMes.split('-')[1]
        reporteVentaTotal = Venta.reporteVentasTotal(mes,anio)
        print(reporteVentaTotal)
        data['reporteVentaTotal'] = reporteVentaTotal
    elif request.method == 'POST' and 'btnBoletasMensuales' in request.POST:
        getMes = request.POST.get('mes_boletas')
        anio = getMes.split('-')[0]
        mes = getMes.split('-')[1]
        reporteBoleta = Boleta.reporteBoleta(mes,anio)
        print(reporteBoleta)
        data['reporteBoleta'] = reporteBoleta
    elif request.method == 'POST' and 'btnFacturasMensuales' in request.POST:
        getMes = request.POST.get('mes_facturas')
        anio = getMes.split('-')[0]
        mes = getMes.split('-')[1]
        reporteFactura = Factura.reporteFactura(mes, anio)
        print(reporteFactura)
        data['reporteFactura'] = reporteFactura
    elif request.method == 'POST' and 'btnCantidadVentas' in request.POST:
        getMes = request.POST.get('cantidad_ventas_mes')
        anio = getMes.split('-')[0]
        mes = getMes.split('-')[1]
        reporteVenta = Venta.reporteVenta(mes,anio)
        print(reporteVenta)
        data['reporteVenta'] = reporteVenta
    elif request.method == 'POST' and 'btnProductoMasVendido' in request.POST:
        getMes = request.POST.get('producto_mas_vendido_mes')
        anio = getMes.split('-')[0]
        mes = getMes.split('-')[1]
        reporteProducto = Producto.reporteProducto(mes,anio)
        print(reporteProducto)
        data['reporteProducto'] = reporteProducto

    return render(request, 'core/reportes.html', data)
