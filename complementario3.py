#Deco:cambio dolar-euro
print("-----------------------------------------------------")
print("complementario3:Cambio de pesos a euros y dolares ")
print("------------------------------------------------------")
#constantes
EURO = 934.0
DOLAR = 873.0
#entradas
print ("ingrese monto en pesos:")
pesos=float ( input())
#proceso
dolares=pesos/DOLAR
euros=pesos/EURO
#Salida
print("---------------------------")
print("En",pesos, "pesos hay", euros,"euros")
print("En",pesos,"pesos hay",dolares,"dolares")