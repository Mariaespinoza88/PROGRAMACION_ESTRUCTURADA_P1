'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones
  num=float(input("Ingresa el numero que deseas multiplicar: "))
con=num+1
r1=num*con
print(f"{num}x{con}={r1}")
'''

'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones

'''
"""
print("\033c")


numtabla=int(input("Numero de la tabla de multiplicacion: "))

for num in range(1,11): 
   multi= numtabla*num
   print(f"{numtabla}x{num}= {multi}")
 """
'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras while
  2.- Sin funciones


numtabla=int(input("Numero de la tabla de multiplicacion: "))
num=1
while num<11:
   multi= numtabla*num
   print(f"{numtabla}x{num}= {multi}")
   num+=1

'''
  
'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- con funciones

'''

"""
print("\033c")
def ntabla(numtabla,num):
   multi= numtabla*num
   print(f"{numtabla}x{num}= {multi}")
   num+=1
   return num
    

numtabla=int(input("Numero de la tabla de multiplicacion: "))
num=1


num=ntabla(numtabla,num)
num=ntabla(numtabla,num)
num=ntabla(numtabla,num)
num=ntabla(numtabla,num)
num=ntabla(numtabla,num)
num=ntabla(numtabla,num)
num=ntabla(numtabla,num)
num=ntabla(numtabla,num)
num=ntabla(numtabla,num)
num=ntabla(numtabla,num)

"""


'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- con estructuras de control for
  2.- con funciones
'''


print("\033c")
def ntabla(numtabla,num):
 numtabla=int(input("Numero de la tabla de multiplicacion: "))
 respuesta=numtabla*num
 return respuesta
   

for i in range(10,0,-1):
  numtabla , num=ntabla(numtabla,num)

  

