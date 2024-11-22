#Imprimir título
print("Programa para calcular los pagos en un restaurante con descuento del 15%:")
Consumo=int(input("Ingrese el total del consumo:"))
#Uso de condicionates 
if Consumo>130000:
    Descuento=Consumo*0.15
    Total_a_Pagar=Consumo-Descuento
    print("Descuento aplicado:" , Descuento)
else:
    Descuento=0
    Total_a_Pagar=Consumo
    print("El total a pagar es:" , Total_a_Pagar)
    print("El total a pagar con decuento es:" , Total_a_Pagar)