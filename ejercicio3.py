#decoracion
print("_______________________________")
print(  "Ejercicio3: Puntaje final")
print("_______________________________")
#entradas
print("Ingrese numero de respuestas correctas:")
RC= int(input())
print("Ingrese numero de respuestas incorrectas:")
RI=int(input())
print("Ingrese numero de respuestas en blanco:")
RB= int(input())
#Proceso
PCR=RC*3
PRI=RI*-1
PRB=RB*0
PF= PCR+PRI+PRB
#SALIDA
print("El puntaje total es:", PF)