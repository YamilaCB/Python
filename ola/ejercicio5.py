emp=int(input("ingrese cantidad de empleados: "))
sueldoMayor=0
contador=0
for i in range(1,emp+1):
    sueldo=int(input("ingrese los sueldos: "))
    if sueldo>sueldoMayor:
        sueldoMayor=sueldo
        contador=contador+1
print(f"el empleado numero {contador} tiene el mayor sueldo {sueldoMayor}")