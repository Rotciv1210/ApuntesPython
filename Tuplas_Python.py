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
print("--------------")

#"Desmontar" tuplas
#Esto es asignar variables independientes a los valores de las tuplas
frutas = ["manzana", "platano", "mango"]
(a, b ,c) = frutas
print(a)#Manzana
print(b)#Platano
print(c)#Mango
print("--------------")

#El * se usa cuando el numero de variables es menor al numero de valores, por lo que el * asignara los valores como una lista
ciudades = ["A Coruña", "Vigo", "Madrid", "Barcelona"]
(d, e, *f) = ciudades
print(d)#A Coruña
print(e)#Vigo
print(f)#Lista con los valores que faltan (Madrid, Barcelona)
print("--------------")

#Si el asterisco se usa en una variable distinta de la ultima, Python asignara valores a la variables hasta que el numero de valores restantes sea igual al numero de variables restantes
colores = ["rojo", "negro", "blanco", "amarillo", "azul"]
(g, *h, i) = colores
print(g)#Rojo
print(h)#Negro, blanco y amarillo como una lista
print(i)#Azul
print("--------------")
 
#Iterar tuplas

#Con bucle for
nombres = ["Victor", "Carmen", "Javier", "Diego"]
for nombre in nombres:
    print(nombre)
print("--------------")

#Iterar los indices de la tupla
for indice in range(len(nombres)):
    print(nombres[indice])
print("--------------")

#Usando while
indice = 0
while indice < len(nombres):
    print(nombres[indice])
    indice = indice +1
print("--------------")

#Juntar tuplas
#Se usa el operador +

tupla1 = (1,2,3)
tupla2 = ("a", "b", "c")

tupla3 = tupla1 + tupla2
print(tupla3)
print("--------------")

apellidos = ("Pereira", "Garcia", "Vallejo")
apellidosMultiplicados = apellidos *2
print(apellidosMultiplicados)
print("--------------")