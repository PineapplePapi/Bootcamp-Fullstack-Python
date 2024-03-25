import datetime

# Clase Cliente
class Cliente:
    def __init__(self, id_cliente, nombre, apellido, correo):
        self.ID_Cliente = id_cliente
        self.Nombre = nombre
        self.Apellido = apellido
        self.Correo = correo
        self.Fecha_Registro = datetime.datetime.now()
        self.__Saldo = 0.0

    def agregar_saldo(self, cantidad):
        self.__Saldo += cantidad

    def mostrar_saldo(self):
        return self.__Saldo

# Clase Producto
class Producto:
    def __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto):
        self.SKU = sku
        self.Nombre = nombre
        self.Categoría = categoria
        self.Proveedor = proveedor
        self.Stock = stock
        self.Valor_Neto = valor_neto
        self.__Impuesto = 1.19

# Clase Vendedor
class Vendedor:
    def __init__(self, run, nombre, apellido, seccion):
        self.RUN = run
        self.Nombre = nombre
        self.Apellido = apellido
        self.Sección = seccion
        self.__Comision = 0.0

# Clase Bodega
class Bodega:
    def __init__(self):
        self.__stock__ = {
            'ef236b72': Producto('ef236b72', 'zapatillas', 'Calzado', 'FabricanteX', 20, 30.0),
            'eb873cb8': Producto('eb873cb8', 'poleras', 'Ropa', 'FabricanteY', 10, 15.0),
            'd84b9204': Producto('d84b9204', 'zapatos', 'Calzado', 'FabricanteZ', 15, 25.0),
            'b4d38db0': Producto('b4d38db0', 'poleron', 'Ropa', 'FabricanteX', 3, 40.0),
            '0a5e85c5': Producto('0a5e85c5', 'chaqueta', 'Ropa', 'FabricanteY', 5, 50.0),
            'd28e3788': Producto('d28e3788', 'guantes', 'Accesorio', 'FabricanteZ', 4, 10.0)
        }

    def agregar_producto(self, id_producto, producto, cantidad):
        if id_producto not in self.__stock__:
            self.__stock__[id_producto] = Producto(id_producto, producto, '', '', cantidad, 0.0)
        else:
            return 'El producto ya existe, utiliza ACTUALIZAR STOCK'

    def actualizar_stock(self, id_producto, cantidad):
        if id_producto in self.__stock__:
            self.__stock__[id_producto].Stock += cantidad
        else:
            return 'El producto no existe, utiliza AGREGAR PRODUCTOS'

    def stock_completo(self):
        return {id_producto: vars(producto) for id_producto, producto in self.__stock__.items()}

    def stock_unidad(self, id_producto):
        if id_producto in self.__stock__:
            return self.__stock__[id_producto].Stock
        else:
            return f'El producto con ID {id_producto} no existe'

    def stock_solonombres(self):
        return [producto.Nombre for producto in self.__stock__.values()]

    def stock_masunidades(self, cantidad):
        return [producto.Nombre for producto in self.__stock__.values() if producto.Stock > cantidad]

# Clase ControlVentas
class ControlVentas:
    def __init__(self, bodega):
        self.__bodega__ = bodega
        self.__clientes__ = {
            '3b64e7': Cliente('3b64e7', 'Juan', 'Pérez', 'juan@example.com'),
            '9a2c8f': Cliente('9a2c8f', 'Maria', 'González', 'maria@example.com'),
            '1d9b5e': Cliente('1d9b5e', 'Carlos', 'Rodríguez', 'carlos@example.com'),
            '7f6a2d': Cliente('7f6a2d', 'Ana', 'Martínez', 'ana@example.com'),
            '5e8c1f': Cliente('5e8c1f', 'Pedro', 'López', 'pedro@example.com'),
            '4d3b9a': Cliente('4d3b9a', 'Sofía', 'Díaz', 'sofia@example.com'),
            '8c2e1d': Cliente('8c2e1d', 'Luis', 'Fernández', 'luis@example.com')
        }
        self.__carrito__ = {}
        self.__vendedores__ = {
            '12345': Vendedor('12345', 'Juan', 'Pérez', 'Calzado'),
            '54321': Vendedor('54321', 'María', 'González', 'Ropa')
        }

    def print_clientes(self):
        if self.__clientes__:
            clientes = len(self.__clientes__)
            return f'Existen {clientes} clientes registrados'
        else:
            return 'No existen clientes registrados'

    def agregar_saldo_cliente(self, id_cliente, cantidad):
        if id_cliente in self.__clientes__:
            self.__clientes__[id_cliente].agregar_saldo(cantidad)
            return f'Saldo agregado correctamente. Nuevo saldo: {self.__clientes__[id_cliente].mostrar_saldo()}'
        else:
            return f'El cliente con ID {id_cliente} no está registrado.'

    def mostrar_saldo_cliente(self, id_cliente):
        if id_cliente in self.__clientes__:
            return f'Saldo del cliente {self.__clientes__[id_cliente].mostrar_saldo()}'
        else:
            return f'El cliente con ID {id_cliente} no está registrado.'

    def realizar_venta(self, id_cliente, id_producto, unidades=1):
        if id_cliente in self.__clientes__:
            stock_disponible = self.__bodega__.stock_unidad(id_producto)
            if stock_disponible is not None and stock_disponible >= unidades:
                if id_cliente in self.__carrito__:
                    self.__carrito__[id_cliente][id_producto] = self.__carrito__[id_cliente].get(id_producto, 0) + unidades
                else:
                    self.__carrito__[id_cliente] = {id_producto: unidades}
                self.__bodega__.actualizar_stock(id_producto, -unidades)
                # Asignar la venta al vendedor
                if id_producto in self.__bodega__.__stock__:
                    sku_vendedor = self.__bodega__.__stock__[id_producto].Proveedor
                    if sku_vendedor in self.__vendedores__:
                        self.__vendedores__[sku_vendedor].__Comision += (self.__bodega__.__stock__[id_producto].Valor_Neto * unidades * 0.1)
                return 'Venta realizada con éxito'
            else:
                return 'Venta cancelada: stock insuficiente'
        else:
            return f'El cliente con ID {id_cliente} no está registrado.'

    def mostrar_comision_vendedor(self, sku_vendedor):
        if sku_vendedor in self.__vendedores__:
            return f'Comisión del vendedor: {self.__vendedores__[sku_vendedor].__Comision}'
        else:
            return 'Vendedor no encontrado'

    @property
    def carrito(self):
        return self.__carrito__

