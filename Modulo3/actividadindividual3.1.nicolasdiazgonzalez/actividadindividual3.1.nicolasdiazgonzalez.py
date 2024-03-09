
def cuestionarios():
    cuestionarios = []
    # ● El usuario debe ingresar por consola sus características (lugar de origen, edad y afinidad por los deportes).
    edad = int(input("¿Cuál es su edad? "))
    origen = input("¿Cuál es su lugar de origen? (America latina / Otro): ").lower()
    deportes = input("¿Tiene afinidad por los deportes? (si/no): ").lower()

    if origen == "america latina":
        # ● Los usuarios que son originarios de América Latina responden el cuestionario sobre hábitos alimenticios.
        cuestionarios.append("Cuestionario de hábitos alimenticios")
        # ● Todos los usuarios entre 18 y 29 años responden el cuestionario de empleabilidad.
        if 18 <= edad <= 29:
            cuestionarios.append("Cuestionario de empleabilidad")
        # ● Los usuarios originarios de América Latina entre 30 y 59 años responden el cuestionario de experiencia laboral.
        elif 30 <= edad <= 59:
            cuestionarios.append("Cuestionario de experiencia laboral")
        # ● Los usuarios originarios de América Latina de 60 años y más responden el cuestionario de actividades recreativas.
        elif edad >= 60:
            cuestionarios.append("Cuestionario de actividades recreativas")
        # ● Todos los usuarios que tienen afinidad por los deportes y que son menores de 60 años responden el cuestionario de atletismo.
        if deportes == "si" and edad < 60:
            cuestionarios.append("Cuestionario de atletismo")
        # ● Los usuarios originarios de América Latina que tienen afinidad por los deportes y que tienen 60 años o más responden el cuestionario de natación.
        elif deportes == "si" and edad >= 60:
            cuestionarios.append("Cuestionario de natación")
        # ● Todos los usuarios que no tienen afinidad por los deportes responden un cuestionario de Deportes en General.
        elif deportes == "no":
            cuestionarios.append("Cuestionario de Deportes en General")

    else:
        # ● Todos los usuarios entre 18 y 29 años responden el cuestionario de empleabilidad.
        if 18 <= edad <= 29:
            cuestionarios.append("Cuestionario de empleabilidad")
        # ● Todos los usuarios que tienen afinidad por los deportes y que son menores de 60 años responden el cuestionario de atletismo.
        if deportes == "si" and edad < 60:
            cuestionarios.append("Cuestionario de atletismo")
        # ● Todos los usuarios que no tienen afinidad por los deportes responden un cuestionario de Deportes en General.
        elif deportes == "no":
            cuestionarios.append("Cuestionario de Deportes en General")

    # ● El número máximo de cuestionarios a responder es de 3.        
    if len(cuestionarios) > 3:
        cuestionarios = cuestionarios[::2]

    # ● Programa un mensaje que indique el número de cuestionarios a responder y cuáles son.
    numerodecuestionarios = len(cuestionarios)
    print(f"Debes responder {numerodecuestionarios} cuestionarios:")
    for i in cuestionarios:
        print(f'{cuestionarios.index(i)+1}. {i}')
    
cuestionarios()

