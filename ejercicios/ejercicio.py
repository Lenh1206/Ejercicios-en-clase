#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

contraseña = str(input('Introduzca su contraseña: \n'))
password_validation2 = str(input('Confirme su contraseña: \n'))
if contraseña.lower() == password_validation2.lower():
    print ('Puede continuar...')
else: print ('La contraseña no coincide')


year = int(input('¿En que año estas?'))
otheryear = int(input('dime otro año distinto'))

if year > otheryear:
    print ('han pasado ', str(year - otheryear), ' años')
else:
    print ('faltan ', str(otheryear - year), 'años')



print ('Bienvenido a la pizzeria Bella Napoli! ')
typeofpizza = int(input('\n Indique que tipo de pizza desea ordenar \n 1. Vegetariana \n 2. Corriente \n'))
if typeofpizza == 1:
    typeofpizza = 'vegetariana'
    ingredients = int(input('\n Los ingredientes disponibles son: \n 1. Pimiento \n 2. Tofu \n'))
    if ingredients == 1:
        ingredients = 'Pimiento'
        print ('Su pizza es ', typeofpizza, ' y contiene ', ingredients)
    elif ingredients == 2:
        ingredients = 'Tofu'
        print ('Su pizza es ', typeofpizza, ' y contiene ', ingredients)
    else: print ('No hay ingredientes correspondientes a ese número')
elif typeofpizza == 2:
    typeofpizza = 'Corriente'
    ingredients = int(input('\n Los ingredientes disponibles son: \n 1. Pepperoni \n 2. Jamón \n 3. Salmón \n'))
    if ingredients == 1:
        ingredients = 'Pepperoni'
        print ('Su pizza es ', typeofpizza, ' y contiene ', ingredients)
    elif ingredients == 2:
        ingredients = 'Jamón'
        print ('Su pizza es ', typeofpizza, ' y contiene ', ingredients)
    elif ingredients == 3:
        ingredients = 'Salmón'
        print ('Su pizza es ', typeofpizza, ' y contiene ', ingredients)
    else: print ('No hay ingredientes correspondientes a ese número')
else: print ('error')
















age = int(input('introduzca su edad: '))
if age < 4:
    price = 0
elif age >= 4 and age <= 18:
    price = 5
else: 
    price = 10
print ('El precio de su estrada es de ' + str(price) + '€')    


renta = int(input('Introduzca su renta anual: \n '))
if renta < 10000:
    print ('su tipo de impositivo es de 5%')
elif renta >= 10000 and renta < 20000: 
    print ('su tipo de impositivo es de 15%')
elif renta >= 20000 and renta < 35000: 
    print ('su tipo de impositivo es de 20%')
elif renta >= 35000 and renta < 60000: 
    print ('su tipo de impositivo es de 30%')
else: print ('su tipo de impositivo es de 45%')

age = int(input('introduce tu edad: '))
earnings = int(input('introduce tus ingresos:'))

if age > 16 and earnings >= 1000:
    print ('usted tiene que tributar')
else:
    print ('usted no tiene que tributar')    



password = input(str('Introduzca su contraseña: '))
password_validation = input(str('repita su contraseña:'))
if password.lower() == password_validation.lower():
    print ('La contraseña coincide')
else: 
    print ('La contraseña no coincide')







age = input('Introduce your age:\n')
if int(age) < 18 :
    print ('Es menor de edad')
else : print ('Es mayor de edad')



