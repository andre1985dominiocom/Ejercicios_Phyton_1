#Imprimir título
print("Programa para calcular el subtotal, IVA y total:")
Producto_1=int(input("Ingresar el valor del producto 1:"))
Producto_2=int(input("Ingresar el valor del producto 2:"))
Producto_3=int(input("Ingresar el valor del producto 3:"))
Producto_4=int(input("Ingresar el valor del producto 4:"))
Producto_5=int(input("Ingresar el valor del producto 5:"))
print("Calcular el valor de los productos:")
IVA=int(input("Ingresar el valor del IVA:"))
Subtotal=Producto_1+Producto_2+Producto_3+Producto_4+Producto_5
print("Mostrar el subtotal:" , Subtotal)
IVA=(Producto_1+Producto_2+Producto_3+Producto_4+Producto_5)*0.19
print("Mostrar el IVA:" , IVA)
Total=(Subtotal+IVA)
print("Mostrar el total:" , Total)