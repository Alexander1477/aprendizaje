import math

pi = math.pi
radio = float(input("Introduce el radio del circulo: "))
diametro = radio * 2
circunferencia = diametro * pi
area = pi * radio ** 2
print(f"Diametro: {diametro}")
print(f"Circunferencia: {circunferencia}")
print(f"Area:{area}")