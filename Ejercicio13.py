#Imprimir título
print("Programa para calcular descuento a diferentes tipos de clientes:")
Tipo_A=float(input("Ingresar el valor del helado A:"))
Tipo_B=float(input("Ingresar el valor del helado B:"))
Tipo_C=float(input("Ingresar el valor del helado C:"))
Descuento=Tipo_A*0.10
print ("Mostrar resultado" , Descuento)
Descuento=Tipo_B*0.15
print("Mostrar resultado" , Descuento)
Descuento=Tipo_C*0.20
print("Mostrar resultado" , Descuento)
if Tipo_A>Tipo_B and Tipo_A>Tipo_C:
  print("Mostrar el resultado:" , Descuento)
elif Tipo_B>Tipo_A and Tipo_B>Tipo_C:
  print("Mostrar el resultado:" , Descuento)
#else:
  #print("Mostrar resultado descuento" , Descuento)
