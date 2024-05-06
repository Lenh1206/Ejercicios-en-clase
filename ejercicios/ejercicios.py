nombre = ""
while nombre == "" or nombre.isspace():
	print("El nombre no puede estar vacio")
	nombre = input("Escribe un nombre: ")




#Escribir un programa que pregunte el nombre de un producto, su precio y un número de unidades y 
#muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros
#y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

product = str(input('¿Cuál es el nombre del producto? \n'))
price = float('Cuál es su precio')
units = int('Cuantas unidades son')
total = float(price * units)

