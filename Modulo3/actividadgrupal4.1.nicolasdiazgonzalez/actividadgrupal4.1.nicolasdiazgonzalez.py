import random, time

stock = {'producto1': 120, 'producto2': 150}
proveedormaximo = 0
def compra(stock):
    producto = random.choice(list(stock.keys()))
    n = random.randint(1,10)
    if n <= stock[producto] and stock[producto] > 0 :
        stock[producto] -= n
        print(f'Se compro {n} unidades de {producto}')
    else:
        print(f"No es posible realizar la venta de {n} unidades de {producto} debido a la falta de stock")
    return

def proveedor(stock, proveedormaximo):
    for llave, valor in stock.items():
        if proveedormaximo == 150:
            return
        elif (valor < 100) and (proveedormaximo < 150):
            stock[llave] += 50
            proveedormaximo += 50
            print(f'Se abastecio de 50 unidades de {llave}')
            return
compras = 0
while compras != 10:
     proveedor(stock, proveedormaximo)
     compra(stock)
     compras += 1
     time.sleep(3)
     if compras == 10:
         print(f'{''.join((f'- {valor} unidades de {llave}' for llave, valor in stock.items()))}')
         compras = 0
