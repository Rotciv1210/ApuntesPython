#Variables en python, no hay comandos para declarar variables y no hace falta asignarles un tipo (int, String, boolean, etc.)
x = 5 #Este es un entero
y = "Hola en Y" #Cadena de texto
print(x)
print(y)
print("----------------")
#Estos valores se pueden ir cambiando en funcion de que el codigo avanza, por ejemplo
x = "Hola en X"
y = 2
print(x)
print(y)
print("----------------")

#Castear una variable
#Si se quiere hacer que una variable tenga un tipo en especifico se puede hacer casteandola antes
x = str(3) #asi saldra "3", como si fuese un String
y = int(3) #Asi saldra como un entero
z = float(3) #Asi saldra como 3.0
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))
print("----------------")

#Para imprimir el tipo de una variable
x = 5
y = "Victor"
print(type(x))
print(type(y))
print("----------------")

#Python hace distincion de mayusculas o minusculas a la hora de asignar las variables
a = "esta es la variable a como minuscula"
A = "esta es la variable A como MAYUSCULA"
print(a)
print(A)
print("----------------")

#Se pueden asignar varias variables en una sola linea
x , y , z = "Victor", "Carmen", "Max"
print(x)
print(y)
print(z)
print("----------------")

#Asi tambien se puede asignar el mismo valor a distinas variables en una sola linea
x = y = z = "Valor de X Y Z"
print(x)
print(y)
print(z)
print("----------------")

#Si hay una coleccion, le puedes asignar a una variable esa coleccion
deportes = ["futbol", "baloncesto", "tenis"]
x = deportes #Asi se asigna toda la coleccion
y = deportes[0] #Asi se asigna un valor en concreto
print(x)
print(y)
print("----------------")
