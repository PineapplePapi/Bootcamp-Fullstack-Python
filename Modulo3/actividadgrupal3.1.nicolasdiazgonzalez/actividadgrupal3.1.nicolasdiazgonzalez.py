# DESARROLLO
# Considerando los avances realizados en nuestro proyecto, se solicita crear y agregar sentencias que
# nos permitan manipular un stock de productos. Para ello debemos aplicar lo siguiente:
# - Definir el stock de un producto en una variable. La variable será un diccionario, asi podemos manejar varios items de productos en una misma variable.

productos = {'producto1': 20, 'producto2': 50, 'producto3': 15, 'producto4': 13, 'producto5': 45 }
productos_seleccionados = {}
#podria ser en un txt para que no se borre :O

#En vez de producto1, producto2 etc. se podrian utilizar id's con numeros como el codigo de barra, además en los valores se podría asociar una lista, con el stock, vendidos, devueltos o cosas asi, mientras mas datos mejor

# - Definir una forma de solicitar el stock disponible del producto por consola. Definiremos una función stock() para poder solicitar el stock disponible. Pero antes, definiremos una función consulta() para determinar las distintas consultas que se puedan hacer y manipular el stock.

def consultas(productos):
    while True:
        print()
        consulta = int(input('Ingrese el numero de la opción que desea realizar: \n\n1. Stock disponible de un producto. \n\n2. Solicitar unidades de un producto. \n\n0. Salir.\n\n'))
        print()
        if consulta == 1: stock(productos)
        elif consulta == 2: solicitar(productos, productos_seleccionados)
        elif consulta ==0 : exit()

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
                    continue
            elif producto > len(list(productos)):
                    #Por si ponen un numero mayor a los de la lista
                    print()
                    print('Producto no encontrado pruebe nuevamente o ingrese 0 para salir\n')
                    continue
            else: 
                    #Numero correcto chin chin chin $$$$
                    productokey = list(productos.keys())[producto-1]
                    print()
                    #print del producto seleccionado con sus unidades
                    print(f'Existen {productos.get(productokey)} unidades de {productokey}\n')


# - Definir una forma de solicitar unidades del producto por consola. Este número de productos se
# almacenarán en una nueva variable llamada ‘Productos seleccionados’. Lo haremos con una función solicitar() dentro del menu consultas.
                    

def solicitar(productos, productos_seleccionados):
    while True:
            
            #utilizaremos el mismo tipo de input que en la función stock :)
            solicitud = int(input(f'Ingrese el numero del producto para agregar al carrito: \n\n{"\n".join((f'{index + 1}.{producto}' for index, producto in enumerate(productos.keys())) )} \nIngrese 0 para imprimir ticket\nIngrese 99 para voler a menú principal\n'))
            #Efectivamente, no existirá producto 99, número reservado por sistema xdxd

            
            ##Necesito una opcion para salir al menu de cosultas() y otro para salir e imprimir el ticket, y como int('00') = int('0'), necesitamos una opcion en la que 00 != 0, entonces utilizamos str()## Explicación para un if str(solicitud) == '00': pero no funcionó como se esperaba, extrañamente igua imprimía el ticket sin tener la funcion ticket(), se utilizo otro numero, 99 y funcioní sin dar problemas.
            if solicitud == 99:
                  return
            
            elif solicitud == 0:
                    #Para salir e imprimir ticket de pedido
                    if len(productos_seleccionados)>0:
                        return ticket(productos_seleccionados)
                    else:
                        continue

            #informamos del numero de stock disponible
            try:
                productokey = list(productos.keys())[solicitud-1]
            except IndexError:
                  print('Producto no existente, porfavor ingrese nuevamente')
                  solicitar(productos, productos_seleccionados)
            else:
                print(f'Existen {productos.get(productokey)} unidades de {productokey}\n')

            if solicitud < 0:
                    #Por si ponen un numero negativo
                    print()
                    print('Numero incorrecto, pruebe nuevamente.\n')
            elif solicitud > len(list(productos)):
                    #Por si ponen un numero mayor a los de la lista
                    print()
                    print('Producto no encontrado pruebe nuevamente o ingrese 0 para salir\n')
            else: 
                #solicitamos las unidades
                cantidad = int(input('Cuantas unidades desea añadir al carrito?: \nSi desea salir, ingrese 0.\n'))

                #Opcion para salir
                if cantidad == 0:
                       return
                #cambiamos el valor de cantidad si la cantidad requerida es igual o mayor a 12
                if cantidad >= 12:
                    cantidad = cantidad +1
                else:
                    cantidad = cantidad

                if cantidad > productos.get(productokey): 
                    print('No existe stock suficiente para su pedido, porfavor intentelo nuevamente.\n')
                    continue
                #Verificar existencias del producto, si no hay, se devuelve mensaje para que insista en otro valor
                       
                elif cantidad <= productos.get(productokey):
                    if maximo20(productos_seleccionados, cantidad):
                        continue
                    else:
                        productos[productokey] -= cantidad; productos_seleccionados[productokey] = productos_seleccionados.get(productokey, 0) + cantidad
                        continue
                         # asi, si no existe, ahora existe y podemos sumarle, si lo hacemos solo con un productos_seleccionados[productokey] += cantidad, si no exsite en el diccionario, dará error con el key.


