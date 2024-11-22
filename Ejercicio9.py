#Imprimir título
print("Programa para calcular la suma de los números pares y el producto del impar:")
#En las variables se utiliza False
Suma_Pares=0
Productos_Impares=1
Existen_Impares=False
N=int(input("Ingrese la cantidad de números a procesar:"))
#Se utiliza range para definir la variable N junto con el bucle For _ in
for _ in range(N):
  Número=int(input("Ingrese un número:"))
#Se utilizan condicionantes con True
if Número%2==0:
  Suma_Pares+=Número
else:
  Productos_Impares*=Número
  Existen_Impares=True
#Imprimir resultado
  print("La suma de los números pares es:" , Suma_Pares)
if Existen_Impares:
  print("El producto de los números impares es:" , Productos_Impares)
else:
  print("No se ingresaron números impares:")
  