
def funcion3  (a):
	verificador = True
	for elemento in range ( len(lista) + 1) :
		if elemento+1 < len(lista) and lista[elemento] > lista[elemento+1] :
			verificador = False
			break
	if verificador == True:
		return ("all right")
	else:
		return ("not right")

