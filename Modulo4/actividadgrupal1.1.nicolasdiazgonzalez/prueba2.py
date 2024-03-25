import datetime

# clase producto
class producto:
    def __init__(self, sku, nombre, categoria, proveedor, stock, precio):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor = proveedor
        self.stock = stock
        self.precio = precio
        self.impuesto = 1.19

    def precio_impuesto(self):
        return self.precio * self.impuesto

# clase cliente
class cliente:
    def __init__(self, id_cliente, nombre, apellido, correo, saldo_inicial=0):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fecha_registro = datetime.datetime.now()
        self.__saldo = saldo_inicial

    def agregar_saldo(self, cantidad):
        self.__saldo += cantidad

    def mostrar_saldo(self):
        return self.__saldo

# clase vendedor
class vendedor:
    def __init__(self, run, nombre, apellido, seccion, comision=0.05):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = comision

    def calcular_comision(self, monto_venta):
        return monto_venta * self.__comision

    def agregar_comision(self, monto_comision):
        self.__comision += monto_comision

class elemento_venta:
    def __init__(self, sku, nombre, precio, unidades):
        self.sku = sku
        self.nombre = nombre
        self.precio = precio
        self.unidades = unidades
        self.totalsinimpuestos = self.precio * self.unidades
        self.totalconimpuestos = self.precio * self.unidades * producto.impuesto

        

# clase bodega
# revisado, solo se usaron tres funciones de la actgru6 modulo3 y funciona bien :)
class bodega:
    def __init__(self):
        self.stock = {
            'ef236b72': producto('ef236b72', 'zapatillas', 'Calzado', 'FabricanteX', 20, 30.0),
            'eb873cb8': producto('eb873cb8', 'poleras', 'Ropa', 'Fabricante1', 10, 15.0),
            'd84b9204': producto('d84b9204', 'zapatos', 'Calzado', 'Fabricante2', 15, 25.0),
            'b4d38db0': producto('b4d38db0', 'poleron', 'Ropa', 'Fabricante3', 3, 40.0),
            '0a5e85c5': producto('0a5e85c5', 'chaqueta', 'Ropa', 'Fabricante4', 5, 50.0),
            'd28e3788': producto('d28e3788', 'guantes', 'Accesorio', 'Fabricante5', 4, 10.0)
        }

    def agregar_producto(self, producto):
        if producto.sku not in self.stock:
            self.stock[producto.sku] = producto
        else:
            return 'El producto ya existe en la bodega, utilizar ACTUALIZAR STOCK'

    def actualizar_stock(self, sku, cantidad):
        if sku in self.stock:
            self.stock[sku].stock += cantidad
        else:
            print("El producto no existe en la bodega, utilizar AGREGAR PRODUCTO.")

    def lista_productos(self):
        for sku, producto in self.stock.items():
            print(f"SKU: {sku}, Nombre: {producto.nombre}, Stock: {producto.stock}, Proveedor: {producto.proveedor}, Precio: ${producto.precio}")

