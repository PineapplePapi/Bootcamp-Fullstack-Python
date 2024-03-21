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
        #Comprobamos que exista y si existe, podremos actualizar stock
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
        if id_cliente in self.clientes:
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
        

#Instanciamos las clases a utilizar
labodega = bodega()
ventas = control_ventas(labodega)
#Menu principal
def menu():
    while True:
        print('Menu Principal\n')
        print('1. Gestionar Bodega\n')
        print('2. Gestionar Ventas\n')
        print('0. Salir\n')
        eleccion = input('Ingrese una opcion: ')
        if eleccion == '1':
            #Ingresamos al menu bodega
            menu_bodega()
        elif eleccion == '2':
            #Ingresamos al menu ventas
            menu_ventas()
        elif eleccion == '0':
            break
        else:
            print('Opcion invalida. Intente nuevamente.')

def menu_bodega():
    while True:
        #Acciones requerimientos del ejercicio
        print('\nMenu de Bodega:')
        print('1. Agregar producto\n')
        print('2. Actualizar stock\n')
        print('3. Ver stock completo\n')
        print('4. Ver stock de un producto\n')
        print('5. Ver solo nombres de productos\n')
        print('6. Ver productos con mas de X unidades\n')
        print('0. Volver al menu principal\n')
        eleccion = input('Ingrese una opcion: ')

        if eleccion == '1':
            #Para agregar producto, pedimos los datos requeridos, id producto, producto y cantidad
            id_producto = input('Ingrese el ID del producto: \n')
            producto = input('Ingrese el nombre del producto: \n')
            cantidad = int(input('Ingrese la cantidad: \n'))
            #En la variable instanciada, llamamos a la funcion agregar_producto e ingresamos los datos pedidos
            labodega.agregar_producto(id_producto, producto, cantidad)
        elif eleccion == '2':
            #Para actualizar stock, pedimos los datos requeridos, ID y cantidad
            id_producto = input('Ingrese el ID del producto: \n')
            cantidad = int(input('Ingrese la cantidad a actualizar: \n'))
            #A la variable instanciada, le anadimos la funcion actualizar_stock con los inputs pedidos.
            labodega.actualizar_stock(id_producto, cantidad)
        elif eleccion == '3':
            #Imprimimos la bodega completa con la variable instanciada y la funcion stock_completo
            print(labodega.stock_completo())
        elif eleccion == '4':
            #Para ver el stock de un producto, solicitamos el ID
            id_producto = input('Ingrese el ID del producto: \n')
            #Imprimimos el stock del produco con la funcion stock_unidad en la variable instanciada
            print(labodega.stock_unidad(id_producto))
        elif eleccion == '5':
            #Imprimimos stock de solo los nombres de los productos con stock_solonombres
            print(labodega.stock_solonombres())
        elif eleccion == '6':
            #Para saber los productos con una cantidad minima de unidades, solicitamos las unidades
            cantidad = int(input('Ingrese la cantidad minima de unidades: \n'))
            #E imprimimos los productos con mas unidades que la ingresada con stock_masunidades
            print(labodega.stock_masunidades(cantidad))
        elif eleccion == '0':
            break
        else:
            print('Opcion invalida. Intente nuevamente.')

def menu_ventas():
    while True:
        print('\nMenu de Ventas:')
        print('1. Mostrar clientes registrados\n')
        print('2. Realizar compra\n')
        print('3. Imprimir carrito')
        print('0. Volver al menu principal\n')
        opcion = input('Ingrese una opcion: \n')

        if opcion == '1':
            #Hacemos un print de los clientes con printclientes en la variable instanciada 
            print(ventas.printclientes())
        elif opcion == '2':
            #Para realizar compras, solicitamos IDs de clientes, productos y cantidad, si no se ingresa una cantidad especifica, entonces es 1 unidad, por requerimiento del ejercicio
            id_cliente = input('Ingrese el ID del cliente: \n')
            id_producto = input('Ingrese el ID del producto: \n')
            unidades = int(input('Ingrese la cantidad de unidades (o presione Enter para 1): \n') or 1)
            #Hacemos un print con la variable instanciada y con los inputs requeridos
            print(ventas.compra(id_cliente, id_producto, unidades))
        elif opcion == '3':
            #Agregamos una opcion para imprimir el carrito con una funcion imprimir_carrito
            imprimir_carrito(ventas.carrito)
        elif opcion == '0':
            break
        else:
            print('Opcion invalida. Intente nuevamente.')

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


menu()