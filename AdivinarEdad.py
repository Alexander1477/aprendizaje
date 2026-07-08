import time

print("puedo saber tu edad con solo unas preguntas...")
time.sleep(2)

edad = int(input("¿cuantos años tienes?"))
if edad > 0:
    print("procesando información...")
    time.sleep(2)
    print("cargando...")
    time.sleep(2)
    print("tienes", edad, "años")
