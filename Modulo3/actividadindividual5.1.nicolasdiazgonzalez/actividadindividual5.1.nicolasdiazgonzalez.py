from datetime import datetime
import uuid
import time

# DESARROLLO
# Como buen desarrollador, para comenzar a poder trabajar de manera óptima, es necesario que
# debamos preparar las herramientas necesarias para inicializar nuestro proyecto, esto incluye tener ya
# nuestro editor de texto y la versión de Python disponible en nuestro equipo.
# Familiarizado ya con estos componentes debemos prepararnos para realizar las siguientes acciones,
# para simular el funcionamiento de tu aplicación.

# Diseñe 7 diccionarios, donde el nombre de cada diccionario es el nombre de un usuario de su
# aplicación.
# En cada diccionario, integre características como: edad, género y otras características particulares de
# su aplicación.
# Por ejemplo, si la aplicación se enfoca en Juntas de Vecinos integrar dirección y número telefónico.
# Integre al menos cinco características.
# Guarde estos diccionarios en una lista. En el caso de ejemplo, podría ser nombrada “JJVV”.
# A continuación, recorra su lista e imprima toda la información que posee la estructura de datos sobre
# cada usuario (en el caso de ejemplo: de cada junta de vecinos).
# ¿Qué problemas encontró con esta forma de almacenar la información?

#Puede ser que el problema radique en la forma tosca de almacenar la informacion y la manera en la que puede acceder a ella. Aunque tuve dudas a la forma que se referia el ejercicio de la estructura de los datos. Espero cumplir satisfactoriamente los requerimientos del ejercicio. 


# Vuelva al inicio del problema y diseñe una estructura de datos unificada que permita almacenar todas
# las juntas de vecinos.
# Agregue para cada usuario los campos nombre_usuario, id_unico, antigüedad, fecha de incorporación.
# Imprima en pantalla la fecha de incorporación de todos los usuarios.



usuario1 = {"edad": "edad1", "género": "género1", "dirección": "dirección1", "teléfono": "teléfono1"}
usuario2 = {"edad": "edad2", "género": "género2", "dirección": "dirección2", "teléfono": "teléfono2"}
usuario3 = {"edad": "edad3", "género": "género3", "dirección": "dirección3", "teléfono": "teléfono3"}
usuario4 = {"edad": "edad4", "género": "género4", "dirección": "dirección4", "teléfono": "teléfono4"}
usuario5 = {"edad": "edad5", "género": "género5", "dirección": "dirección5", "teléfono": "teléfono5"}
usuario6 = {"edad": "edad6", "género": "género6", "dirección": "dirección6", "teléfono": "teléfono6"}
usuario7 = {"edad": "edad7", "género": "género7", "dirección": "dirección7", "teléfono": "teléfono7"}

JJV = [usuario1, usuario2, usuario3,usuario4, usuario5, usuario6, usuario7]

for usuario in JJV:
    for llave, valor in usuario.items():
        print (f'\n{llave} : {valor}\n')
    print()



JJVV ={ 'usuario1' : {"nombre" : "usuario1", "edad": "edad1", "género": "género1", "dirección": "dirección1", "teléfono": "teléfono1", "id_unico" : str(uuid.uuid4()), "antiguedad" : "antiguedad1", "fecha_de_incorporacion" : str(datetime.now())},
'usuario2' : {"nombre" : "usuario2", "edad": "edad2", "género": "género2", "dirección": "dirección2", "teléfono": "teléfono2", "id_unico" : str(uuid.uuid4()), "antiguedad" : "antiguedad2", "fecha_de_incorporacion" : str(datetime.now())},
'usuario3' : {"nombre" : "usuario3", "edad": "edad3", "género": "género3", "dirección": "dirección3", "teléfono": "teléfono3", "id_unico" : "id_unico3", "antiguedad" : "antiguedad3", "fecha_de_incorporacion" : str(datetime.now())},
'usuario4' : {"nombre" : "usuario4", "edad": "edad4", "género": "género4", "dirección": "dirección4", "teléfono": "teléfono4", "id_unico" : str(uuid.uuid4()), "antiguedad" : "antiguedad4", "fecha_de_incorporacion" : str(datetime.now())},
'usuario5' : {"nombre" : "usuario5", "edad": "edad5", "género": "género5", "dirección": "dirección5", "teléfono": "teléfono5", "id_unico" : str(uuid.uuid4()), "antiguedad" : "antiguedad5", "fecha_de_incorporacion" : str(datetime.now())},
'usuario6' : {"nombre" : "usuario6", "edad": "edad6", "género": "género6", "dirección": "dirección6", "teléfono": "teléfono6", "id_unico" : str(uuid.uuid4()), "antiguedad" : "antiguedad6", "fecha_de_incorporacion" : str(datetime.now())},
'usuario7' : {"nombre" : "usuario7", "edad": "edad7", "género": "género7", "dirección": "dirección7", "teléfono": "teléfono7", "id_unico" : str(uuid.uuid4()), "antiguedad" : "antiguedad7", "fecha_de_incorporacion" : str(datetime.now())} }


for llave, valor in JJVV.items():
    print(llave)
    print(valor["fecha_de_incorporacion"])