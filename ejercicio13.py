#decoracion
print("---------------------------------------------------------------")
print(                 "verificacion año bisiesto")
print("---------------------------------------------------------------")

#entradas
anio=int(input("ingrese año"))

#salida
print("Salida:")
print("-----------------------------------------------------------------")
if(anio % 400==0) or (anio % 4==0) and (anio % 100 !=0):
    print ("el año es BISIESTO")
else:
    print ("el año NO ES BISIESTO")