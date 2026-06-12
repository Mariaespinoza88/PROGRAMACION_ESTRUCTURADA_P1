# Un módulo es simplemente un archivo con extensión .py que contiene código de Python (funciones, clases, variables, etc.).
def funcion1():
    nombre=input("Nombre: ").upper().strip()
    apellido=input("Apellidos: ").upper().strip()
    print(f"El nombre del alumno es: {nombre} {apellido}") 
    funcion1()
def funcion3(nom,ape):
    nombre=nom
    apellido=ape
    print(f"El nombre del alumno es: {nombre} {apellido}") 


 #2.- Funcion que no recibe parametros y regresa valor
def funcion2():
    nombre=input("Nombre: ").upper().strip()
    apellido=input("Apellidos: ").upper().strip()
    return nombre, apellido

 #4.- Funcion que recibe parametros y regresa valor
def funcion4(nom,ape):
    nombre=nom
    apellido=ape
    return nombre,apellido

def borrarpantalla():
 print("\033c")