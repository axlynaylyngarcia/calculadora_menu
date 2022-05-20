# calculadora básica con menú 

from math import log

#input
bandera = False 
x = float(input("Dame el valor del número x: "))
y = float(input("Dame el valor del número y: "))

print("Dame la opción que deseas realizar: \n")

# Se despliega el menú para seleccionar la opción que deseas realizar
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Potencia")
print("6. Logaritmo")

opción = int(input("Dame la opción: "))

#processing
if (opción == 1):
    z = x + y 
    print(x, " + ",y)
elif (opción == 2):
    z = x - y
    print(x, " - ",y)
elif (opción ==3):
    z = x * y
elif (opción == 4 and y != 0):
    z = x/y
    print(x, " / ",y)
elif (opción == 4 and y == 0):
    print("El denominador es igual a cero y ")
    print("NO se puede realizar la divisi+on")
    bandera = True
elif (opción == 5):
    z = pow(x,y)
    print(x, " ^ ",y)
elif (opción == 6 and x > 0):
    z = log(x) 
    print("Logaritmo de ", x)
elif (opción == 6 and x <= 0):
    print("NO se puede calcular el logaritmo.")
    bandera = True 
else:
    print("opción no válida")

# Se escribe el resultado con otra condición
if (opción < 7 and bandera == False):
    print("Resultado = ", z)
    
#fin