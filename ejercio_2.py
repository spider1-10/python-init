#Ejercicio 2.   Calcular el salario neto con deducciones
# Crea un programa que solicite al usuario ingresar su salario bruto anual. El programa debe calcular y mostrar el salario neto después de aplicar las siguientes deducciones:
#   20% por impuestos si el salario es mayor a 50,000 Bolivianos
#   10% por impuestos si el salario está entre 30,000 y 50,000 Bolivianos.
#   Sin deducciones si el salario es menor o igual a 30,000 Bolivianos.

salario = int(input("Ingrese salario en Bs: "))

if salario > 50000:
    salario_neto = salario - salario * 0.20
    print(f"Salario neto: {salario_neto} Bs")
elif salario > 30000 and salario <= 50000:
    salario_neto = salario - salario * 0.10
    print(f"Salario neto: {salario_neto} Bs")
elif salario <= 30000:
    print(f"Salario neto: {salario} Bs")