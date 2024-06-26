numero=int(input("ingrese la cantidad de numero que quiere ingresar: "))
contador=0
for i in range(1,numero+1):
    num=int(input("ingrese numero: "))
    if num==0:
        contador=contador+1

print(f"hay {contador} ceros")