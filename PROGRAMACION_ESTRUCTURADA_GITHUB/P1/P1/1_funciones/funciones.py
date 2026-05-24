
"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""
#Funcion o procediciemto que borre pantalla 
def borrarPantalla():
    print("\033c")
#1.- Funcion que no recibe parametros y no regresa valor
def funcion1():
    borrarPantalla()
    nombre=input("Escribe el nombre: ").strip().upper()
    apellidos=input("Escribe el apellidos: ").strip().upper()
    print(f"Nombre completo del alumno es: {nombre} {apellidos}")
funcion1()
 #3.- Funcion que recibe parametros y no regresa valor 
def funcion3(nom,ape):
    borrarPantalla()
    nombre=nom
    apellidos=ape
    print(f"Nombre completo del alumno es: {nombre} {apellidos}")
funcion3("Fernanda","Ruvalcaba")

 #2.- Funcion que no recibe parametros y regresa valor
def funcion2():
    borrarPantalla()
    nombre=input("Escribe el nombre: ").strip().upper()
    apellidos=input("Escribe el apellidos: ").strip().upper()
    return nombre,apellidos 

nom,ape=funcion2() 
print(f"Nombre completo del alumno es: {nom} {ape}")


 #4.- Funcion que recibe parametros y regresa valor
def funcion4(nom,ape):
    borrarPantalla()
    return nom,ape 
nom,ape=funcion4("Maria","Fernanda")
print(f"Nombre completo del alumno es: {nom} {ape}")

#Invocar las funciones

funcion1()

nombre=input("Nombre: ").strip().upper
apellidos=input("Apellidos: ").strip().upper()
funcion3(nombre,apellidos)

nombre.apellidos=funcion3()
print(f"El nombre del alumno es: {nombre}{apellidos}")

nombre=input("nombre: ").strip().upper() 
apellidos=input("Apellidos: ").strip().upper()
nom,ape=funcion4(nombre,apellidos)
print=(f"El nombre del alumno es: {nom}{ape}")


