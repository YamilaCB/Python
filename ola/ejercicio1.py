numero=int(input("ingrese cuantos numeros quiere ingresar: "))
num=int(input("ingrese un numero: "))
menor=num
mayor=num
for i in range(1,numero):
    num=int(input("ingrese un numero: "))
    if num<menor:
        menor=num
    else:
        if num>mayor:
            mayor=num
print(f"el menor seria: {menor} y el mayor seria: {mayor}")