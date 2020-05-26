from django.urls import path
from .views import home, productos, listado_proveedor, listado_empleados, listado_orden_compra, sobre_nosotros, modificar_empleado, eliminar_empleado, modificar_proveedor, eliminar_proveedor, modificar_orden, listado_producto, registro_usuario, modificar_producto, change_password, edit_profile, listado_factura, modificar_factura, eliminar_producto_factura, eliminar_producto_oc, listado_boleta, modificar_boleta, eliminar_producto_boleta, recepcion_orden_compra,modificar_recepcion_orden,actualizar_stock_recepcion,aprobar_orden,rechazar_orden

urlpatterns = [
    path('', home, name="home"),
    path('productos/',productos, name="productos" ),
    path('listado_proveedor/', listado_proveedor, name="listado_proveedor"), 
    path('listado_empleados/', listado_empleados, name="listado_empleados"), 
    path('listado_orden_compra/', listado_orden_compra, name="listado_orden_compra" ),

    path('listado_recepcion_orden/', recepcion_orden_compra, name="listado_recepcion_orden"), 

    path('listado_factura/', listado_factura, name="listado_factura"),
    path('listado_boleta/', listado_boleta, name="listado_boleta"),

    path('sobre_nosotros/',sobre_nosotros, name="sobre_nosotros" ), 

    path('listado_productos/', listado_producto, name="listado_productos"),

    path('modificar_empleado/<id>/', modificar_empleado, name="modificar_empleado"),
    path('modificar_proveedor/<id>/', modificar_proveedor, name="modificar_proveedor"),
    path('modificar_orden/<id>/', modificar_orden, name="modificar_orden" ),
    path('modificar_producto/<id>/',modificar_producto, name="modificar_producto" ),
    path('modificar_factura/<id>/',modificar_factura, name="modificar_factura" ),
    path('modificar_boleta/<id>/', modificar_boleta, name="modificar_boleta"),
    path('modificar_recepcion_orden/<id>', modificar_recepcion_orden, name="modificar_recepcion_orden"),

    path('change_password/', change_password, name="change_password"),
    path('edit_profile/', edit_profile, name="edit_profile"),

    path('eliminar_empleado/<id>/', eliminar_empleado, name="eliminar_empleado"), 
    path('eliminar_proveedor/<id>/', eliminar_proveedor, name="eliminar_proveedor"),
    path('eliminar_producto_factura/<id>/<sku>/<cantidad>/<total>/', eliminar_producto_factura, name="eliminar_producto_factura"),
    path('eliminar_producto_oc/<id>/<sku>/<cantidad>/<total>/', eliminar_producto_oc, name="eliminar_producto_oc"),
    path('eliminar_producto_boleta/<id>/<sku>/<cantidad>/<total>/', eliminar_producto_boleta, name="eliminar_producto_boleta"),
    path('registro/', registro_usuario, name='registro_usuario'),


    path('actualizar_stock_recepcion/<id>/<sku>/<cantidad>/', actualizar_stock_recepcion, name="actualizar_stock_recepcion"),
    path('aprobar_orden_recepcionada/<id>', aprobar_orden, name="aprobar_orden_recepcionada"),
    path('rechazar_orden_recepcionada/<id>', rechazar_orden, name="rechazar_orden_recepcionada")

]
