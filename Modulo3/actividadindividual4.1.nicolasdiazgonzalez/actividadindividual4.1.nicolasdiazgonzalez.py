useryclave = {}

def main():
    while True:
        print()
        consulta = int(input('Ingrese el numero de la opción que desea realizar: \n\n1. Crear contraseña. \n\n2. Enviar encuestas. \n\n0. Salir.\n\n'))
        print()
        if consulta == 1: user(useryclave)
        if consulta == 2: enviarencuestas(useryclave)
        elif consulta ==0 : exit()

#OPCION 1
def user(useryclave):
    usuario = input('Ingrese su nombre de ususario: ')
    useryclave[usuario] = ingresarcontrasena()
    print(f'Contraseña registrada correctamente.\n{''.join((f'Usuario: {usuario}\nClave: {clave}' for usuario, clave in useryclave.items()))}')
    exit()

def ingresarcontrasena():
    while True:
        contrasena = input('Ingrese su contrasena: ')
        if len(validacioncontrasena(contrasena)) > 0:
            print(f"Su contrasena no cumple con las siguientes condiciones: \n {"\n ".join((f"{condicion}" for condicion in validacioncontrasena(contrasena)))}")
            continue
        return contrasena

def validacioncontrasena(contrasena):
    condiciones = ['8 o mas caracteres', 'mayusculas', 'minusculas', 'cifras']
    if len(contrasena) >= 8:
        condiciones.remove('8 o mas caracteres')
    if any(letra.isupper() for letra in contrasena):
        condiciones.remove('mayusculas')
    if any(letra.islower() for letra in contrasena):
        condiciones.remove('minusculas')
    if any(letra.isdigit() for letra in contrasena):
        condiciones.remove('cifras')
    return condiciones

#FIN OPCION 1


#OPCION 2

def enviarencuestas():


main()