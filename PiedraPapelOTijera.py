import time
import random


MiPuntaje = 0
PuntajeCompu = 0

print("Bienvenido, espero te diviertas!")
while True:
    opcion_jugador = int(input("Que escoges: \n1.Piedra\n2.Papel\n3.Tijera\n >>"))
    if opcion_jugador == 1 or opcion_jugador == 2 or opcion_jugador == 3:
        
        opcionComputadora = random.randint(1,3)
        
        computadoraEnTexto = ""
        if opcionComputadora ==1:
            
            computadoraEnTexto = "Piedra"
        elif opcionComputadora == 2:
            computadoraEnTexto = "Papel"
        else:
            computadoraEnTexto = "Tijera"
            
        print("Calculando resultados...")
        time.sleep(3)
        
        if opcion_jugador == opcionComputadora:
            print("Haz empatado.")
        elif opcion_jugador == 1 and opcionComputadora == 3:
            print("La computadora escogio:", computadoraEnTexto)
            print("Felicidades, haz ganado!")
            MiPuntaje = MiPuntaje + 1
        elif opcion_jugador == 2 and opcionComputadora == 1:
            print("La computadora escogio:", computadoraEnTexto)
            print("Felicidades, haz ganado!")
            MiPuntaje = MiPuntaje + 1
        elif opcion_jugador == 3 and opcionComputadora == 2:
            print("La computadora escogio:", computadoraEnTexto)
            print("Felicidades, haz ganado!")
            MiPuntaje = MiPuntaje + 1
        else:
            print("La computadora escogio:", computadoraEnTexto)
            print("Haz perdido, mas suerte la proxima vez!")
            PuntajeCompu = PuntajeCompu + 1
            
        print('Puntajes: Jugador:', MiPuntaje, ', Computadora:', PuntajeCompu)