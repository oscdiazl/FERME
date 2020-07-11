from django.urls import path
from .views import home, productos, listado_proveedor, listado_empleados, listado_orden_compra, sobre_nosotros, modificar_empleado, eliminar_empleado, modificar_proveedor, eliminar_proveedor, modificar_orden, listado_producto, registro_usuario, modificar_producto, change_password, edit_profile, listado_factura, modificar_factura, eliminar_producto_factura, eliminar_producto_oc, listado_boleta, modificar_boleta, eliminar_producto_boleta, recepcion_orden_compra,modificar_recepcion_orden,actualizar_stock_recepcion,aprobar_orden,rechazar_orden,consultar_proveedor,modificar_consultar_proveedor, eliminar_producto_orden_prov, recepcionar_orden_proveedor, rechazar_orden_proveedor, anular_stock_factura,anular_factura, anular_stock_boleta, anular_boleta, listado_clientes, modificar_cliente, pedido, reportes,anadir_productos_pedido,orden_productos,confirmar_pedido, listado_pedidos,insertar_venta_pedido,detalle_pedido,insertar_venta_pedido_factura,anular_orden, detalle_pedido_cliente, imprimir_detalle_boleta, imprimir_detalle_factura, detalle_filtro_producto

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
    path('listado_clientes/', listado_clientes, name="listado_clientes"),
    path('listado_pedidos/', listado_pedidos, name="listado_pedidos"),

    path('modificar_empleado/<id>/', modificar_empleado, name="modificar_empleado"),
    path('modificar_proveedor/<id>/', modificar_proveedor, name="modificar_proveedor"),
    path('modificar_orden/<id>/', modificar_orden, name="modificar_orden" ),
    path('modificar_producto/<id>/',modificar_producto, name="modificar_producto" ),
    path('modificar_factura/<id>/',modificar_factura, name="modificar_factura" ),
    path('modificar_boleta/<id>/', modificar_boleta, name="modificar_boleta"),
    path('modificar_recepcion_orden/<id>', modificar_recepcion_orden, name="modificar_recepcion_orden"),
    path('modificar_cliente/<id>', modificar_cliente, name="modificar_cliente"),

    path('change_password/', change_password, name="change_password"),
    path('edit_profile/', edit_profile, name="edit_profile"),

    path('eliminar_empleado/<id>/', eliminar_empleado, name="eliminar_empleado"), 
    path('eliminar_proveedor/<id>/', eliminar_proveedor, name="eliminar_proveedor"),
    path('eliminar_producto_factura/<id>/<sku>/<cantidad>/<total>/', eliminar_producto_factura, name="eliminar_producto_factura"),
    path('eliminar_producto_oc/<id>/<sku>/<cantidad>/<total>/', eliminar_producto_oc, name="eliminar_producto_oc"),
    path('eliminar_producto_orden_prov/<id>/<sku>/<cantidad>/<total>/', eliminar_producto_orden_prov, name="eliminar_producto_orden_prov"),
    path('eliminar_producto_boleta/<id>/<sku>/<cantidad>/<total>/', eliminar_producto_boleta, name="eliminar_producto_boleta"),
    path('registro/', registro_usuario, name='registro_usuario'),


    path('actualizar_stock_recepcion/<id>/<sku>/<cantidad>/', actualizar_stock_recepcion, name="actualizar_stock_recepcion"),
    path('aprobar_orden_recepcionada/<id>/', aprobar_orden, name="aprobar_orden_recepcionada"),
    path('rechazar_orden_recepcionada/<id>/', rechazar_orden, name="rechazar_orden_recepcionada"), 

    path('recepcionar_orden_proveedor/<id>/', recepcionar_orden_proveedor, name="recepcionar_orden_proveedor"),
    path('rechazar_orden_proveedor/<id>/', rechazar_orden_proveedor, name="rechazar_orden_proveedor"),  

    path('consulta_proveedor/', consultar_proveedor, name="consultar_proveedor"), 
    path('modificar_consultar_proveedor/<id>', modificar_consultar_proveedor, name="modificar_consultar_proveedor"), 
    
    path('anular_stock_factura/<id>/<sku>/<cantidad>/', anular_stock_factura, name="anular_stock_factura"), 
    path('anular_factura/<id>/', anular_factura, name="anular_factura"), 

    path('anadir_productos_pedido/<id_pedido>/<id_producto>/<cantidad>/', anadir_productos_pedido, name="anadir_productos_pedido"),
    path('orden_productos/<id_pedido>/', orden_productos, name="orden_productos"),

    path('anular_stock_boleta/<id>/<sku>/<cantidad>/', anular_stock_boleta, name="anular_stock_boleta"), 
    path('anular_boleta/<id>/', anular_boleta, name="anular_boleta"), 
    path('anular_orden/<id>/', anular_orden, name="anular_orden"),

    path('pedido/', pedido, name="pedido"),
    path('confirmar_pedido/<id_pedido>/<total>/', confirmar_pedido, name="confirmar_orden"), 
    path('insertar_venta_pedido/<id_pedido>/<fecha_venta>/<rut_cliente>/', insertar_venta_pedido, name="insertar_venta_pedido"),
    path('insertar_venta_pedido_factura/<id_pedido>/<fecha_venta>/<rut_cliente>/', insertar_venta_pedido_factura, name="insertar_venta"), 

    path('detalle_pedido/<id_pedido>/', detalle_pedido, name="detalle_pedido"),

    path('reportes/', reportes, name="reportes"), 

    path('detalle_pedido_cliente/<id_pedido>/', detalle_pedido_cliente, name="detalle_pedido_cliente"), 

    path('imprimir_detalle_boleta/<id>/', imprimir_detalle_boleta, name="imprimir_detalle_boleta"),
    path('imprimir_detalle_factura/<id>/', imprimir_detalle_factura, name="imprimir_detalle_factura"), 

    path('detalle_filtro_producto/<tipo>/', detalle_filtro_producto, name="detalle_filtro_producto")


]
