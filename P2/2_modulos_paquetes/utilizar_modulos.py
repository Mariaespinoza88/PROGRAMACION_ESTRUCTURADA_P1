# 1er utilizar los modulos 
#Se pone , si desea agregar otro archivo
"""
import modulos
modulos.borrarpantalla
modulos.funcion1

nom="Fernanda"
ape="Ruvalcaba"

modulos.funcion3

nombre,apellidos=modulos.funcion4(nom,ape)
print(f"Nombre:  {nombre}\nApellidos: {apellidos}")
"""
#2da formar de utilizar modulos

from modulos import borrarpantalla, funcion4

modulos.borrarpantalla():

nom="Daniel"
ape="Carreom"

nombre,apellido=modulos.funcion4(nom,ape)
print(f"Nombre:  {nombre}\nApellidos: {apellidos}")
