#Imprimir título
print("Programa para calcular el subtotal, IVA y total:")
#Variables
Subtotal=0
IVA=0.19
#Imprimir el valor de los 5 productos
print("Calcular compra para 5 productos:")
#Se utiliza range junto con el bucle for i in para calcular el precio de los 5 productos
for i in range(1 , 6):
    Precio=int(input("Ingrese el precio del producto:"))
    Subtotal+=Precio
#Calcular el IVA, subtotal y total
IVA=Subtotal*IVA
Total=Subtotal+IVA
#Imprimir resultados
print("Resultados de la compra:")
print("Mostrar Subtotal:" , Subtotal)
print("Mostrar IVA:" , IVA)
print("Mostrar total a pagar:" , Total)
