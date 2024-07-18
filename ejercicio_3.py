#****Ejercicio 2: Estructuras Repetitivas****

#EJERCICO 3.   Generar números primos hasta un límite
# Escribe un programa que pida al usuario ingresar un número 
# entero positivo n. Luego, genera todos los números primos 
# desde 2 hasta n
   
num = int(input("ingrese numero: "))
for n in range(1,num+1):   
    if n > 1:
        contador = 0
        i = 2
        while i < n and contador == 0:
            resto = n % i
            if resto == 0:
                contador += 1
            i += 1
        if contador == 0:
            print(n)            
     
               
            
 