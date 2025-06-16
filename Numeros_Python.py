import random

#Numeros en python
#Los INT son numeros enteros, positivos o negativos
x = 1
y = 34095730475
z = -20
print(x)
print(y)
print(z)
print("----------------")

#Los FLOAT son los numeros decimales, positivos o negativos
x = 1.0
y = 1.0
z = -235324.5000
a = -100e100 #La e significa potencia de 10
print(x)
print(y)
print(z)
print(a)
print("----------------")

#Los COMPLEX son los numeros que se escriben con una "j" como parte imaginaria, positivos o negativos
x = 3+5j
y = 5j
z = -5j
print(x)
print(y)
print(z)
print("----------------")

#Conversiones
x = 1    # int
y = 2.8  # float
z = 1j   # complex
#INT a FLOAT
a = float(x)
#float a int
b = int(y)
#int a complex
c = complex(x)
print(a)
print(b)
print(c)
print("----------------")
#Generar un numero aleatorio, se hace con la libreria random ---> import random
#generar un numero dentro de un rango
print(random.randrange(1,10))
print("----------------")
