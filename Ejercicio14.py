#Decoración: Nombre del Algoritmo
print("-------------------------------------------------------")
print("                  Ejercicio14: FUNCIÓN.")
print("-------------------------------------------------------")

#entradas 
print("ingrese valores")
NUM= int(input("tipo de calculo"))
V=int (input("ingrese V:"))

#proceso
#usando diccionario

Funcion = {
1 : 100*V,
2 : 100**V,
3 : 100/V
}

#DICCIONARIO.get(ElementoABuscarEnDiccionario, PorDefecto)
#porDefecto: En caso de que el elemnto no se encuentre.
VAL = Funcion.get(NUM, 0)

#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print(VAL)


