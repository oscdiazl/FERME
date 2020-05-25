from django import forms
from django.forms import ModelForm
from .models import Proveedor, Empleado, OrdenCompra, Producto, Direccion, Cliente, Factura
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields =['nombre_proveedor', 'rut_proveedor', 'telefono', 'correo', 'giro']

class EmpleadoForm(ModelForm): 
    class Meta: 
        model = Empleado
        fields =['rut_empleado', 'nombres','apaterno','amaterno', 'telefono','telefono_2', 'correo', 'tipo_empleado_id_tipo_empleado','estado_empleado_id_estado_emp' ]

class OrdenDeCompraForm(ModelForm): 
    class Meta: 
        model = OrdenCompra
        fields = ['proveedor_id_proveedor','id_orden_compra','fecha_solicitud','empleado_rut_empleado','estado_orden_id_estado','neto','iva','total']

class ProductoForm(ModelForm):
    class Meta: 
        model = Producto
        fields = ['tipo_producto_id_tipo_producto', 'id_producto', 'fecha_vencimiento', 'familia_producto_id_fam_prod', 'nombre', 'stock', 'stock_critico', 'precio', 'marca', 'valor_producto_compra', 'imagen']

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut_cliente', 'nombres', 'apaterno', 'amaterno', 'telefono', 'telefono_2', 'correo', 'rut_empresa', 'razon_social', 'giro', 'estado_cli_id_estado_cli']

class DireccionForm(ModelForm):
    class Meta:
        model = Direccion
        fields = ['numero', 'calle', 'piso', 'codigo_postal', 'tipo_vivienda_id_tipo_vivienda', 'comuna_id_comuna']

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email','password1','password2']

class UserEditForm(forms.ModelForm): 
    class Meta: 
        model = User
        fields = [
            'username','first_name', 'last_name', 'email'
        ]

class FacturaForm(forms.ModelForm): 
    class Meta: 
        model = Factura
        fields = [
            'sub_total', 'iva', 'giro', 'total', 'estado_venta_id_estado_venta'
        ]