import time

pausa1 = 1
pausa2 = 0.4
opcion_origen = 0

while opcion_origen != 4:
    print("====================")
    print("    Bienvenido!")
    print("====================")
    time.sleep(pausa1)
    print("Seleccione la unidad de temperatura que desea convertir")
    time.sleep(pausa2)
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    print("4. Salir")
    time.sleep(pausa2)
    opcion_origen = int(input("Introduzca el numero de la opcion deseada: "))

    if opcion_origen == 1:
        c = float(input("Cuantos grados Celsius deseas convertir? "))
        print("A que unidad deseas convertir?")
        time.sleep(pausa2)
        print("1. Fahrenheit")
        print("2. Kelvin")
        time.sleep(pausa2)
        opcion_destino = int(input("Selecciona la opcion deseada: "))

        if opcion_destino == 1:
            f = c * 9/5 + 32
            print(f"Fahrenheit: {f}")
            time.sleep(pausa1)
        elif opcion_destino == 2:
            k = c + 273.15
            print(f"Kelvin: {k}")
            time.sleep(pausa1)

    elif opcion_origen == 2:
        f = float(input("Cuantos grados Fahrenheit deseas convertir? "))
        print("A que unidad deseas convertir?")
        time.sleep(pausa2)
        print("1. Celsius")
        print("2. Kelvin")
        time.sleep(pausa2)
        opcion_destino = int(input("Selecciona la opcion deseada: "))

        if opcion_destino == 1:
            c = f - 32 * 5/9
            print(f"Celsius: {c}")
            time.sleep(pausa1)
        elif opcion_destino == 2:
            k = f - 32 * 5/9 + 273.15
            print(f"Kelvin: {k}")
            time.sleep(pausa1)

    elif opcion_origen == 3:
        k = float(input("Cuantos grados Kelvin deseas convertir? "))
        print("A que unidad deseas convertir?")
        time.sleep(pausa2)
        print("1. Celsius")
        print("2. Fahrenheit")
        time.sleep(pausa2)
        opcion_destino = int(input("Selecciona la opcion deseada: "))

        if opcion_destino == 1:
            c = k - 273.15
            print(f"Celsius: {c}")
            time.sleep(pausa1)
        elif opcion_destino == 2:
            f = k - 273.15 * 9/5 + 32
            print(f"Fahrenheit: {f}")
            time.sleep(pausa1)


    elif opcion_origen == 4:
        print("Saliendo...")
        break