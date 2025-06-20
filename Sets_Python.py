#Sets en Python
#Los sets sirven para almacenar multiples items en una sola variable, un set no esta ordenado, no se puede cambiar y no esta indexado.

set1 = {"manzana", "platano", "mango"}
print(set1)
print("--------------")

#En los sets no se aceptan duplicados
set2 = {"Manzana", "Manzana", "platano"}
print(set2) #Solo imprime una vez el valor manzana
print("--------------")

#Los valores True y 1 son considerados el mismo y seran tratados como duplicados
set3 = {"Manzana", True, 1, 2}
print(set3)
print("--------------")

#Los valores False y 0 son considerados el mismo y seran tratados como duplicados
set4 = {False, 0, 1}
print(set4)
print("--------------")

#Obtener la longitud de un set
print(len(set1))
print("--------------")

#Otra sintaxis para crear un set
set5 = set((1,2,3,4))
print(set5)
print("--------------")

#Acceso a los items de un set
frutas = {"manzana", "platano", "mango"}
for fruta in frutas:
    print(fruta)
print("--------------")

#Comprobar si existe en el set
print("manzana" in frutas)
print("platano" not in frutas)
print("--------------")

#UNA VEZ EL SET ESTA CREADO NO PUEDES CAMBIAR LOS ITEMS, PERO SI PUEDES AÑADIR NUEVOS
#Añadir items al set
frutas.add("naranja")
print(frutas)
print("--------------")

#Añadir un set a otro set
frutas_Tropicales = {"piña", "papaya"}
frutas.update(frutas_Tropicales)
print(frutas)
print("--------------")

#El item que se añade con el metodo update() no tiene porque ser otro set, puede ser un objeto iterable (listas, diccionarios, tuplas etc.)
lista = [1,2,3]
frutas.update(lista)
print(frutas)
print("--------------")

#Como eliminar items de un set
frutas.remove("manzana") #Si el objeto no existe dara error
print(frutas)
print("--------------")

#Otra forma de eliminar de un set
frutas.discard("platano")
print(frutas)
print("--------------")
#Con el metodo discard() si el item no existe NO dara error

#El metodo pop() eliminar un item random del set, por lo que no puedes estar seguro de cual va a eliminar
x = frutas.pop()
print(x)
print(frutas)
print("--------------")

#Para "limpiar" un set (eliminar todos los valores) se usa el metodo clear()

set1.clear()
print(set1)
print("--------------")

#Para eliminar un set por completo se usa la palabra clave del
del set2
#print(set2) #Como se ha eliminado este print dara error

#Iterar sets

#Bucle for
juegos = {"COD", "FIFA", "Pokemon"}

for juego in juegos: 
    print(juego)
print("--------------")

#Juntar sets

'''
Los metodos union() y update() juntan todos los items de los dos sets
El metodo intersection() mantiene SOLO los duplicados
El metodo difference() mantiene los items del primer set que no estan en otros sets
El metodo symmetric_difference() mantiene TODOS los items EXCEPTO los duplicados
'''
consolas = {"XBOX", "PS5", "Nintendo Switch"}
juegos_consolas = juegos.union(consolas) #En vez de usar el metodo union() se puede usar el operador | 
print(juegos_consolas)
print("--------------")

#A los sets se le pueden unir otro tipo de datos, como listas o tuplas

x = {1,2,3}
y = ("a", "b", "c")

z = x.union(y)
print(z)
print("--------------")

#Metodo update()

ciudades = {"A Coruña", "Vigo", "Lugo"}
paises = {"España", "Italia", "Japon"}

ciudades.update(paises)
print(ciudades)
print("--------------")

#Metodo intersection()

cosas1 = {"manzana", "pera", "platano"}
cosas2 = {"verde", "eevee", "manzana"}

cosas = cosas1.intersection(cosas2) #En lugar del metodo intersection() se puede usar el operador &
print(cosas) #Solo mantiene manzana
print("--------------")

#Metodo intersection_update()

animales = {"perro", "gato", "elefante"}
random = {"Coruña", "Pokemon", "gato"}

animales.intersection_update(random)
print(animales) #Mantiene solo los duplicaods pero cambiara el set original en vez de crear uno nuevo
print("--------------")

#Metodo difference()
ejemplo1 = {"platano", "cereza", "mango"}
ejemplo2 = {"Yuumi", "Adidas", "mango"}

ejemplo = ejemplo1.difference(ejemplo2) #devuelve un set que contiene solo los items del primero que no estan presentes en el segundo. Se puede usar el operador -
print(ejemplo)
print("--------------")

#Metodo difference_update()
ejemplo3 = {"CocaCola", "Pepsi", "Sprite"}
ejemplo4 = {"Pepsi", "Max", "Hola"}

ejemplo3.difference_update(ejemplo4) #En vez de retornar un set nuevo, actualiza el set con los items que no estan en el segundo
print(ejemplo3)
print("--------------")

#Metodo symmetric_difference()

ejemplo5 = {"LOL", "CSGO", "WOW"}
ejemplo6 = {"Fortnite", "Mario Kart", "CSGO"}

ejemplo7 = ejemplo5.symmetric_difference(ejemplo6) #Mantiene los elementos que no estan presentes en ninguno de los dos sets. Tambien se puede usar el operador ^ 
print(ejemplo7)
print("--------------")

#Metodo symmetric_difference_update()
ejemplo8 = {"Zar", "Yuumi", "Blanca"}
ejemplo9 = {"Max", "Sayu", "Blanca"}

ejemplo8.symmetric_difference_update(ejemplo9) #Mantiene los elementos que no estan presentes en ninguno de los dos sets.
print(ejemplo8)
print("--------------")
