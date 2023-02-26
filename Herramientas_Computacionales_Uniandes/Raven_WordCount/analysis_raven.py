# 1. Crear lista con los parrafos del texto
archivo = open("the_raven_poe.txt", encoding="utf-8")
lineas = archivo.readlines()
texto = ''.join(lineas)
x = texto.split("\n")
x.pop(0)
x.pop(2)
x.pop(3)

listafinal = []
for var in x:
    if var != "":
        listafinal.append(var)

#2 numero I's
totales = 0
busqueda = ''.join(listafinal)
w = busqueda.count("I")

print(f'El texto tiene {w} I\'s')

#4 Comparar con i's

total = busqueda.count("i") + w
porcentaje = w * 100 / total
print(
    f'El texto tiene {total} i\'s y {w} I\'s, el porcentaje de I\'s es {porcentaje}%'
)