print("------------------------------------------------------")
print("                          costo articulo             ")
print("------------------------------------------------------")
#entradas
print("ingrese el costo del articulo")
costo=float(input())
print("ingrese la marca")
marca=str(input())

#procesos
if (costo>=2000) and (marca == "NOSY"):
    precioAparato = costo*0.90
    precioTotal = precioAparato*0.95
elif (costo >= 2000) and (marca != "NOSY"):
    precioTotal = costo*0.90
elif (costo < 2000) and (marca == "NOSY"):
    precioAparato = costo*0.90
    precioTotal = precioAparato+precioAparato*1.20
elif (costo < 2000) and (marca != "NOSY"):
    precioTotal = costo*1.20

#salida
print("-----------SALIDA-----------------")
print("usted pagara:",precioTotal,"pesos")
