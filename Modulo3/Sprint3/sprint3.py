import random
import string

# Elaborar un programa que recorra una lista con los nombres de 10 de sus futuros usuarios de tu aplicación (pueden ser personas, pacientes, organizaciones sociales o instituciones públicas).

futuros_usuarios = ['persona1', 'persona2', 'paciente3', 'paciente4', 'organizacion5', 'organizacion6', 'institucion7', 'institucion8', 'seguro9', 'seguro10']

useryclave = {}

def main():
    while True:
        print()
        consulta = int(input('Ingrese el numero de la opción que desea realizar: \n\n1. Anadir usuarios con contrasena y numero.\n\n0. Salir.\n\n'))
        print()
        if consulta == 1: usuarios(futuros_usuarios)
        elif consulta ==0 : exit()

# Mediante una función, a todos los usuarios se les creará una cuenta automáticamente.
def usuarios(futuros_usuarios):
    # El programa no terminará de preguntar por los números hasta que todas las organizaciones tengan un número de contacto asignado.
    for elemento in futuros_usuarios:
        # Cada cuenta debe guardarse en una nueva variable con su respectiva contraseña.
        # Se debe guardar como un string.
        useryclave[elemento] = (generadorcontrasena(), numerotelefono(elemento))
    #Este print solo es para mostrar y comprobar el diccionario con usuario, contrasena y numero.
    print(f'\n\nEstos son los usuarios con sus respectivas contrasenas y numeros de telefono: \n {"\n".join((f'{usuario} con clave {claveynumero[0]} y con numero telefonico {claveynumero[1]}' for usuario, claveynumero in useryclave.items()))}\n')
    exit()


#Asigne una contraseña para cada cuenta. La contraseña debe ser creada con random y debe cumplir con los siguientes criterios: mayúsculas, minúsculas y números.
def generadorcontrasena():
    minuscula = "abcdefghijklmnopqrstuvwxyz"
    mayuscula = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    contrasena_lista = random.sample(minuscula, 5) + random.sample(mayuscula, 5) + random.sample(numeros, 5)
    random.shuffle(contrasena_lista)
    contrasena = ''.join(contrasena_lista) # ''.join lo convierte en string
    return contrasena

print(generadorcontrasena())

def numerotelefono(elemento):
    while True:
        # Por cada cuenta debe pedir un número telefónico para contactarse.
        numero = input(f"{elemento}, ingrese su número telefónico de 8 dígitos sin incluir su código de país (+569): ")
        # El programa debe verificar que el número telefónico tenga 8 dígitos numéricos.
        if (len(numero) > 8) or (len(numero) < 8): 
            print("Colocaste un número demasiado largo o corto, por favor ingrese su número de 8 dígitos nuevamente sin incluir su código de país (+569).")
            continue #corta la iteración actual y entra a una nueva
        return numero


main()


