#Imprimir título
print("Programa para calcular los pagos en un restaurante con descuento del 15%")
Consumo=int(input("El total consumo con descuento es:"))
if Consumo>130000:
    Descuento=Consumo*0.15
    Total_a_Pagar=Consumo-Descuento
    print("Descuento aplicado:" , Descuento)
else:
    Descuento=0
    Total_a_Pagar=Consumo
    print("El total a pagar es:" , Total_a_Pagar)