# clase controlventas
class controlventas:
    def __init__(self, bodega):
        self.bodega = bodega
        self.ventas = {}
        self.cliente = {
            '3b64e7': cliente('3b64e7', 'Juan', 'Pérez', 'juan@example.com', 0),
            '9a2c8f': cliente('9a2c8f', 'Maria', 'González', 'maria@example.com', 0),
            '1d9b5e': cliente('1d9b5e', 'Carlos', 'Rodríguez', 'carlos@example.com', 0),
            '7f6a2d': cliente('7f6a2d', 'Ana', 'Martínez', 'ana@example.com', 0),
            '5e8c1f': cliente('5e8c1f', 'Pedro', 'López', 'pedro@example.com', 0),
            '4d3b9a': cliente('4d3b9a', 'Sofía', 'Díaz', 'sofia@example.com', 0),
            '8c2e1d': cliente('8c2e1d', 'Luis', 'Fernández', 'luis@example.com', 0)
        }

    #Venta completa para que el menu se vea mas pulcro sin tantos print, generamos la pantalla completa aqui con los inputs :)
    def realizar_venta(self, clientes, vendedores, productos, carrito):
        print("----- REALIZAR VENTA -----")

        # Y solicitamos el RUN del vendedor

        run = input("Ingrese el RUN del vendedor: ")

        if run in vendedores:
            print('RUN para vendedor existente')
        else:
            print('RUN no existente, pruebe nuevamente')
            return
        
        # solicitar información del cliente
        id_clienteventa = input("Ingrese el ID del cliente: ")
        nombre_clienteventa = input("Ingrese el nombre del cliente: ")
        apellido_clienteventa = input("Ingrese el apellido del cliente: ")
        while True:
            #instanciamos clienteventa
            clienteventa = cliente(id_cliente=id_clienteventa, nombre_cliente=nombre_clienteventa, apellido_cliente=apellido_clienteventa)
        
            # y buscamos si exsite
            if clienteventa in clientes.values():
                # mostrar lista de productos disponibles en la bodega, como son pocos los imprimimos para que la lista de productos este a la vista con sus sku

                print("productos disponibles:")
                bodega.lista_productos()        

                #si exsite, empezamos generando un carrito con el id del cliente y una diccionario donde el primer elemento sera el total de la compra donde sumaremos el total.
                if carrito[clienteventa.id_cliente]:
                    pass
                else:
                    carrito[clienteventa.id_cliente]={}
                while True:
                        sku_producto = input("Ingrese el SKU del producto (o ingrese 'salir' para terminar compra): \n")
                        unidadesventa = int(input("Ingrese el numero de unidades: \n") or 1)
                        if sku_producto.lower() == "salir":
                            break
                        if sku_producto not in bodega.stock:
                            print("El producto no existe en la bodega.\n")
                            continue
                        productoventa = elemento_venta(bodega.stock.sku_producto)
                        if productoventa.stock < unidadesventa:
                            print("No hay suficiente stock de ese producto.\n")
                            continue

                        producto_venta = elemento_venta(bodega.stock.sku_producto.sku, bodega.stock.sku_producto.nombre, bodega.stock.sku_producto.precio, unidades = unidadesventa)

                        if producto_venta.sku in carrito.values():
                            carrito[clienteventa.id_cliente][producto_venta.sku].unidades + unidadesventa
                        else:
                            carrito[clienteventa.id_cliente][producto_venta.sku] = producto_venta
                break
            else:
                print('Cliente no encontrado, intente nuevamente')

            print('===== DETALLE =====')
            print(f'{elemento}: {valor}\n' for elemento, valor in carrito[clienteventa.id_cliente].items())
            confirmacion_venta = input('Desea confirmar la compra (Si/No): ').lower()
            if confirmacion_venta == 'si':
                total_venta = sum(producto.totalconimpuestos for producto in carrito[clienteventa.id_cliente].values())
                comision_vendedor = vendedor.calcular_comision(total_venta)
                vendedor.agregar_comision(comision_vendedor)
                for producto in carrito[clienteventa.id_cliente].values():
                    bodega.actualizar_stock(producto.sku, -producto.unidades)
            elif confirmacion_venta == 'no':
                #adiosito y no se hace nada
                break













        for producto in productos:
            self.bodega.actualizar_stock(producto.sku, -1)
        self.ventas.append({"cliente": cliente, "vendedor": vendedor, "productos": productos, "monto_total": total_venta})

    def generar_boleta(self, venta):
        cliente = venta["cliente"]
        vendedor = venta["vendedor"]
        productos = venta["productos"]
        monto_total = venta["monto_total"]
        impuesto_total = sum(producto.precio_impuesto() - producto.precio for producto in productos)
        print("===== BOLETA DE VENTA =====")
        print(f"cliente: {cliente.nombre} {cliente.apellido}")
        print(f"vendedor: {vendedor.nombre} {vendedor.apellido}")
        print("productos:")
        for producto in productos:
            print(f"- {producto.nombre}: Precio: ${producto.precio}, Impuesto: ${producto.precio_impuesto() - producto.precio}")
        print(f"Total (sin impuestos): ${monto_total}")
        print(f"Impuesto Total: ${impuesto_total}")
        print(f"Monto Total (con impuestos): ${monto_total + impuesto_total}")
        print("============================")

# Función para mostrar menú principal
def menu_principal():
    print("===== MENÚ PRINCIPAL =====")
    print("1. Gestionar bodega")
    print("2. Gestionar clientes")
    print("3. Gestionar vendedores")
    print("4. Realizar Venta")
    print("5. Mostrar Ventas Realizadas")
    print("6. Salir")
    print("===========================")

