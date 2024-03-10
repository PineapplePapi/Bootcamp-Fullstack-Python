# DESARROLLO
# Considerando los avances realizados en nuestro proyecto, se solicita crear y agregar sentencias que
# nos permitan manipular un stock de productos. Para ello debemos aplicar lo siguiente:
# - Definir el stock de un producto en una variable. La variable será un diccionario, asi podemos manejar varios items de productos en una misma variable.

productos = {'producto1': 20, 'producto2': 50, 'producto3': 15, 'producto4': 13 }
#podria ser en un txt para que no se borre :O

#En vez de producto1, producto2 etc. se podrian utilizar id's con numeros como el codigo de barra, además en los valores se podría asociar una lista, con el stock, vendidos, devueltos o cosas asi, mientras mas datos mejor

# - Definir una forma de solicitar el stock disponible del producto por consola. Definiremos una función stock() para poder solicitar el stock disponible. Pero antes, definiremos una función consulta() para determinar las distintas consultas que se puedan hacer y manipular el stock.

def consultas():
    while True:
        print()
        consulta = int(input('Ingrese el numero de la opción que desea realizar: \n\n1. Stock disponible de un producto. \n\n2. Solicitar unidades de un producto. \n\n0. Salir.\n\n'))
        print()
        if consulta == 1: stock(productos) #Probando en una sola linea :D
        elif consulta == 2: solicitar(productos)
        elif consulta ==0 : return

def stock(productos):
        while True:
            producto = int(input(f'Ingrese el numero del producto del cual desea saber su stock: \n\n{"\n".join((f'{index + 1}.{producto}' for index, producto in enumerate(productos.keys())) )} \nIngrese 0 para salir\n\n')) 
        # explicacion de {",\n".join( [f'{index + 1}.{producto}' for index, producto in enumerate(productos.keys())] )}, agregamos un .join al ",\n" para separar los elementos que queremos agregar, dentro del join añadimos el f'{index + 1}.{producto}' para añadir el index +1 del producto, cuyos elementos son lo que conseguimos al recorrer para index y producto en enumerate(productos.keys) que son los elementos keys del diccionario 'productos' enumerado en memoria por la funcion enumerate. Y todo esto para conseguir un diccionario imprimido(IMPRESO) de sus elementos keys con sus indices de posicion + 1 para que se vea bonito :) y para ocupar numeros :))))))) pero como no se puede buscar un key directamente con su index en un dict() porque no funciona un productos[1] o la posicion que sea, utilizaremos una lista :D y solucionaremos los numeros 0 y negativos para que sirvan de salida y otros mensajes, y asi vamos solucionando problemas sobre la marcha LOL solo para intentar utilizar el mayor numero de conceptos y sobre todo numeros en el menu :D.
            if producto == 0:
                    #Para salir
                    return
            elif producto < 0:
                    #Por si ponen un numero negativo
                    print()
                    print('Numero incorrecto, pruebe nuevamente.\n')
            elif producto > len(list(productos)):
                    #Por si ponen un numero mayor a los de la lista
                    print()
                    print('Producto no encontrado pruebe nuevamente o ingrese 0 para salir\n')
            else: 
                    #Numero correcto chin chin chin $$$$
                    productokey = list(productos.keys())[producto-1]
                    print()
                    print(f'{productos.get(productokey)} unidades de {productokey}\n')


# - Definir una forma de solicitar unidades del producto por consola. Este número de productos se
# almacenarán en una nueva variable llamada ‘Productos seleccionados’. Lo haremos con una función solicitar() dentro del menu consultas.
def solicitar(productos):
    while True:
            carritopedido = {}
          #utilizaremos el mismo tipo de input que en la función stock :)
            solicitud = int(input(f'Ingrese el numero del producto del cual desea stock: \n\n{"\n".join((f'{index + 1}.{producto}' for index, producto in enumerate(productos.keys())) )} \nIngrese 0 para salir\n\n'))

            if solicitud == 0:
                    #Para salir
                    return
            elif solicitud < 0:
                    #Por si ponen un numero negativo
                    print()
                    print('Numero incorrecto, pruebe nuevamente.\n')
            elif solicitud > len(list(productos)):
                    #Por si ponen un numero mayor a los de la lista
                    print()
                    print('Producto no encontrado pruebe nuevamente o ingrese 0 para salir\n')
            else: 
                print('vamos muy bien :D')
                #tengo que primero que verificar stock y entregarlo, preguntar cuantos desea y si desea 12 o mas, entregar +1, si no se puede, entregar el numero que desea. imprimir todo :D
                #no mas de 20 unidades en un pedido de todo.
                #si no hay stock, imprimirlo. todo en este else supongo :(

consultas()

# - Los productos reubicados serán descontados del stock inicial.
# - El programa debe verificar que existan unidades disponibles.
# - Al verificar las unidades disponibles, el programa entregará una unidad extra cuando se seleccionen
# más de 12 unidades. Verificar que el stock posibilite entregar una unidad extra. Sino se entregan las
# unidades justas. Cada una de las posibles acciones debe imprimir un mensaje explicando lo realizado.
# - No se pueden solicitar más de 20 unidades en un mismo pedido.
# - Si el valor ingresado es superior al stock disponible, este debe entregar un mensaje indicando que no
# es posible realizar esta acción debido a que no hay stock suficiente.
# El código debe estar debidamente comentado para asegurar su comprensión.
