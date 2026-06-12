"""  
 List (Array)
 son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""

print("\033c")
# #Funciones más comunes en las listas
# paises= ["México","Canada","EUA",",Mexico","Brasil"]
# numeros=[23,45,8,24]
# varios=[33,3.1416,"Hola",True]
# vacio=[]

#Imprimir el contenido de una lista

# print(paises)
# print(numeros)
# print(varios)
# print(vacio)
# print(paises[1])
# print(paises[0]+paises[3])


#Recorrer la lista 
#1er forma 
# for i in paises: 
#     print(i)


# # #2do forma 
# for i in range(0,5):
#     print(paises[i])


paises= ["México","Canada","EUA","Mexica","Brasil"]
print(paises)
#ordenar elementos de una lista
  #Sort ordena de forma ascendente 
# paises.sort() 
# print(paises)


#dar la vuelta a una lista
#Metodos de ordenamiento, reverse solo le da la vuelta a la lista
# paises.reverse()
# print(paises)


#Agregar, insertar, Añadir un elemento a una lista
#1er forma 
paises.append("yuyui")
print(paises)

# #2da forma
# paises.insert(1,"Argentina")
# print(paises)
# paises.insert(100,"panama")
# print(paises)
# paises.insert(28,"jhgfcxfg")
# print(paises)
# paises.append(23)
# paises.append(3)
# print(paises)
# paises

#Eliminar, borrar, suprimir, un elemento de una lista
#1er forma
#.pop borra de la lista
# paises.pop(4)
# print(paises)
# paises.pop(3)
# print(paises)
# paises.pop(2)
# print(paises)
# paises.pop(1)
# print(paises)
# paises.pop(0)
# print(paises)
#2da forma 
#.remove borra los elementos escritos 
# paises.remove("EUA")
# print(paises)

#Buscar un elemento dentro de la lista
# buscar="Brasil" in paises
# print(buscar)

# buscar="Brasil" in paises
# if buscar==True:
#     print("Soy true")
# else:
#     print("soy False")  
# #Contar el numeros de veces que aparece un elemento dentro de una lista
# numeros=[23.45,24,8,23,50,23]
# # num=int(input("Dame un numero a contar: "))
# # cuantas=numeros.count(100)
# # print(f"El numero {num} aparece {cuantas} veces")


# #Conocer la posicion o indice en el que se encuentra un elemento de la lista
# posicion=numeros.index(50)
# print(f"Estoy en la posicion {posicion}")


#Unir el contenido de una lista dentro de otra lista
numeros1=[23.45,24,8,23,50,23]
numeros2=[100,-100]
numeros1.extend(numeros2)
print(numeros1)

#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenid ordenado descendentemente

numeros1.sort()
numeros1.reverse()
print(numeros1)
#reverse solo los voltea (no hay una funcion que los ordenme exactamente por eso se usa sort)



