
def main():
    while True:
        print()
        consulta = int(input('Ingrese el numero de la opción que desea realizar: \n\n1. Crear contraseña. \n\n2. Enviar encuestas. \n\n0. Salir.\n\n'))
        print()
        if consulta == 1: stock(productos)
        elif consulta == 2: solicitar(productos, productos_seleccionados)
        elif consulta ==0 : exit()


def ingresarcontrasena():
    contrasena = input('Ingrese su contrasena: ')



def validacioncontrasena(contrasena):
    validacion = []
    if len(contrasena) < 8:
        validacion.append('contrasena no cumple con el largo minimo')
    if 