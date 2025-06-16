#String en python

print("Hola")
print("----------------")

#Se pueden asignar a variables
a = "Victor"
print(a)
print("----------------")

#Se pueden considerar como arrays
a = "Hola, Mundo!"
print(a[1])
print("----------------")

#Como son considerados arrays, se pueden loopear con un for
for x in "platano":
    print(x)
#esto deletreara la palabra platano
print("----------------")

#Para saber la longitud de un String
a = "Que pasa?"
print(len(a))
print("----------------")

#Para verificar si una palabra o un caracter esta dentro del string
texto = "Me gusta el chocolate"
print("chocolate" in texto) #Esto devolvera true si chocolate esta en el texto
print("----------------")

#Se puede verificar con un if
texto = "Estoy aprendiendo en Python?"
if "Python" in texto:
    print("Si, lo estas haciendo")
print("----------------")

#Ahora a la inversa, para comprobar si no esta
texto = "Todo lo gratis es bueno"
print("caro" not in texto) #Devuelve true si caro no esta en el texto
print("----------------")

#Con un if
texto = "El mejor lenguaje de programacion es JAVA"
if "Python" not in texto:
    print("No, Python es el mejor")     
print("----------------")

#Castear a mayusculas o minusculas
texto = "este texto va en mayusculas"
print(texto.upper())
texto2 = "ESTE TEXTO VA EN MINUSCULAS"
print(texto2.lower())
print("----------------")

#Formatear Strings. Se utiliza f antes de asignar el string y se usan las {} como placeholders para variblaes u otras operaciones
edad = 24
texto = f"Mi nombre es Victor y tengo {edad} años"
print(texto)
print("----------------")

precio = 100
texto = f"El precio es de {precio}€"
print(texto)
print("----------------")
#En las {se puede hacer operaciones comos sumas, restas, etc.}
texto = f"El precio es de {precio:.2f}€" #Añade dos decimales
print(texto)
print("----------------")
texto = f"El precio es de {precio * 10}€" #Multiplica por 10 el precio
print(texto)
print("----------------")

#Entrecomillar caracteres
texto= "We are the so-called \"Vikings\" from the north."
print(texto)
