# Función para realizar una venta
def realizar_venta(control_ventas, bodega, cliente, vendedores):
    print("----- REALIZAR VENTA -----")
    # Mostrar lista de productos disponibles en la bodega
    print("productos disponibles:")
    bodega.lista_productos()
    
    # Solicitar el ID del vendedor
    id_vendedor = input("Ingrese el ID del vendedor: ")
    vendedor = None
    for v in vendedores:
        if v.run == id_vendedor:
            vendedor = v
            break

    # Solicitar información del cliente
    id_cliente = input("Ingrese el ID del cliente: ")
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    apellido_cliente = input("Ingrese el apellido del cliente: ")
    correo_cliente = input("Ingrese el correo del cliente: ")
    saldo_cliente = float(input("Ingrese el saldo del cliente: "))
    cliente = cliente(id_cliente, nombre_cliente, apellido_cliente, correo_cliente, saldo_cliente)
    
    # Solicitar productos a vender
    productos_venta = []
    while True:
        sku_producto = input("Ingrese el SKU del producto a vender (o 'fin' para terminar): ")
        if sku_producto.lower() == "fin":
            break
        if sku_producto not in bodega.stock:
            print("El producto no existe en la bodega.")
            continue
        producto = bodega.stock[sku_producto]
        if producto.stock <= 0:
            print("No hay suficiente stock de ese producto.")
            continue
        productos_venta.append(producto)
    
    
    # Realizar la venta si hay productos en el carrito y el vendedor es válido
    if productos_venta and vendedor:
        total_venta = sum(producto.precio for producto in productos_venta)
        comision = vendedor.calcular_comision(total_venta)
        cliente.agregar_saldo(-total_venta)
        vendedor.comision += comision
        for producto in productos_venta:
            bodega.actualizar_stock(producto.sku, -1)
        control_ventas.registrar_venta(cliente, productos_venta, total_venta)
        print("Venta realizada exitosamente.")
    else:
        print("No se ha agregado ningún producto al carrito o el vendedor no es válido.")