import time
pausa = 0.5
a = int(input("introduce un valor: "))
b=int(input("introduce otro valor: "))

suma=a+b
resta=a-b
multiplicacion=a*b

if b == 0:
    time.sleep(pausa)
    print("No se puede dividir entre 0")
    time.sleep(pausa)
    if a == 6 and b == 7:
        time.sleep(pausa)
        print("SIX SEBEEEENNNNN")
    elif suma == 13 or resta == 13 or multiplicacion == 13:
        time.sleep(pausa)
        print("Mientras más me lo mamas más me crece")
    elif suma == 14 or resta == 14 or multiplicacion == 14:
        time.sleep(pausa)
        print("Prende cam")    
    else:
        time.sleep(pausa)
        print(f"Suma: {suma}")
        time.sleep(pausa)
        print(f"Resta: {resta}")
        time.sleep(pausa)
        print(f"Multiplicacion: {multiplicacion}")
else:
    division=a/b

    if a == 6 and b == 7:
        time.sleep(pausa)
        print("SIX SEBEEEENNNNN")
    elif suma == 13 or resta == 13 or multiplicacion == 13 or division == 13:
        time.sleep(pausa)
        print("Mientras más me lo mamas más me crece")
    elif suma == 14 or resta == 14 or multiplicacion == 14 or division == 14:
        time.sleep(pausa)
        print("Prende cam")    
    else:
        time.sleep(pausa)
        print(f"Suma: {suma}")
        time.sleep(pausa)
        print(f"Resta: {resta}")
        time.sleep(pausa)
        print(f"Multiplicacion: {multiplicacion}")
        time.sleep(pausa)
        print(f"Division: {division}")