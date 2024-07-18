#5.   Juego de adivinar el número
# Escribe un programa que genere un número aleatorio entre 1 y 100. 
# Luego, pide al usuario que adivine el número. El programa debe dar 
# pistas si el número ingresado es mayor o menor que el número aleatorio. 
# El juego termina cuando el usuario adivina el número correctamente (***Puede usar random***).

import random

numero_aleatorio = random.randint(0,100)

while True:
    n = int(input("Ingrese numero entre [1 - 100]: "))
    if numero_aleatorio == n:
        print(f"Adivinaste el numero: {numero_aleatorio}")
        break
    elif numero_aleatorio > n:
        print(f"{n} es menor")
    else:
        print(f"{n} es mayor")

print("***fin del juego***")