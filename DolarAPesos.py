import time
pausa = 0.3

dolares = float(input("Cuantos dolares deseas convertir? "))

print("Deseas usar un valor del dolar aproximado o insertar un valor?")
time.sleep(pausa)
print("Introduzca 1 para usar valor aproximado")
time.sleep(pausa)
print("Introduzca 2 para insertar un valor")
time.sleep(pausa)
opcion = int(input("Elija su opcion: "))

if opcion == 1:
    tipo_cambio = 17.49
    pesos = tipo_cambio * dolares
elif opcion == 2:
    tipo_cambio = float(input("Introduzca el valor del dolar a dia de hoy: "))
    pesos = tipo_cambio * dolares
else:
    print("No es una opcion valida.")
    exit()

print("=======================================")
print("        Conversion completada")
print("=======================================")
print(f"Dolares.................... ${dolares:.2f}")
print(f"Tipo de cambio............. ${tipo_cambio:.2f}")
print(f"Pesos mexicanos............ ${pesos:.2f}")    
