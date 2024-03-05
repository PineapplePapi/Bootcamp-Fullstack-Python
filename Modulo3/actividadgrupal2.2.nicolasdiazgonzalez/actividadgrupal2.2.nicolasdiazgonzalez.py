# - Formulen un programa que:

# i. A una variable se le asigne un mensaje motivador que incluya los nombres de todos los
# integrantes. ¿Qué tipo de dato puede ser?
# El tipo de dato debe ser un string.

lista = ['nicolas', 'Andrea', 'alan', 'Daniela', 'ignacio', 'jose', 'Pedrito']


mensaje_motivador = "Somos Te lo Vendo! Y esperamos que hoy sea un gran día !"

for usuario in lista:
    print("Hola", usuario.capitalize(), ", " + mensaje_motivador)

# ii. Se asegure que todos su caracteres estén en mayúscula.

mensaje_motivador = mensaje_motivador.upper()

print(mensaje_motivador)




# iii. Elabore una lista con cada palabra del string.
# iv. Cada integrante del grupo debe reconocer en qué índice está su nombre.
# v. Indique cuántas palabras tenía el string.
# vi. Imprima una tupla con todas las palabras del string.
# vii. ¿Con qué función podrían obtener el mensaje por teclado al ejecutar el programa?
# Implementarlo!.