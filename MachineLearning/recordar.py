import numpy as np
import pandas as pd
## Strings como listas----------------
print ("Strings como listas")
s_lista = "String como lista!"
#Char en posicion x
print(s_lista[2])
print(s_lista[-1])
# recorridos
print(s_lista[-5:-1])
print(s_lista[0:-1:2])
print(s_lista[-3:-9:-2])
print(s_lista[::2])#elementos pares
#reverse
print(s_lista[::-1])

## Metodos de strings-----------------

print("Metodos de String")


#Format
s1 = "Metodo"
s2= "format"
union = "El {} de {}".format(s1, s2)
print(union)

#Mayusculas y minusculas
union = union.upper()
print(union)

union = union.lower()
print(union)

#Title (mayusculas al inicio de cada palabra)
union = union.title()
print(union)

#busqueda

posicion = union.find("De")
print(posicion)

#contar char en string

print(union.count("o"))

#sustitucion

string_sustituido = union.replace("o", "ç")
print(string_sustituido)

#slip
split = union.split(" ")


##Listas--------------------

lista1 = np.linspace(0,100,101)


with open('archivito.txt', 'r') as myfile:
 	archivito = myfile.read()
l = archivito.split(" ")
for var in range(len(l)):
	print(l[var])

l.extend(["mas", "dos", "y"])
l.append("dos")
l.insert(4,"pn")
l.index("pn")
l.remove("pn")
l.pop(-3) 
len(l)#tamaño
set(l) #dibuja lista sin repeticiones de elementos
l.count("Dos")
min(lista1)
max(lista1)

#Tupla (lista constante)

tup = ("tupla", lista1)

#conversiones

t = tuple(lista1)
nl= list(t)
print(nl==lista1) #ojo, cosas raras :v

#Diccionarios (no se rige por indices, sino por claves) claves inmutables
diccionario = {"buenos dias" : "ohaio", 'dexterrainbow@gmail.com' : '99Happy9'}
d2 = {0 : False, 1 : True}
diccionario[1] = "nuevo string" #añadir elemento/modificar si ya existe
valor = d2.get(2, False)#regresa valor de 2 o False
del diccionario['dexterrainbow@gmail.com'] #elimina elemento

llaves = d2.keys()
key = list(llaves)
valores = d2.values()
val = list(valores)

diccionario.update(d2)

#list comprenhension 

lc = [valor for valor in range(0, 100+1)]
lc2 = ["string" for valor in range(0, 100+1)]
pares = [valor for valor in range(0, 100+1) if valor%2 == 0]

#print(lc, "\n", lc2)