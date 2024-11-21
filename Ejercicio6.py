#Imprimir título
print("Programa para calcular la temperatura y la presión:")
#Ingresar datos
Temperatura=int(input("Ingresar el valor de la temperatura:"))
Presión=int(input("Ingresar el valor de la presión:"))
if Presión>200 and Temperatura>100:
  print("Alarma")
else:
  print("Normal")