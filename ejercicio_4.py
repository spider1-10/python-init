#EJERCICIO 4.   Calcular el factorial de un número
# Desarrolla un programa que pida al usuario ingresar un número entero 
# no negativo. Luego, calcula y muestra el factorial de ese número. 
  
n = int(input("ingrese numero: "))
if n >= 0:
    i = 1
    fac = 1 
    while i <= n:
        fac = fac * i
        i += 1  
    print(f"factorial de {n}! es: {fac}")    
else:
    print("INGRESE NUMERO POSITIVO...!!") 
    