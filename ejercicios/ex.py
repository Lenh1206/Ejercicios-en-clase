

#Escribir un programa que pregunte al usuario una
#cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

print(2**2)

ci = float(input('Introduzca la cantidad inicial a invertir: '))
i = float(input('De cuanto es el interés anual: '))
n = int(input('Diga el número de años: '))
print('La ganancia final es de: ' + str(round(ci * (1 + i)**n, 2)))


#num = int(input("introduce un numero: "))
#num2 = int(input("introduce otro numero: "))
#division_result = str(num // num2)
#leftover = str(num % num2)
#print('Su cociente es: ' + division_result + f' y su resto es {leftover}')
