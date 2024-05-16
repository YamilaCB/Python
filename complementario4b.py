#deco
print("-----------------------------------------------------")
print("                          fecha                      ")
print("------------------------------------------------------")

#entrada
print("ingrese fecha")
print("año")
año = int(input())
print("mes (numerico)")
mes = int(input())
print("dia")
dia = int(input())

#procesoysalida
if dia > 0 and dia < 30:
    print ( "mañana es ",dia+1,"/",mes,"/",año)
elif mes>0 and mes<12:
    print ("mañana es 1 /", mes+1 ,"/",año)
else :
    print ("mañana es 1 / 1 /",año+1)
