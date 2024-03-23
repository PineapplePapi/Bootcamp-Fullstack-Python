# Creamos la clase bodega donde en su init estaran los productos en una lista con su stock disponible y se le anadiran las funciones correspondientes a la bodega

class bodega:

    def __init__(self):

        self.__stock__ = {
            'ef236b72': {'producto': 'zapatillas', 'cantidad': 20},
            'eb873cb8': {'producto': 'poleras', 'cantidad': 10},
            'd84b9204': {'producto': 'zapatos', 'cantidad': 15},
            'b4d38db0': {'producto': 'poleron', 'cantidad': 3},
            '0a5e85c5': {'producto': 'chaqueta', 'cantidad': 5},
            'd28e3788': {'producto': 'guantes', 'cantidad': 4}
        }

    def agregar_producto(self, id_producto, producto, cantidad):
        # Primero comprobaremos si existe, en ese caso se suma la cantidad a la ya existente, y si no existe, la creamos.
        if id_producto not in self.__stock__:
            # Anadimos cantidades
            self.__stock__[id_producto] = {'producto': producto, 'cantidad': cantidad}
        else:
            # Si existe, indicamos que ya existen y tiene que actualizar stock
            return 'El producto ya existe, utiliza ACTUALIZAR STOCK'

    def actualizar_stock(self, id_producto, cantidad):
        #Comprobamos que exista y si existe, podremos actualizar stock con numero positivos y negativos
        if id_producto in self.__stock__:
            self.__stock__[id_producto]['cantidad'] += cantidad
        else:
            #Si el producoto no existe, debemos agregarlo con agregar_producto
            return 'El producto no existe, utiliza AGREGAR PRODUCTOS'

    def stock_completo(self):
        #Simplemente retornamos stock completo y lo imprimimos
        return self.__stock__

    def stock_unidad(self, id_producto):
        #Si el producto existe en stock con su ID, devolvemos la cantidad del producto.
        if id_producto in self.__stock__:
            return self.__stock__[id_producto]['cantidad']
        else:
            #Si no existe, devolvemos la informacion
            return f'El producto con ID {id_producto} no existe'

    def stock_solonombres(self):
        #Retornamos el stock solo con los nombres
        return [self.__stock__[id_producto]['producto'] for id_producto in self.__stock__]

    def stock_masunidades(self, cantidad):
        #Retornamos los productos con mas unidades de la indicada
        return [self.__stock__[id_producto]['producto'] for id_producto, info in self.__stock__.items() if info['cantidad'] > cantidad]
