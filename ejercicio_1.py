#*****Estructuras Condicionales*****
#Ejercicio 1:  Determinar el tipo de triángulo
#Escribe un programa que solicite al usuario ingresar las longitudes de los lados de un triángulo. 
#El programa debe determinar si el triángulo es equilátero (todos los lados son iguales), 
# isósceles (dos lados son iguales) o escaleno (todos los lados son diferentes).

lado1 = int(input("Ingrese lado 1: "))
lado2 = int(input("Ingrese lado 2: "))
lado3 = int(input("Ingrese lado 3: "))

if lado1 == lado2 and lado1 == lado3:
    print("Es un triangulo EQUILATERO")
elif lado1 == lado2:
    print("El triangulos es ISOSCELES")
elif lado1 == lado3:
    print("El triangulos es ISOSCELES")
elif lado2 == lado3:
    print("El triangulos es ISOSCELES")
else:
    print("El triangulo es ESCALENO")
        

