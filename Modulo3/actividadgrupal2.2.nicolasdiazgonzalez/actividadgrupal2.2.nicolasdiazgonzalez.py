#Módulo 3: Actividad Grupal 2
# Grupo 1 

# - Formulen un programa que:

# i. A una variable se le asigne un mensaje motivador que incluya los nombres de todos los
# integrantes. ¿Qué tipo de dato puede ser?
# El tipo de dato debe ser un string.

import paquete
from paquete.moduloprueba import mensaje_motivador              #con * para importar todo dentro del módulo
from paquete.modulo2 import prueba_paquete
print(mensaje_motivador)
print()
print(prueba_paquete)
print()
# ii. Se asegure que todos su caracteres estén en mayúscula.

mensaje_motivador = mensaje_motivador.upper()

print(mensaje_motivador)
print()

# iii. Elabore una lista con cada palabra del string.

lista = mensaje_motivador.split()

print(lista)
print()

# iv. Cada integrante del grupo debe reconocer en qué índice está su nombre.

peticion = input('Ingrese el nombre del integrante que desea saber su indice en la lista: ').upper()
def index(peticion):
    if peticion in lista:
        print('La posición de ',peticion,'es: ', lista.index(peticion))
    else:
        print('El nombre ingresado no se encuentra')

index(peticion)
print()
# v. Indique cuántas palabras tenía el string.
print()

print(f"El mensaje motivacional tiene {len(lista)} palabras")
print()
# vi. Imprima una tupla con todas las palabras del string.

tupla = tuple(lista)

print(f"Y ahora mejor, EN FORMATO TUPLA {tupla}")

# vii. ¿Con qué función podrían obtener el mensaje por teclado al ejecutar el programa?

def mensajemotivador():
    mensaje_motivador2 = input('Ahora ingrese un mensaje motivador: ')
    return mensaje_motivador2
print()
mensaje_motivador2 = mensajemotivador()
print()
print(mensaje_motivador2)
print()

# Implementarlo!.

# - Discutan ¿Qué es un dato booleano? ¿Qué utilidad puede tener para el desarrollo de un
# programa?

# #Un dato booleano es un tipo de dato que puede tomar solo dos valores: True (verdadero) o False (falso).
# Es útil para representar condiciones lógicas, realizar operaciones condicionales y tomar decisiones en un programa.Por ejemplo se puede utilizar para verificar si un usuario está autenticado o no, si una persona es mayor de edad, si un número es par o impar, entre otros casos.

# - Investigar qué significa que python sea un lenguaje de tipado dinámico.

# Python es un lenguaje de tipado dinámico, lo que significa que no es necesario declarar el tipo de dato de una variable al crearla. En cambio, el intérprete de Python determina automáticamente el tipo de dato de una variable en tiempo de ejecución, basándose en el valor que se le asigna. Esto brinda flexibilidad, ya que una variable puede cambiar de tipo de dato durante la ejecución del programa.


#La siguiente sección está documentada en el archivo "documentacion.txt"
# - Investigar y documentar sobre la creación de Módulos en Python.22 
# - Investigar y documentar sobre la creación de Paquetes en Python.
# - Investigar e implementar el uso del archivo __init__.py

