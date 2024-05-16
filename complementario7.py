import math 
#encabezado
print("-----------------------------------------------------")
print(                "complementario7"                  )
print("------------------------------------------------------")
#constante
PI=3,1416
#entradas
print("ingrese lado b")
ladoB=int(input())
print("ingrese lado c")
ladoC=int(input())
anguloAlfa= 57
#proceso
ladoA=math.sqrt((ladoB**2+(ladoC)**2)-(2*ladoB*ladoC)*math.cos(anguloAlfa*math.pi/180))
#salida
print ("-------------------------------")
print ("lado A:",ladoA)