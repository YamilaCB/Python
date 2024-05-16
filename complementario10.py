import math
#encabezado
print("-----------------------------------------------------")
print(                "complementario10"                     )
print("-----------------------------------------------------")
#entradas
print ("ingrese valores de los puntos x1,y1,z1")
X1=float(input())
y1=float(input())
z1=float(input())
print ("ingrese valores de los puntos x2,y2,z2")
X2=float(input())
y2=float(input())
z2=float(input())
#proceso
dis=math.sqrt((X2-X1)**2+(y2-y1)**2+(z2-z1)**2)
#salida
print("----------------------------")
print("la distancia entre punto1 y punto2 es: ",dis,"metros")
