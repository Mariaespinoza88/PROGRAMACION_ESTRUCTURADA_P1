import funciones

#pelis={
# nombre": "Toy Story",
#       "duracion": "120 min",
#       "idioma": "Español",
#       "clasificacion": "A",
#       "genero": "animada",
#}

#los dic solo puede tener 1 
      
def menuPrincipal():
    print("\n\t\t...:::: M E N U  P R I N C I P A L ::::...\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe un opcion: ").strip()
    return opcion

def agregarPeliculas(pelis):
    print("\n\t\t...:::: AGREGAR CARACTERISTICAS DE UNA PELICULA ::::...\n")
    opc="si"
    while opc=="si":
     caracteristica=input("Introducir el nombre de la caracteristica: ").lower().strip()
    valor=input("Introducir el valor de la caracterisitica: ").upper().strip()
    pelis[caracteristica]=valor
    opc=""
    while opc!="si" and opc!="no":
     opc=input("¿Deseas agregar otra caracteristica (Si/No)? ").lower().strip()
    funciones.accionExitosa()
      #opc="" es para entrar al while, es lo que ayusa a regresar 


       
def mostrarPeliculas(pelis):
    print("\n\t\t...:::: MOSTRAR CARACTERISTICAS DE LA PELICULA::::...\n")
    if len(pelis)>0:
       print("\tCaracteristica\t\tValor\n")
       for i in pelis:
         print(f"{i}\t\t{pelis[i]}")
    else:
        input("\n\t...¡No hay caracteristicas a mostrar!. Verifique...")
        funciones.espereTecla()
    
    
def limpiarPeliculas(pelis):
    if len(pelis)>0:
        opc =""
        while opc!="si" and opc!="no":
          opc=input("¿Deseas borrar TODAS las caracteristicas (Si/No)? ").lower().strip()
        if opc == "si":
          pelis.clear()
          funciones.accionExitosa()
    else:
        input("...¡No hay peliculas que borrar!...") 
        
#len revisar todos los datos. es la longitud de la lista.


def buscarPeliculas(pelis):
    print("\n\t\t...:::: BUSCAR PELICULAS ::::...\n")
    peli=input("Escribir el nombre de la pelicula: ").lower().strip()
    noencontre =  True
    for i in pelis:
     #CADA ATRIBUTO QUE TIENE
     if i == pelis:
        print(f" la caracteristica es: {peli} y su valor es {pelis}")
        funciones.espereTecla()
        noencontre=False
    if noencontre:
        input("...¡No exite la pelicula que estas buscando, verifique!...")

        #noenconttre es una funcion bandera 

def borrarPeliculas(pelis):
    print("\n\t\t...:::: BORRAR PELICULAS ::::...\n")
    peli=input("Escribir el nombre de la pelicula: ").lower().strip()
    noencontre=True
    for i in pelis: 
        if peli==i:
         noencontre=False
         opc=""
         while  opc!="si" and opc!="no":
                  opc=input("¿Deseas borrar las caracteristicas pelicula (Si/No)? ").lower().strip()
        if opc=="si":
            caracteristica=peli
    if noencontre:    
        input("...¡No exite la pelicula que estas buscando, verifique!...")
    else:
       pelis.pop(caracteristica)
       funciones.accionExitosa
        
def modificarPeliculas(pelis):
    print("\n\t\t...:::: MODIFICAR EL VALOLR DE LA CARACTERISTICA ::::...\n")
    peli=input("Escribir el nombre de la pelicula: ").lower().strip()
    noencontre=True
    for i in pelis: 
        if peli==i:
         noencontre=False
         print(f"La caracteristica a buscar es: {peli} y su valor actual es: {pelis[peli]}")
         opc=""
         while  opc!="si" and opc!="no":
                  opc=input("¿Deseas modificar las caracteristicas pelicula (Si/No)? ").lower().strip()
        if opc=="si":
            pelis[peli]=input("Escribe el nuevo valor de esta caracteristica: ").upper().strip()
        
            caracteristica=peli
    if noencontre:    
        input("...¡No exite la pelicula que estas buscando, verifique!...")
    else:
       pelis.pop(caracteristica)
       funciones.accionExitosa


    # posiciones=[]
    # print("\n\t\t...:::: MODIFICAR PELICULAS ::::...\n")
    # peli=input("Escribir el nombre de la pelicula: ").upper().strip()
    # if peli in pelis:
    #     for i in range(0,len(pelis)):
    #         if peli==pelis[i]:
    #             opc=""
    #             while opc!="si" and opc!="no":
    #               opc=input("¿Deseas modificar la pelicula (Si/No)? ").lower().strip()
    #             if opc=="si":
    #               pelis[i]=input("Escribe el nuevo nombre: ").upper().strip()
    #               funciones.accionExitosa()
    # else:
    #     input("...¡No existe la pelicula que estas buscando, verifique!...")cc