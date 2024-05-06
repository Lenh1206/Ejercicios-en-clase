"""""
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si 
l divisor es cero el programa debe mostrar un error.
"""

num1 = int(input("introduzca un número: \n"))
num2 = int(input('introduzca otro numero: \n'))
division = num1 // num2
if num2 == 0:
    print('Error, no se puede dividir entre cero.')
else: print('la division es igual a: ' + str(num1 // num2))

##########################################
"""""
Solicita al usuario que ingrese los coeficientes a, b y c de una ecuación cuadrática de la forma ax^2 + bx + c = 0.

Calcula el discriminante de la ecuación, que se define como b^2 - 4ac.

Muestra el valor del discriminante y explica su significado (si es negativo, positivo o cero). 
Un discriminante positivo indica que la cuadrática tiene dos soluciones reales distintas. Un discriminante de 
cero indica que la cuadrática tiene una solución real repetida. Un discriminante negativo indica que ninguna de
las soluciones son números reales.
"""""
a = int(input('valor de a?: \n'))
b = int(input('valor de b?: \n'))
c = int(input('valor de c?: \n'))

discriminant_value = (b)**2 - (4*a*c)
if discriminant_value < 0:
    discriminant = f'Tu discriminante es {discriminant_value}. Al ser negativo la solución no pertenece al conjunto de los numeros reales.'
elif discriminant_value == 0:
    discriminant = f'Tu discriminante es {discriminant_value}. Al ser 0 la ecuación tiene una solución real repetida.'
else: discriminant = f'Tu discriminante es {discriminant_value}. La ecuación tiene dos soluciones reales distintas.'
print(discriminant)

##########################################

h = 'hola'
m = 'mundo'
print(h, m)
######################################################

'''
Pide al usuario que ingrese la base y la altura de un rectángulo.
Calcula el área y el perímetro del rectángulo y muestra los resultados.
La fórmula para calcular el área de un rectángulo es: A = base * altura.
La fórmula para calcular el perímetro de un rectángulo es: P = 2 * (base + altura).
'''
base = int(input('introduzca la base del rectangulo: \n'))
hight = int(input('introduzca la altura del rectangulo: \n'))
area = base * hight
perimeter = 2 * (base + hight)
print('El area del rectangulo es de ' + str(area) + ' y su perimetro es de '+ str(perimeter))



################################################

birth = int(input('Introduce your birthyear: '))
age = 2024 - birth
if age < 13:
    life_stage = 'infancy'
elif age >= 13 and age < 20:
    life_stage = 'adolescense'
elif age >= 20 and age < 65:
    life_stage = 'adulty'
else: life_stage = 'third age'
print ('Your life stage is {} and your age is {}'.format(life_stage, age))

#############################
salario = int(input('Diga su salario como profesor: \n'))
if salario < 18000:
    incremento = 0.12
elif salario >= 18000 or salario <= 30000:
    incremento = 0.08
elif salario > 30000 or salario <= 50000:
    incremento = 0.07
else: incremento = 0.06
print('Su incremento salarial es de {}, y su nuevo salario es de {}'.format(incremento, (salario + (salario*incremento))))