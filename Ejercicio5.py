#Imprimir título
print("Algoritmo para calcular el área de un rectángulo con los lados positivos:")
#Ingresar datos
lado1=float(input("Ingresar lado 1:"))
lado2=float(input("Ingresar lado 2:"))
#Uso de condicionantes
if lado1>0 and lado2>0:
  área=lado1*lado2
  print("El área del rectángulo es:" , área)
else:
  print("Error: ambos lados deben ser números positivos")