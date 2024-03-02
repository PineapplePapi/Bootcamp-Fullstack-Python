# ● En base al contexto: Piensa en una aplicación web que busque solucionar una problemática.
# ● Esta aplicación debe entregar la posibilidad de iniciar sesión con un perfil individual.
# ● Generalmente, uno ingresa a su cuenta personal en una página, ésta te saluda y te reconoce
# ● Intentemos replicar esto. Crea un string con el nombre de al menos 7 usuarios de tu aplicación.

lista = ['nicolas', 'Andrea', 'alan', 'Daniela', 'ignacio', 'jose', 'Pedrito']

listanormalizada = []
for i in lista:
    listanormalizada.append(i.lower())
    # Recorro la lista sin normalizar, agrego cada elemento a la lista normalizada y cada elemento que agrego le aplico un lower().

# ● Ahora piensa en tres de ellos. Buscalos en la lista con el método adecuado.
print()
peticion = input('Ingrese 3 nombres de usuarios separados por un espacio: ').lower()
print()
# ● ¿Qué problemas pueden surgir si otra persona quiere buscar a un usuario e ingresa
# manualmente su nombre? ¿Cómo solucionarías este problema?

#Puede que los nombres en la lista no estén en el mismo formato con el que la persona busca el nombre y no coincidan por el formato o tildes, hay que normalizar o la busqueda y/o la lista. Utilizando .lower(), normalizaremos la lista y la petición del usuario para poder buscarlo en la lista. Si llegara a tner tilde algun nombre, habría que utilizar la biblioteca "unidecode" para importar "unidecode" para quitar los caracteres especiales como tildes o dieresis de los nombres y normalizarlo.
#Además, puede que uno de los nombres que se ingrese no se encuentre en la lista.


# ● Convierte tu string en una lista, en la cual cada elemento es un usuario.

if " " in peticion:
    peticion = peticion.split(" ")  #split() convierte en lista separando por un carácter especifico, en este caso " "
else:
    peticion = [peticion] #si solo es un nombre, y no hay espacios, convierte el nombre en una lista.
        
# ● Imprime en pantalla la cantidad usuarios que tiene tu aplicación.
    
print(f'Los usuarios de la aplicación son:  {len(lista)}')
print()
for usuario in listanormalizada:
    print(listanormalizada.index(usuario),'.',usuario.capitalize())
    print()

# ● Imprimer en pantalla un mensaje de saludo a los diferentes usuarios. ¿Qué técnica puedes
# utilizar para realizar esto?
#Podemos utilizar un ciclo for para recorrer nuetra lista peticion,comprobamos si está en nuestra listanormalizada, y saludamos a los usuarios e indicamos quien no está en la lista.
    
for usuario in peticion:
    if usuario in listanormalizada:
        usuario = usuario.capitalize()
        print(usuario,'es usuario, Bienvenido', usuario)
        print()
    else:
        usuario = usuario.capitalize() 
        print(usuario, 'no es usuario.')
        print()
