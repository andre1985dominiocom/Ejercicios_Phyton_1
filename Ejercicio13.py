#Imprimir título
print("Programa para calcular descuento a diferentes tipos de clientes:")
#Solicitar el valor del helado
Precio=int(input("Ingresar el precio de la compra:"))
#Se ingresa el tipo de membresía
print("Tipos de membresía:")
print("A: 10% descuento:")
print("B: 15% descuento:")
print("C: 20% descuento:")
Tipo_Membresia=input("Ingresar el tipo de membresía (A, B, C):")
#Calcular el descuento según tipo de membresía
if Tipo_Membresia=="A":
  Descuento=Precio*0.10
elif Tipo_Membresia=="B":
  Descuento=Precio*0.15
elif Tipo_Membresia=="C":
  Descuento=Precio*0.20
else:
  Descuento=0
  print("Error tipo de membresía no valida no se aplica descuento:")
#Calcular el precio después del descuento
Total=Precio-Descuento
#Imprmir resultados
print("Resumen de la compra:")
print("Precio inicial:" , Precio)
print("Descuento:" , Descuento)
print("Total a pagar:" , Total)

