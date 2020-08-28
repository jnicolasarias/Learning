# 1. Crear lista con los parrafos del texto
archivo = open("the_raven_poe.txt")
lineas = archivo.readlines()
texto = ''.join(lineas)
x=texto.split("\n")
x.pop(0)
x.pop(2)
x.pop(3)

listafinal = []
for var in x:
	if var != "":
		listafinal.append(var)
print(listafinal)

#2 lista I's
totales = 0
busqueda = ''.join(listafinal)
z=busqueda.split()
w=z.count("I")
listai = ["I"]*w

#3 juntar String
	#se creo el string indicado con nombre busqueda en el punto anterior
print(busqueda)

#4 contar 

total  = z.count("i") + w
porcentaje = w*100/total
print(porcentaje)

		


