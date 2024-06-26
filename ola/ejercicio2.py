letras=input("ingrese 5 caracteres: ")
caracteres=0
for i in range(1,5):
    letras=input("ingrese caracteres: ")
    if letras=="a":
        caracteres=caracteres+1
print(f"hay {caracteres} caracter a")