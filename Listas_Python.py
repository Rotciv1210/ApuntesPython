#Listas en Python

#Las listas se utilizan para almacenar multiples valores en una sola variable

miLista = ["Manzana", "Naranja", "Platano"]
print(miLista)
print("--------------")

"""
Las listas son ordenadas, modificables y permiten valores duplicados.
Estan indexadas, el primer item es la posicion 0
Cuando se dice que estan ordenadas quiere decir que los items tienen un orden en especifico y ese orden no se va a cambiar.
Si añades items nuevos a la lista, estos iran al final.
"""

#Para determinar cuantos items componen una lista se utiliza la funcion len()
print("Mi lista tiene ", len(miLista), " objetos")
print("--------------")

#Las listas pueden contener cadenas de texto, numeros o booleanos, pueden contener cualquier tipo de dato

lista1 = ["Victor", "Javier", "Pedro", "Xabier"]
lista2 = [1,2,3,4]
lista3 = [True, False, True]
lista4 = ["Victor", 1 , True]
print(lista1)
print(lista2)
print(lista3)
print(lista4)

#Otra forma de crear listas es con el constructor list()

lista5 = list(("Manzana", "Pera", "Yogurt"))
print(lista5)
print("--------------")

#Para acceder a un indice de la lista
print(lista5[1])
print("--------------")

#Indices negativos el -1 refiere al ultimo item, el -2 al penultimo, etc.
print(lista5[-2])
print("--------------")

#Para acceder a un rango de indices
lista6 = ["manzana", "pera", "mango", "fresa", "naranja", "melon", "sandia"]
print(lista6[2:5]) #Esto mostrara los valores dentro del rango, el 3 4 y 5 
print(lista6[3:]) #Esto mostrara a partir del 3
print(lista6[:2]) #Esto mostrara los dos primeros
print("--------------")

#Para comprobar si un item esta en la lista
if "manzana" in lista6:
    print("Si, hay manzana")
else:
    print("No hay manzana")
print("--------------")


#Para cambiar valores dentro de una lista

lista7 = ["Coruña", "Vigo", "Ourense", "Santiago", "Viveiro"]
#lista7[2] = "Lugo"
#print(lista7)
#Para cambiar los valores dentro de un rango determinado
lista7[3:4] = ["Madrid" , "Barcelona"]
print(lista7)
#Para insertar valores en la lista
lista7.insert(6, "Gijon") #El 6 hace referencia al indice donde se va a colocar el item
print(lista7)
print("--------------")


#Agregar valores a la lista

lista8 = ["Oro", "Plata", "Rubi"]
lista8.append("Zafiro")
print(lista8)
#Añadir una lista a otra
lista9 = ["Esmeralda", "Platino", "Amatista"]
lista8.extend(lista9)
print(lista8)
print("--------------")
 
 #Para borrar
lista8.remove("Oro")
print(lista8)
#Borrar un valor de un indice especifico
lista8.pop(2) #Para borrar el ultimo item se podria dejar el pop vacio --> lista8.pop()
print(lista8)
del lista8[0] #Esto borra el indice especificado. Para borrar la lista completa ---> del lista8
print(lista8)

#Vaciar la lista
lista8.clear()
print(lista8)
print("--------------")

#Iterar listas

#Bucle for
lista10 = ["Nintendo Switch", "Xbox", "PS5"]
for x in lista10:
    print(x) #Esto itera cada valor de la lista y lo imprime
print("--------------")

for i in range(len(lista10)):
    print(lista10[i])   #Esto itera cada indice de la lista e imprime su valor
print("--------------")

#Usando WHILE. Itera los indices de la lista y devuelve el valor
i = 0
while i < len(lista10):
    print(lista10[i])
    i = i + 1 #Si no se añade esta linea hace un bucle infinito en el primer valor
print("--------------")

#Otra forma de hacer un bucle for con lista
[print(x) for x in lista10]
print("--------------")

#Comprension de listas
#Con una lista base, permite crear una lista basada en la anterior
frutas = ["Manzana", "Platano", "Cereza", "Kiwi", "mango"]
frutas_Nuevas = []

for x in frutas: 
    if "a" in x: 
        frutas_Nuevas.append(x) #Inserta en la nueva lista todas las frutas que contengan la vocal a
print(frutas_Nuevas)
print("--------------")
#Otra sintaxis --> frutas_Nuevas = [x for x in frutas if "a" in x] // nombreLista = [expresion for item in iterador if condicion == true]

#Meter frutas que no sean la manzana
frutas_NoManzana = [x for x in frutas if x != "Manzana"]
print(frutas_NoManzana)
print("--------------")

#Clasificar listas --> sort()
frutas.sort() #Las ordena alfanumericamente en forma ascendente. Para ordenarlos descendentemente --> frutas.sort(reverse = True)
print(frutas)

#Por defecto el metodo es case sensitive
frutas.sort(key = str.lower) #Para que no sea case sensitive
print("--------------")
#Ordenarlas aleatoriamente
frutas.reverse()
print(frutas)
print("--------------")

#Copiar listas
#3 Maneras. 1--> lista.copy(). 2--> miLista = list(lista). 3--> miLista = lista[:]
nuevasFrutas = frutas.copy()
#nuevasFrutas = list(frutas)
#nuevasFrutas = frutas[:]
print("--------------")

#Hacer un Join de las listas

juegos = ["Mario", "Zelda", "Pokemon"]
numeros = [1,2,3]

juegosNumeros = juegos + numeros
print(juegosNumeros)
print("--------------")

#Otra forma
for x in numeros:
    juegos.append(x)
print(juegos)
print("--------------")

#Otra forma
juegos.extend(numeros)
print(juegos)
print("--------------")
