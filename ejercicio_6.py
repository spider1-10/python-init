#EJERCICIO 6.   Contar letras, dígitos y otros caracteres en una cadena
# Desarrolla un programa que cuente el número de letras, dígitos y otros 
# caracteres (espacios, símbolos, etc.) en una cadena dada por el usuario 
# (***Hacer uso de isalpha(), isdigit()***).
'''
texto = input("Ingrese texto: ")
dig = 0
letras = 0
for i in texto:
    if i.isdigit():
        dig += 1
        dig = i
    elif i.isalpha():
        letras += 1
        letras = i
    else:
        pass
R = i
print(f"Cantidad de digitos: {R}")
print(f"Cantidad de letras: {R}")
'''

def contar_digitos_letras(cadena):
    digitos = 0
    letras = 0
    
    for i in cadena:
        if i.isdigit():
            digitos += 1
        elif i.isalpha():
            letras += 1
        else:
            pass
    return digitos,letras

texto = input("Ingrese texto: ")
R = contar_digitos_letras(texto)

print(f"Cantidad de digitos: {R[0]}")
print(f"Cantidad de letras: {R[1]}")
