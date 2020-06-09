//Variables

const carrito = document.getElementById('carrito');
const productos = document.getElementById('lista-productos');

const lista_productos_carrito = document.querySelector('#lista-carrito tbody'); 

const vaciarCarritoBtn = document.getElementById('vaciar-carrito'); 

//Listeners

cargarEventListeners(); 

console.log(productos)

function cargarEventListeners(){

    productos.addEventListener('click', comprarProducto); 

    //Cuando se elimina un producto del carrito
    carrito.addEventListener('click', eliminarProductoDeCarrito);

    //Vacias Carrito
    vaciarCarritoBtn.addEventListener('click', vaciarCarrito);

    //Al cargar el documento, mostrar productos desde locals
    document.addEventListener('DOMContentLoaded', leerLocalStorage)

}

//Funciones


//funcion que anade el producto al carrito
function comprarProducto(e){
    e.preventDefault();

    //Delegation para agregar-carrito
    if(e.target.classList.contains('agregar-carrito')){
        const producto = e.target.parentElement;

        leerDatosProducto(producto);
    }
}

function leerDatosProducto(producto){

    const infoProducto = {
        imagen: producto.querySelector('img').src, 
        nombre_producto: producto.querySelector('.nombre_prod').textContent, 
        id_producto : producto.querySelector('.id_prod').textContent, 
        stock_producto: producto.querySelector('.stock_prod').textContent, 
        precio_producto: producto.querySelector('.precio_prod').textContent
    }


    insertarProductoAlCarrito(infoProducto);
}

function insertarProductoAlCarrito(infoProducto){
    const row = document.createElement('tr');

    row.innerHTML = `
        <td> <img src="${infoProducto.imagen}" width="70px">  </td>
        <td><small>${infoProducto.id_producto}</small></td>
        <td><small>${infoProducto.nombre_producto}</small></td>
        <td><small>${infoProducto.precio_producto}</small></td>
        <td>
            <a href="#" class="borrar-curso-carrito" data-id="${infoProducto.id_producto}">X</a>
        </td>
        <td></td>
    `;

    lista_productos_carrito.appendChild(row);

    //Guardar en localstorage

    guardarProductoLocalStorage(infoProducto);
}


//Elimina Curso de carrito

function eliminarProductoDeCarrito(e){
    e.preventDefault();

    let producto, productoId;

    if(e.target.classList.contains('borrar-curso-carrito')){
       e.target.parentElement.parentElement.remove();
       producto = e.target.parentElement.parentElement;
       productoId = producto.querySelector('a').getAttribute('data-id');
    }

    eliminarProductoLocalStorage(productoId)
}

//Vaciar Carrito

function vaciarCarrito(e){

    while(lista_productos_carrito.firstChild){
        lista_productos_carrito.removeChild(lista_productos_carrito.firstChild);
    }

    return false;
}

//guardar en ls

function guardarProductoLocalStorage(infoProducto){
    let productos;

    productos = obtenerProductosLocalStorage();
    productos.push(infoProducto);

    //El producto seleccionado se agrega a locals
    localStorage.setItem('productos', JSON.stringify(productos))
}


//Comprueba que haya elementos en locals
function obtenerProductosLocalStorage(){
    let productos_localStorage; 

    //Comprobar si hay algo en locals

    if(localStorage.getItem('productos') === null){
        productos_localStorage = []
    }else{
        productos_localStorage = JSON.parse( localStorage.getItem('productos') );
    }

    return productos_localStorage;
}


//mostrar productos desde locals
function leerLocalStorage(){
    let productosLocalStorage; 

    productosLocalStorage = obtenerProductosLocalStorage();

    productosLocalStorage.forEach(infoProducto => {
        const row = document.createElement('tr');

        row.innerHTML = `
            <td> <img src="${infoProducto.imagen}" width="70px">  </td>
            <td><small>${infoProducto.id_producto}</small></td>
            <td><small>${infoProducto.nombre_producto}</small></td>
            <td><small>${infoProducto.precio_producto}</small></td>
            <td>
                <a href="#" class="borrar-curso-carrito" data-id="${infoProducto.id_producto}">X</a>
            </td>
            <td></td>
        `;
    
        lista_productos_carrito.appendChild(row);
    });
}

//eliminar producto de locals

function eliminarProductoLocalStorage(producto_id){
    let productosLS; 

    productosLS = obtenerProductosLocalStorage();

    productosLS.forEach(function(productoLS, index) {
        if(productoLS.id_producto === producto_id){
            productosLS.splice(index, 1);
        }
    }); 

    localStorage.setItem('productos', JSON.stringify(productosLS) )
}