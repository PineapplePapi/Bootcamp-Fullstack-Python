import random
import time

# Inicializar stock de productos
stock_producto_1 = 120
stock_producto_2 = 150

# Función para simular una compra
def simular_compra():
    global stock_producto_1, stock_producto_2
    producto = random.randint(1, 2)
    cantidad = random.randint(1, 10)
    print(f"Compra de {cantidad} unidades del producto {producto}")
    if producto == 1:
        if stock_producto_1 >= cantidad:
            stock_producto_1 -= cantidad
        else:
            print("¡No hay suficiente stock del producto 1!")
    else:
        if stock_producto_2 >= cantidad:
            stock_producto_2 -= cantidad
        else:
            print("¡No hay suficiente stock del producto 2!")

# Función para imprimir el stock actual
def imprimir_stock():
    print(f"Stock actual - Producto 1: {stock_producto_1}, Producto 2: {stock_producto_2}")

# Función para recibir suministros de los proveedores
def recibir_suministros():
    global stock_producto_1, stock_producto_2
    if stock_producto_1 < 100:
        suministro_1 = min(50, 150 - stock_producto_1)  # Verificar disponibilidad del proveedor
        stock_producto_1 += suministro_1
        print(f"Recibidos {suministro_1} unidades del producto 1 de los proveedores.")
    if stock_producto_2 < 100:
        suministro_2 = min(50, 150 - stock_producto_2)  # Verificar disponibilidad del proveedor
        stock_producto_2 += suministro_2
        print(f"Recibidos {suministro_2} unidades del producto 2 de los proveedores.")

# Simulación de compras y gestión de stock
compras_realizadas = 0
while True:
    simular_compra()
    compras_realizadas += 1
    if compras_realizadas % 10 == 0:
        imprimir_stock()
    recibir_suministros()
    time.sleep(3)  # Esperar 3 segundos entre cada compra simulada