#Creamos la clase control_ventas, donde manjaremos la lista de clientes, la bodega y el carrito con los ids asociados
class control_ventas:

    def __init__(self, bodega):
        self.__bodega__ = bodega
        self.__cliente__ = {
            '3b64e7': {'nombre': 'Juan', 'edad': 30},
            '9a2c8f': {'nombre': 'Maria', 'edad': 25},
            '1d9b5e': {'nombre': 'Carlos', 'edad': 35},
            '7f6a2d': {'nombre': 'Ana', 'edad': 28},
            '5e8c1f': {'nombre': 'Pedro', 'edad': 40},
            '4d3b9a': {'nombre': 'Sofia', 'edad': 22},
            '8c2e1d': {'nombre': 'Luis', 'edad': 33}
        }
        self.__carrito__ = {}

    def printclientes(self):
        #Si existen clientes registrados, los retornamos
        if self.__cliente__:
            clientes = len(self.__cliente__.keys())
            return f'Existen {clientes} registrados'
        else:
            #Si no existen, avisamos que no existen clientes registrados
            return 'No existen clientes registrados'

    def compra(self, id_cliente, id_producto, unidades=1):#Agregamos 1 porque es el minimo por requerimiento, aunque se puede cambiar.
        #Si existe el ID del cliente
        if id_cliente in self.__cliente__:
            #Instanciamos el stock en una variable utilizando la funcion stock_unidad() con el id del producto en self.bodega
            stock_disponible = self.__bodega__.stock_unidad(id_producto)
            #Si el stock_disponible existe y es igual o mayor a las unidades pedidas
            if stock_disponible is not None and stock_disponible >= unidades:
                #Si rl ID esta en el carrito, osea, si ya agrego otro producto
                if id_cliente in self.__carrito__:
                    #Agregamos al carrito con el ID del cliente y el ID del prodcuto mediante un get las unidades del producto
                    self.__carrito__[id_cliente][id_producto] = self.__carrito__[id_cliente].get(id_producto, 0) + unidades
                else:
                    #Si ya existia el carrito con el ID del cliente, agregamos el producto con las unidades al carrito diccionario
                    self.__carrito__[id_cliente] = {id_producto: unidades}
                #Por ultimo actualizamo el stock con la funcion actualizar_stock
                self.__bodega__.actualizar_stock(id_producto, -unidades)
                #y retornamos un compra aprobada y en camino por requerimiento
                return 'Compra aprobada y en camino'
            else:
                #Si no existe un stock_disponible o las unidades son mayores al stock_disponible, se retorna una compra cancelada
                return 'Compra cancelada'
        else:
            #Si no existe el ID, avisamos que no esta registrado
            return f'El cliente con ID {id_cliente} no esta registrado.'
    #Creamo la funcion carrito y la hacemos property, con la finalidad de que se pueda usar en otras funciones, en este caso para imprimir_carrito
    @property
    def carrito(self):
        return self.__carrito__
        

def imprimir_carrito(carrito):
    #Si el carrito esta vacio, lo imprimimos
    if not carrito:
        print('El carrito está vacío.')
    #Si el carrito no esta vacio, imprimimos los elementos asociados por ids de clientes.
    else:
        print('Contenido del carrito:')
        for id_cliente, productos in carrito.items():
            print(f'Cliente {id_cliente}:\n')
            for id_producto, unidades in productos.items():
                print(f'  Producto {id_producto}: {unidades} unidades\n')

#Creamos la clase usuario, el que tendra como funciones, imprimir sus datos, comprarusuario() el que nos lleva a la clase control_venta para poder usar compra() con compra_usuario e imprimir_carrito() con imprimir_carrito_usuario()
class usuario:
    def __init__(self, nombre, correo, id_usuario):
        self.nombre = nombre
        self.corre = correo
        self.id_usuario = id_usuario
    
    def informacion(self):
        return f"Nombre: {self.nombre}, Correo: {self.correo}"
    
    def compra_usuario(self, id_cliente, id_producto, unidades):
        return control_ventas.compra(self, id_cliente, id_producto, unidades)
    
    def imprimir_carrito_usuario(self, carrito):
        return imprimir_carrito(carrito)

#Creamos la clase vendedor que hereda usuario, por lo que podra hacer utilizar las mismas funciones, ademas podra actualizar el stock, consultar stock por producto, consultar el stock en lista con solo los nombres y stock con mas de la unidad seleccionada
class vendedor(usuario):
    def __init__(self, nombre, correo, id_usuario):
        super().__init__(nombre, correo, id_usuario)

    def actualizar_stockvendedor(self, bodega, id_producto, cantidad):
        bodega.actualizar_stock(id_producto, cantidad)

    def stock_unidadvendedor(self, bodega, id_producto):
        return bodega.stock_unidad(id_producto)

    def stock_solonombresvendedor(self, bodega):
        return bodega.stock_solonombres()

    def stock_masunidadesvendedor(self, bodega, cantidad):
        return bodega.stock_masunidades(cantidad)

#Creamos la clase admin que hereda vendedor, bodega y control_ventas, por lo que puede hacer uso de todos los metodos que hay en las respectivas clases.    
class admin(vendedor, bodega, control_ventas):
    def __init__(self, nombre, correo, id_usuario):
        super().__init__(nombre, correo, id_usuario)




