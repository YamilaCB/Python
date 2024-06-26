contador=0
for i in range(1,11):
    numero=int(input("ingrese numero: "))
    if numero%2==0:
        contador=contador+1
print(f"hay {contador} numeros pares")
