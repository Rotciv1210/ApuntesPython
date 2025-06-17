#BOOLEANOS EN PYTHON
#Los boolenanos representan dos valores --> TRUE o FALSE
print(10>9)#True
print(10==9)#False
print(10<9)#False
print("--------------")
#Ejemplo con un condicional
a = 200
b = 33

if b > a:
    print("B es mas grande que A")
else:
    print("B es mas pequeño que A")
print("--------------")
    
#La funcion bool() permite evaluar cualquier valor y devolvera TRUE o FALSE
print(bool("Hola"))
print(bool(15))
print("--------------")

#La mayor parte de valores siempre van a devolver TRUE
#-Cualquier String es TRUE salvo los vacios
#-Cualquier INT es TRUE salvo 0
#-Cualquier Lista, Tupla, Set, Diccionario, etc. es TRUE salvo los vacios

#Hay un valor que siempre va a evaluar a FALSE, y es cuando tienes un objeto en una clase con una funcion __len__ que retorna 0 o FALSE
class miClase():
    def __len__(self):
        return 0
miObjeto = miClase()
print(bool(miObjeto))
print("--------------")

#Python tiene tambien funciones ya hechas que retornar el valor del booleano, isinstance(), que determina si un objeto es de cierto tipo de dato
x = 200
print(isinstance(x, int)) #Comprueba si x es un INT