#crearemos una funcion que controle el maximo de unidades. Las variables que entran tiene el mismo nombre las cuales vamos a poner en la funcion, productos_seleccionados es un dict() y solicitud un int().
def maximo20(productos_seleccionados, cantidad):
    if sum(productos_seleccionados.values()) + cantidad > 20: 
        print('\nNo se puede realizar esta operación, el carrito sobrepasaria el limite establecido. Max 20 unidades en total.')
        return 1 #Si la cantidad que se desea ingresar al carrito sobrepasa las 20 unidades, indicamos que no se puede realizar la solicitud y retornmos a la funcion solicitar(productos_seleccionados) para que se siga añadiendo si se desea.
    elif sum(productos_seleccionados.values()) + cantidad == 20: 
        print('\nLe informamos que con la ultima adición se alcanzó el máximo de unidades por pedido') #si el productos_seleccionados tiene 20 unidades en total con la ultima adición, se entrega el ticket inmediatamente.
        return 0


#Y otra para que me imprima el ticket con los productos y unidades seleccionadas.

def ticket(productos_seleccionados):
    #Imprimimmos diccionario de productos_seleccionados con keys y values con funcion items()
    print(f'Su pedido es: \n{"\n".join((f'{index + 1}. {producto[0]}: {producto[1]} unidad/es' for index, producto in enumerate(productos_seleccionados.items())))}')

consultas(productos)

# - Los productos reubicados serán descontados del stock inicial.
# - El programa debe verificar que existan unidades disponibles.
# - Al verificar las unidades disponibles, el programa entregará una unidad extra cuando se seleccionen
# más de 12 unidades. Verificar que el stock posibilite entregar una unidad extra. Sino se entregan las
# unidades justas. Cada una de las posibles acciones debe imprimir un mensaje explicando lo realizado.
# - No se pueden solicitar más de 20 unidades en un mismo pedido.
# - Si el valor ingresado es superior al stock disponible, este debe entregar un mensaje indicando que no
# es posible realizar esta acción debido a que no hay stock suficiente.
# El código debe estar debidamente comentado para asegurar su comprensión.









#Notas:
#Se hicieron distintas pruebas y los diccionarios, despues de solicitar y verificar stock, se actualizan correctamente, pero si se termina la funcion consultas obviamente no se guarda, esto podríamos solucionarlo con un txt, ya que no manejamos aún base de datos. Además se cumple con los diferentes requisistos del ejericio.
#Ahondar mas en formas de una linea y formas ternarias para la proxima.
#Experimentar mas con funciones de listas, tuplas y diccionarios con formas lineales, anidadas y f-string.