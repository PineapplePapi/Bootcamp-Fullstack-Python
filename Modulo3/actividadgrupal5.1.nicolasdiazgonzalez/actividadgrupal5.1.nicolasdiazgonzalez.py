import random, time, uuid

#1er diccionario informacion de clientes.
#2do diccionario informacion de producto.
#3er diccionario informacion de la compra de cada cliente (Vacio).

basededatos = [{
    "juan perez garcia": ["Juan Perez Garcia", 25, str(uuid.uuid4())],
    "maria lopez hernandez": ["Maria Lopez Hernandez", 30, str(uuid.uuid4())],
    "pedro garcia martinez": ["Pedro Garcia Martinez", 35, str(uuid.uuid4())],
    "ana martinez rodriguez": ["Ana Martinez Rodriguez", 28, str(uuid.uuid4())],
    "luis rodriguez perez": ["Luis Rodriguez Perez", 40, str(uuid.uuid4())],
    "sofia hernandez lopez": ["Sofia Hernandez Lopez", 22, str(uuid.uuid4())],
    "diego ramirez martinez": ["Diego Ramirez Martinez", 33, str(uuid.uuid4())],
    "elena gomez rodriguez": ["Elena Gomez Rodriguez", 29, str(uuid.uuid4())],
    "laura diaz garcia": ["Laura Diaz Garcia", 31, str(uuid.uuid4())],
    "carlos sanchez lopez": ["Carlos Sanchez Lopez", 26, str(uuid.uuid4())]},
    {
    "camisa azul": ["Camisa Azul", 2599, str(uuid.uuid4()), "Azul"],
    "pantalon negro": ["Pantalon Negro", 3999, str(uuid.uuid4()), "Negro"],
    "zapatos marron": ["Zapatos Marron", 4999, str(uuid.uuid4()), "Marron"],
    "bufanda gris": ["Bufanda Gris", 1250, str(uuid.uuid4()), "Gris"],
    "sombrero rojo": ["Sombrero Rojo", 1999, str(uuid.uuid4()), "Rojo"]},
    {
        
    }]

#MENU Y METODOS SIN FUCIONES >:c
while True:
    #Menu para los diferentes requerimientos
    eleccion = input('Seleccione el numero de la opcion que desea realizar: \n1. Agrege un cliente.\n2. Agrege un producto.\n3. Mostrar clientes.\n4. Mostrar productos.\n5. Eliminar un cliente al azar\n6. Eliminar ultimo producto agregado\n0. Ingrese 0 para salir.\n')
    if eleccion == '1':
        #Hay libertad para poner cualquier nombre
        nombre_completo = input("Ingrese el nombre completo del cliente: ")
        #En la edad, debe ser un numero y nos aseguramos que el numero sea digito y lo convertimos a entero en la misma variable, sino es digito, pedimos nuevamente que lo intente :D.
        while True:
            edad = input("Ingrese la edad del cliente: ")
            if edad.isdigit():
                edad = int(edad)
                break
            else:
                print("La edad debe ser un número. Intente nuevamente.")
        #Le asignamos id unico
        idcliente = str(uuid.uuid4())
        #Y lo añadimos al diccionario correspondiente
        basededatos[0][nombre_completo.lower()] = [nombre_completo, edad, idcliente]
    elif eleccion == '2':
        #Ingresamos el nombre del producto a añadir
        nombre_producto = input("Ingrese el nombre del producto: ")
        #while true para pedir un precio correcto, nos aseguramos que sea digito y lo convertimos en entero, el mismo procedimiento para la edad
        while True:
            precio = input("Ingrese el precio del producto (solo números enteros): ")
            if precio.isdigit():
                precio = int(precio)
                break
            else:
                print("El precio debe ser un número entero. Intente nuevamente.")
        #Generamos el id unico para el producto
        idproducto = str(uuid.uuid4())
        #Input para el color
        color = input("Ingrese el color del producto: ")
        #Añadimos todo al diccionario correspondiente a los productos
        basededatos[1][nombre_producto.lower()] = [nombre_producto, precio, idproducto, color]
    elif eleccion == '3':
        #Se imprimirá segun los tiempos de los requerimientos, el nombre se repetirá porque el key se nombró con el nombre del usuario y ademas se guardó en la lista valores.
        for llave, valores in basededatos[0].items():
            time.sleep(2)
            print(llave)
            for valor in valores:
                time.sleep(3)
                print(valor)
    elif eleccion == '4':
        #Se imprimirá segun los tiempos de los requerimientos, el nombre se repetirá porque el key se nombró con el nombre del producto y ademas se guardó en la lista valores.
        for llave, valores in basededatos[1].items():
            time.sleep(2)
            print(llave)
            for valor in valores:
                time.sleep(3)
                print(valor)
    elif eleccion == '5':
        #Si existen elementos en el diccionario de los usuarios, se puede eliminar un usuario, sino no
        if basededatos[0]:
            #Al azar, se escoge el elemento usuario a eliminar utilizando random.choice, para usarlo, se convierte en lista los elementos keys de basededatos correspondiente a los ususarios.
            eliminar = random.choice(list(basededatos[0].keys()))
            #se elimina el elemento elegido al azar mediante un pop() para guardarlo en una constante.
            eliminado = basededatos[0].pop(eliminar)
            #Por ultimo, imprimimos todos los datos del usuario eliminado
            print(f"Información del usuario eliminado:\nNombre: {eliminado[0]}\nEdad: {eliminado[1]}\nID: {eliminado[2]}")
        else:
            print("No hay usuarios para eliminar.")
    elif eleccion == '6':
        #Comprobamos que existen productos en su diccionario.
        if basededatos[1]:
            #Generamos una lista con los nombres de los productos y guardamos en una variable el nombre del ultimo.
            eliminar = list(basededatos[1].keys())[-1]
            #Eliminamos el elemento con un pop() y lo guardamos en una constante.
            eliminado = basededatos[1].pop(eliminar)
            #Hacemos uso de la constante eliminado para imprimir sus datos.
            print(f"Información del producto eliminado:\nNombre: {eliminado[0]}\nPrecio: {eliminado[1]}\nID: {eliminado[2]}\nColor: {eliminado[3]}")
    elif eleccion == '0':
        exit()
    else:
        print('Opcion no valida, intente nuevamente.')