# Función para gestionar la bodega
def gestionar_bodega(bodega):
    print("===== GESTIÓN DE bodega =====")
    while True:
        print("1. Agregar producto")
        print("2. Actualizar Stock")
        print("3. Listar productos")
        print("4. Volver al Menú Principal")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            sku = input("Ingrese el SKU del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            categoria = input("Ingrese la categoría del producto: ")
            proveedor = input("Ingrese el proveedor del producto: ")
            stock = int(input("Ingrese el stock inicial del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto_nuevo = producto(sku, nombre, categoria, proveedor, stock, precio)
            bodega.agregar_producto(producto_nuevo)
            print("producto agregado exitosamente.")
        elif opcion == "2":
            sku = input("Ingrese el SKU del producto: ")
            cantidad = int(input("Ingrese la cantidad a actualizar (positiva o negativa): "))
            bodega.actualizar_stock(sku, cantidad)
        elif opcion == "3":
            bodega.lista_productos()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Función para gestionar clientes
def gestionar_clientes(clientes):
    while True:
        print("===== GESTIÓN DE clienteS =====")
        print("1. Agregar cliente")
        print("2. Mostrar clientes Registrados")
        print("3. Mostrar Saldo de cliente")
        print("4. Volver al Menú Principal")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            id_cliente = input("Ingrese el ID del cliente: ")
            nombre = input("Ingrese el nombre del cliente: ")
            apellido = input("Ingrese el apellido del cliente: ")
            correo = input("Ingrese el correo del cliente: ")
            saldo = float(input("Ingrese el saldo inicial del cliente: "))
            cliente = cliente(id_cliente, nombre, apellido, correo, saldo)
            clientes.append(cliente)
            print("cliente agregado exitosamente.")
        elif opcion == "2":
            if clientes:
                print("clientes Registrados:")
                for cliente in clientes:
                    print(f"ID: {cliente.id_cliente}, Nombre: {cliente.nombre} {cliente.apellido}, Correo: {cliente.correo}")
            else:
                print("No hay clientes registrados.")
        elif opcion == "3":
            id_busqueda = input("Ingrese el ID del cliente para mostrar su saldo: ")
            encontrado = False
            for cliente in clientes:
                if cliente.id_cliente == id_busqueda:
                    print(f"El saldo del cliente {cliente.nombre} {cliente.apellido} es: {cliente.mostrar_saldo()}")
                    encontrado = True
                    break
            if not encontrado:
                print("cliente no encontrado.")
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Función para gestionar vendedores
def gestionar_vendedores(vendedores):
    while True:
        print("===== GESTIÓN DE vendedorES =====")
        print("1. Agregar vendedor")
        print("2. Mostrar vendedores Registrados")
        print("3. Calcular Comisión de vendedor")
        print("4. Volver al Menú Principal")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            run = input("Ingrese el RUN del vendedor: ")
            nombre = input("Ingrese el nombre del vendedor: ")
            apellido = input("Ingrese el apellido del vendedor: ")
            seccion = input("Ingrese la sección del vendedor: ")
            comision = float(input("Ingrese la comisión del vendedor (opcional, presione Enter para 0.05): ") or 0.05)
            vendedor = vendedor(run, nombre, apellido, seccion, comision)
            vendedores.append(vendedor)
            print("vendedor agregado exitosamente.")
        elif opcion == "2":
            if vendedores:
                print("vendedores Registrados:")
                for vendedor in vendedores:
                    print(f"RUN: {vendedor.run}, Nombre: {vendedor.nombre} {vendedor.apellido}, Sección: {vendedor.seccion}")
            else:
                print("No hay vendedores registrados.")
        elif opcion == "3":
            run_busqueda = input("Ingrese el RUN del vendedor para calcular su comisión: ")
            encontrado = False
            for vendedor in vendedores:
                if vendedor.run == run_busqueda:
                    monto_venta = float(input("Ingrese el monto de la venta: "))
                    comision_calculada = vendedor.calcular_comision(monto_venta)
                    print(f"La comisión del vendedor {vendedor.nombre} {vendedor.apellido} es: {comision_calculada}")
                    encontrado = True
                    break
            if not encontrado:
                print("vendedor no encontrado.")
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")



# Función para mostrar las ventas realizadas
def mostrar_ventas_realizadas(control_ventas):
    print("===== VENTAS REALIZADAS =====")
    for i, venta in enumerate(control_ventas.ventas, start=1):
        print(f"Venta {i}:")
        control_ventas.generar_boleta(venta)
        print()

# Función principal para el menú
def main():
    clientes = {}  # Lista para almacenar los objetos cliente
    vendedores = {}  # Lista para almacenar los objetos vendedor
    carrito = {}
    
    labodega = bodega()  # Instancia de la bodega
    control_ventas = controlventas(bodega)  # Instancia del control de ventas

    while True:
        # Mostrar menú principal
        menu_principal()
        
        # Solicitar opción al usuario
        opcion = input("Ingrese una opción: ")
        
        # Ejecutar la opción seleccionada
        if opcion == "1":
                        gestionar_bodega(labodega)
        elif opcion == "2":
            gestionar_clientes(clientes)
        elif opcion == "3":
            gestionar_vendedores(vendedores)
        elif opcion == "4":
            realizar_venta(control_ventas, labodega, clientes, vendedores)
        elif opcion == "5":
            mostrar_ventas_realizadas(control_ventas)
        elif opcion == "6":
            print("Gracias por utilizar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()


