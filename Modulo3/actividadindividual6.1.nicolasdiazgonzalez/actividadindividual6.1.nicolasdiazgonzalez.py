import time

usuarios = {}

while True:
    nombre = input('Ingrese su nombre de usuario: \nSi desea salir, ingrese SALIR.\n').lower()
    if nombre == 'salir':
        break
    contrasena = input('Ingrese la contrasena: ')
    while True:
        edad = input('Ingrese su edad: ')
        if edad.isdigit():
            edad = int(edad)
            break
        else:
            print('Ingrese un valor correcto')
            continue
    usuarios[nombre] = {'contrasena': contrasena, 'edad': edad}
    print(f'Usuario {nombre}, tiene una edad: {edad}')
    time.sleep(5)
    print(f'Contrasena del usuario {nombre}: {contrasena}')
print(usuarios)