def imprimir_carrito(carrito):
    if not carrito:
        print('El carrito está vacío.')
    else:
        print('Contenido del carrito:')
        for id_cliente, productos in carrito.items():
            print(f'Cliente {id_cliente}:\n')
            for id_producto, unidades in productos.items():
                print(f'  Producto {id_producto}: {unidades} unidades\n')

# Instanciamos las clases
labodega = Bodega()
ventas = ControlVentas(labodega)

# Menú principal
def menu():
    while True:
        print('Menu Principal\n')
        print('1. Gestionar Bodega\n')
        print('2. Gestionar Ventas\n')
        print('0. Salir\n')
        eleccion = input('Ingrese una opción: ')
        if eleccion == '1':
            menu_bodega()
        elif eleccion == '2':
             menu_ventas()
        elif eleccion == '0':
            break
        else:
            print('Opción inválida. Intente nuevamente.')

def menu_bodega():
    while True:
        print('\nMenu de Bodega:')
        print('1. Agregar producto\n')
        print('2. Actualizar stock\n')
        print('3. Ver stock completo\n')
        print('4. Ver stock de un producto\n')
        print('5. Ver solo nombres de productos\n')
        print('6. Ver productos con más de X unidades\n')
        print('0. Volver al menu principal\n')
        eleccion = input('Ingrese una opción: ')

        if eleccion == '1':
            id_producto = input('Ingrese el ID del producto: \n')
            producto = input('Ingrese el nombre del producto: \n')
            cantidad = int(input('Ingrese la cantidad: \n'))
            labodega.agregar_producto(id_producto, producto, cantidad)
        elif eleccion == '2':
            id_producto = input('Ingrese el ID del producto: \n')
            cantidad = int(input('Ingrese la cantidad a actualizar (positivo o negativo): \n'))
            labodega.actualizar_stock(id_producto, cantidad)
        elif eleccion == '3':
            print(labodega.stock_completo())
        elif eleccion == '4':
            id_producto = input('Ingrese el ID del producto: \n')
            print(labodega.stock_unidad(id_producto))
        elif eleccion == '5':
            print(labodega.stock_solonombres())
        elif eleccion == '6':
            cantidad = int(input('Ingrese la cantidad mínima de unidades: \n'))
            print(labodega.stock_masunidades(cantidad))
        elif eleccion == '0':
            break
        else:
            print('Opción inválida. Intente nuevamente.')

def menu_ventas():
    while True:
        print('\nMenu de Ventas:')
        print('1. Mostrar clientes registrados\n')
        print('2. Agregar saldo a cliente\n')
        print('3. Mostrar saldo de cliente\n')
        print('4. Realizar venta\n')
        print('5. Mostrar comisión de vendedor\n')
        print('6. Imprimir carrito\n')
        print('0. Volver al menu principal\n')
        opcion = input('Ingrese una opción: \n')

        if opcion == '1':
            print(ventas.print_clientes())
        elif opcion == '2':
            id_cliente = input('Ingrese el ID del cliente: \n')
            cantidad = float(input('Ingrese la cantidad a agregar: \n'))
            print(ventas.agregar_saldo_cliente(id_cliente, cantidad))
        elif opcion == '3':
            id_cliente = input('Ingrese el ID del cliente: \n')
            print(ventas.mostrar_saldo_cliente(id_cliente))
        elif opcion == '4':
            id_cliente = input('Ingrese el ID del cliente: \n')
            id_producto = input('Ingrese el ID del producto: \n')
            unidades = int(input('Ingrese la cantidad de unidades (o presione Enter para 1): \n') or 1)
            print(ventas.realizar_venta(id_cliente, id_producto, unidades))
        elif opcion == '5':
            sku_vendedor = input('Ingrese el SKU del vendedor: \n')
            print(ventas.mostrar_comision_vendedor(sku_vendedor))
        elif opcion == '6':
            imprimir_carrito(ventas.carrito)
        elif opcion == '0':
            break
        else:
            print('Opción inválida. Intente nuevamente.')

menu()
