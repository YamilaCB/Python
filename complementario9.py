import math
#encabezado
print("-----------------------------------------------------")
print(                "complementario9"                      )
print("-----------------------------------------------------")
#entradas
print("ingrese el angulo en radianes")
xrad=float(input())
#proceso
xsex= xrad*180/math.pi
xcen= xrad*200/math.pi
#salida
print("---------------------------")
print("Angulo en grados sexagesimales:",xsex)
print("Angulo en grados centesimales:",xcen)
