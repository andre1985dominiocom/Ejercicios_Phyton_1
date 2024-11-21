#Imprimir título
print("Programa para calcular las áreas de un triángulo y círculo:")
import math
print("Cálculo de áreas:")
print("T: Triángulo:")
print("C: Círculo:")
#Que opción puede aparecer para el usuario
Opcion=input("¿Qué figura quiere calcular? T o C:")
#uso de los condicionales
if Opcion=="T":
    Base=float(input("Ingrese la base del triángulo:"))
    Altura=float(input("Ingrese la altura del triángulo:"))
    Área=(Base*Altura)/2
    print("El área del triágulo es:" , Área)
elif Opcion=="C":
    Radio=float(input("Ingrese el radio del círculo:"))
    Área=math.pi*(Radio**2)
    print("El área del círculo es:" , Área)
else:
    print("Opción no válida. Por favor, elija T o C:")