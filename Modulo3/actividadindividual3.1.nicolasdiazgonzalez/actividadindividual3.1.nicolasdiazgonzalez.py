# DESARROLLO
# Como buen desarrollador, para comenzar a poder trabajar de manera óptima, es necesario que
# debamos preparar las herramientas necesarias para inicializar nuestro proyecto, esto incluye tener ya
# nuestro editor de texto y la versión de Python disponible en nuestro equipo.
# Familiarizado ya con estos componentes debemos prepararnos para realizar las siguientes acciones,
# para simular el funcionamiento de tu aplicación.

# ● Para desarrollar de mejor forma tu aplicación, requieres conocer mejor a los usuarios que la
# utilizarán. Antes de continuar desarrollando, debes elaborar un programa que tiene la funcionalidad de
# enviar cuestionarios a grupos particulares de personas.

# ● Los formularios varían según la edad, el lugar de origen y la afinidad con los deportes que tiene
# el usuario.
# ● El número máximo de cuestionarios a responder es de 3.
# ● Los usuarios que son originarios de América Latina responden el cuestionario sobre hábitos
# alimenticios.
# ● Los usuarios que NO son originarios de América Latina no responden el cuestionario de hábitos
# alimenticios.
# ● Todos los usuarios entre 18 y 29 años responden el cuestionario de empleabilidad.
# ● Los usuarios originarios de América Latina entre 30 y 59 años responden el cuestionario de
# experiencia laboral.
# ● Los usuarios originarios de América Latina de 60 años y más responden el cuestionario de
# actividades recreativas.
# ● Todos los usuarios que tienen afinidad por los deportes y que son menores de 60 años
# responden el cuestionario de atletismo.
# ● Los usuarios originarios de América Latina que tienen afinidad por los deportes y que tienen 60
# años o más responden el cuestionario de natación.
# ● Todos los usuarios que no tienen afinidad por los deportes responden un cuestionario de
# Deportes en General.
# ● El usuario debe ingresar por consola sus características (lugar de origen, edad y afinidad por los
# deportes).
# ● Programa un mensaje que indique el número de cuestionarios a responder y cuáles son.













def enviar_cuestionarios():
    # Obtener información del usuario
    lugar_origen = input("¿Cuál es tu lugar de origen? (América Latina / Otro): ").lower()
    edad = int(input("¿Cuál es tu edad? "))
    afinidad_deportes = input("¿Tienes afinidad por los deportes? (Sí / No): ").lower()

    cuestionarios = []

    # Cuestionarios a responder 
    if lugar_origen == "américa latina":
        cuestionarios.append("Cuestionario de hábitos alimenticios")
        if 18 <= edad <= 29:
            cuestionarios.append("Cuestionario de empleabilidad")
        elif 30 <= edad <= 59:
            cuestionarios.append("Cuestionario de experiencia laboral")
        elif edad >= 60:
            cuestionarios.append("Cuestionario de actividades recreativas")

        if afinidad_deportes == "sí" and edad < 60:
            cuestionarios.append("Cuestionario de atletismo")
        elif afinidad_deportes == "sí" and edad >= 60:
            cuestionarios.append("Cuestionario de natación")
        elif afinidad_deportes == "no":
            cuestionarios.append("Cuestionario de Deportes en General")

    else:  # Usuarios NO originarios de América Latina
        if 18 <= edad <= 29:
            cuestionarios.append("Cuestionario de empleabilidad")

        if afinidad_deportes == "sí" and edad < 60:
            cuestionarios.append("Cuestionario de atletismo")
        elif afinidad_deportes == "sí" and edad >= 60:
            cuestionarios.append("Cuestionario de natación")
        elif afinidad_deportes == "no":
            cuestionarios.append("Cuestionario de Deportes en General")

    # Mostrar mensajes al usuario
    num_cuestionarios = len(cuestionarios)
    if num_cuestionarios == 0:
        print("No tienes cuestionarios para responder.")
    else:
        print(f"Debes responder {num_cuestionarios} cuestionarios:")
        for i, cuestionario in enumerate(cuestionarios, start=1):
            print(f"{i}. {cuestionario}")

enviar_cuestionarios()