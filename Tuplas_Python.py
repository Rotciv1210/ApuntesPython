#Tuplas en Python
#al igual que las listas, las tuplas sirven para almacenar items en una sola varuable, son ordenadas y no se pueden cambiar

miTupla = ("manzana", "platano", "cereza")
print(miTupla)
print("--------------")

#Se pueden crear tuplas de un solo valor, pero tienen que llevar una coma

tuplaSolitaria = ("manzana",)
print(len(tuplaSolitaria))
print("--------------")

#se pueden crear utilizando el constructor

otraTupla = tuple((1,23,3))
print(otraTupla)

#Acceso a tuplas
print(miTupla[1]) #Accede al segundo item de la tupla
print("--------------")

print(miTupla[2:5]) #Accede al rango del 2 y el 5
print("--------------")

print(miTupla[:2]) #Accede a los ultimos a partir del 2
print("--------------")

#Para poder cambiar los valores de las tuplas, antes hay que convertirlas a listas

x = ("Switch", "Xbox", "PS5")

y = list(x)

y[1] = "Perro"

x = tuple(y)

print(x)