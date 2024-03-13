import random, time
#useryclave se utiliza para guardar los usuarios y contrasenas creadas por la funcion user()

useryclave = {}

#userclaveprueba se utiliza para la funcion enviarencuestas() e incorporar las encuentas de forma aleatoria a siete ususarios con contrasenas ya creadas

useryclaveprueba= {'usuario1':['123456Ab'], 'usuario2':['123456Ab'], 'usuario3':['123456Ab'], 'usuario4':['123456Ab'], 'usuario5':['123456Ab'], 'usuario6':['123456Ab'], 'usuario7':['123456Ab'], 'usuario8':['123456Ab'], 'usuario9':['123456Ab'], 'usuario10':['123456Ab'] }

def main():
    while True:
        print()
        consulta = int(input('Ingrese el numero de la opción que desea realizar: \n\n1. Crear usuario nuevo (En lista useryclave). \n\n2. Enviar encuestas (A lista auxiliar useryclaveprueba). \n\n3. Imprimir lista useryclave. \n\n0. Salir.\n\n'))
        print()
        if consulta == 1: user(useryclave)
        if consulta == 2: enviarencuestas(useryclaveprueba)
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

#FIN OPCION 1

#OPCION 2

def enviarencuestas(useryclaveprueba):
    encuestas = ['habitos alimenticios', 'experiencia laboral', 'actividades recreativas', 'atletismo', 'natacion', 'deportes en general']
    aux = list(useryclaveprueba.keys())
    aux = random.sample(aux, 7)
    for usuario in aux:
        useryclaveprueba[usuario] += [random.sample(encuestas, random.randint(1, 5))]
    print('A continuacion se mostraran los usuarios y sus respectivas encuestas a realizar:\n ')
    for usuario, valores in useryclaveprueba.items():
         if len(valores) > 1:
             print(f'El usuario {usuario} tiene que realizar {len(valores[1])} encuestas y son las siguientes:') 
             for encuesta in valores[1]:
                 print(f'-{encuesta}')
                 time.sleep(3)
    
#FIN OPCION 2
    
main()