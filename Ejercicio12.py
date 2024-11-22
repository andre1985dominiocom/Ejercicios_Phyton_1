#Imprimir título
print("Programa para restar un número mayor a otro número menor:")
#Solicitar números
num1=int(input("Ingresar el número 1:"))
num2=int(input("Ingresar el número 2:"))
#Utilizar condicionantes
if num1>num2:
  Resultado=num1-num2
  print("La resta del número 1 y número 2 es:" , Resultado )
else:
  print("Operación no es posible: El primer número no es mayor que el segundo:")
