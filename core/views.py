from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from .models import Proveedor, Empleado, OrdenCompra, Producto, DetalleOc, EstadoOrden, Producto, Cliente, Direccion, EstadoCli, UsuarioCliente, Factura, Venta
from .forms import ProveedorForm, EmpleadoForm,OrdenDeCompraForm, ProductoForm, CustomUserForm, DireccionForm, ClienteForm,UserEditForm, FacturaForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate
import bcrypt
import json
from datetime import date
# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def productos(request):
    return render(request, 'core/productos.html')

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

            print(max)
            Empleado.agregarDireccionEmpleado(max['ID_MAX'], rut_empleado)
            Empleado.agregarUsuarioEmpleado(rut_empleado, username, password)

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

    data={
        'form': EmpleadoForm(instance=empleado)
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(data=request.POST, instance=empleado)
        if formulario.is_valid():
            formulario.save()
            data ["mensaje"] = "Modificado Correctamente"
            data['form']  = formulario
            return redirect('listado_empleados')
            


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
    data = {
        'form' : ProductoForm(instance=producto),
        'proveedores':proveedores
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data ["mensaje"] = "Modificado Correctamente"
            data['form']  = formulario
            return redirect('listado_productos')
    return render(request, 'core/modificar_producto.html', data)

def registro_usuario(request):

    estado_clientes = EstadoCli.objects.all()

    data = {
        'form':CustomUserForm(),
        'formDir':DireccionForm(),
        'estados_cliente':estado_clientes
    }

    passw = b"portafolio2020"
    hashed = bcrypt.hashpw(passw, bcrypt.gensalt())

    if bcrypt.checkpw(passw, hashed):
        print('Coinciden')
    else:
        print('no coinciden')

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

                    UsuarioCliente.agregarUsuarioCliente(username, password, rut)
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

    if request.method =='POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        data = {'form' : form}

        if form.is_valid():
            form.save()
            data['mensaje'] = "Guardado Correctamente"
            update_session_auth_hash(request, form.user)
            return redirect('change_password')
    else: 
        form = PasswordChangeForm(user=request.user)
        data = {'form' : form}
    return render(request, 'registration/change_password.html', data)

def edit_profile(request):
    usuario = UsuarioCliente.traerUsuarioCliente()
    print(usuario)
    data={
    }
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
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

            Factura.agregarDetalleFactura(ultima_factura['ID_MAX'],id_producto, cantidad)
            Factura.agregarVentaFactura(rut_cliente, '070903',ultima_factura['ID_MAX'], empleado_rut_empleado)

            ultima_venta = Venta.traerUltimoIdVenta()

            Venta.agregarDetalleVentaFactura(ultima_venta['ID_MAX'], id_producto)
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
        'venta': venta
    }

    if request.method == 'POST': 
        id_producto = request.POST.get('id_producto')
        cantidad = request.POST.get('id_cantidad')

        id_venta = Factura.idVentaFactura(id)

        Factura.agregarDetalleFactura(int(id),id_producto, cantidad)
        Factura.agregarDetalleVenta(int(id_venta['ID_VENTA']), id_producto)

        subtotal = request.POST.get('sub_total')
        iva = request.POST.get('iva')
        giro = request.POST.get('giro')
        total = request.POST.get('total')

        estado_factura = request.POST.get('estado_venta_id_estado_venta')

        Factura.actualizarFactura(id,subtotal, iva, giro, total, estado_factura  )

        factura = Factura.objects.get(id_factura=id)
        data['productos_factura'] = Factura.traerProductosFactura(id)
        data['form'] = FacturaForm(instance=factura)

    return render(request, 'core/modificar_factura.html', data)


def eliminar_producto_factura(request, id, sku, cantidad, total):
    id_venta = Factura.idVentaFactura(id)
    try:
        print(id, sku, cantidad, id_venta)
        Factura.eliminarProductoFactura(id, sku, cantidad, id_venta['ID_VENTA'], total)
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
