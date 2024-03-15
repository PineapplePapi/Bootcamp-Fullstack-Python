import random
import string

class paciente:
    def __init__(self, nombre, password, correo):
        self.nombre = nombre
        self.password = password
        self.correo = correo
    
    def datos(self):
        print(f"{self.nombre}")
        print(f"{self.password}")
        print(f"{self.correo}")
    
class TrabajadorSalud:
    def __init__(self, nombre, password, correo):
        self.nombre = nombre
        self.password = password
        self.correo = correo
    
    def cambiar_paciente(self, paciente, nuevo_nombre, nuevo_correo):
        paciente.nombre = nuevo_nombre
        paciente.correo = nuevo_correo

    def cambiar_salud(self, nuevo_nombre, nuevo_correo):
        self.nombre = nuevo_nombre
        self.correo = nuevo_correo

class Master:
    def __init__(self, nombre, password, correo):
        self.nombre = nombre
        self.password = password
        self.correo = correo
    
    def cambiar_datos(self, usuario, nuevo_nombre, nuevo_correo):
        usuario.nombre = nuevo_nombre
        usuario.correo = nuevo_correo


# Elaborar un programa que recorra una lista con los nombres de 10 de sus futuros usuarios de tu aplicación (pueden ser personas, pacientes, organizaciones sociales o instituciones públicas).

useryclave = {}

def main():
    while True:
        print()
        consulta = int(input('Ingrese el numero de la opción que desea realizar: \n\n1. Crear usuario nuevo (En lista useryclave). \n\n2. Enviar encuestas (A lista auxiliar useryclaveprueba). \n\n3. Imprimir lista useryclave. \n\n0. Salir.\n\n'))
        print()
        if consulta == 1: tipo_de_usuario()
        if consulta == 3: print(f"Usuarios regristrados en lista useryclave:\n {useryclave}")
        elif consulta ==0 : exit()

#OPCION 1
def user(useryclave):
    usuario = input('Ingrese su nombre de ususario: ')
    useryclave[usuario] = [ingresarcontrasena()]
    print(f'Contraseña registrada correctamente.\n{''.join((f'Usuario: {usuario}\nClave: {clave[0]}' for usuario, clave in useryclave.items()))}')

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

def tipo_de_usuario():
    print()
    eleccion = int(input('Ingrese el numero de la opción para tipo de usuario que quiere crear: \n\n1. Paciente. \n\n2. Trabajador de la Salud. \n\n0. Salir.\n\n'))
    if eleccion == 1: useryclave()
    if eleccion == 2: useryclave()
    elif eleccion ==0 : exit()


main()
