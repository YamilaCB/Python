#Decoración: Nombre del Algoritmo
print("-------------------------------------------------------")
print("Vector1: LECTURA DE N ELEMENTOS ENTEROS.")
print("-------------------------------------------------------")
#inicializar
i=1
F=[]
#entrada
print("ingrese numero de elementos a ingresar:")
numElementos=int (input())
#proceso
while i<=numElementos:
    elemento=int(input("ingrese Elemento:"))
    F.append(elemento)
i=i+1
#salida
print("-------------")
print(F)