#deco
print("-----------------------------------------------------")
print("                    raices                          ")
print("------------------------------------------------------")
#entradas
print("ingrese valores de la ecuacion cuadratica")
a=float(input())
b=float(input())
c=float(input())
d = b**2-4*a*c

#proceso
if (d > 0):
    x1=((-b)+d**0.5)/2*a
    x2=((-b)-d**0.5)/2*a
    print ("Raices reales:", x1, x2)
else:
    print("Raices irracionales.")
