
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


#La contrasena tiene que tener las siguientes condiciones
condiciones = ['8 o mas caracteres', 'mayusculas', 'minusculas', 'cifras']

def validacioncontrasena(contrasena, condiciones):
    if len(contrasena) >= 8:
        print(f'Su contrasena cumple y tiene {condiciones.pop('8 o mas caracteres')}')
    if not any(letra.isupper() for letra in contrasena):
        print(f'Su contrasena cumple y tiene {condiciones.pop('mayusculas')}')