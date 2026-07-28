import time

opcion = 0
pausa = 0.4
alumnos = []

while opcion != 5:
    print("==============================")
    print("          Bienvenido          ")
    print("==============================")
    print("Que desea realizar?")
    time.sleep(pausa)
    print("------------------------------")
    print("1. Agregar un registro")
    print("------------------------------")
    print("2. Ver registros")
    print("------------------------------")
    print("3. Borrar un registro")
    print("------------------------------")
    print("4. Editar un registro")
    print("------------------------------")
    print("5. Salir")
    print("------------------------------")

    opcion = int(input("Introduzca el numero de la opcion deseada: "))

    if opcion == 1:

        alumno = {}

        print("==============================")
        nombre = ""
        while nombre.strip() == "":
            nombre = input("Introduzca el nombre del alumno: ")
            if nombre.strip() == "":
                print("___________________________________")
                print("No puede dejar este espacio vacio!")
                print("___________________________________")
        alumno["nombre"] = (nombre)

        print("------------------------------")
        edad = -1
        while edad <= 0:
            edad = int(input("Introduzca la edad del alumno: "))
            if edad <= 0:
                print("___________________________________")
                print("          Edad no valida!")
                print("___________________________________")
        alumno["edad"] = (edad)

        print("------------------------------")
        grupo = ""
        while grupo.strip() == "":
            grupo = input("Introduzca a que grupo pertenece el alumno: ")
            if grupo.strip() == "":
                print("___________________________________")
                print("No puede dejar este espacio vacio!")
                print("___________________________________")
        alumno["grupo"] = (grupo)

        print("------------------------------")
        promedio = -1
        while promedio <= 0 or promedio > 10:
            promedio = float(input("Introduce el promedio del alumno: "))
            if promedio <= 0 or promedio > 10:
                print("___________________________________")
                print("        Edad no valida!")
                print("___________________________________")
        alumno["promedio"] = (promedio)
        print("==============================")

        alumnos.append(alumno)
        time.sleep(pausa)

    elif opcion == 2:
        for alumno in alumnos:
            print("==============================")
            print(f"Nombre: {alumno["nombre"]}")
            print("------------------------------")
            print(f"Edad: {alumno["edad"]}")
            print("------------------------------")
            print(f"Grupo: {alumno["grupo"]}")
            print("------------------------------")
            print(f"Promedio: {alumno["promedio"]}")
            print("------------------------------")
            print("==============================")
            time.sleep(pausa)

    elif opcion == 5:
        print("------------------------------")
        print("     Cerrando programa...     ")
        print("------------------------------")
        time.sleep(pausa)
        break