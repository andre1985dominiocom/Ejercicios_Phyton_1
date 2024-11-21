#Imprimir título
print("Programa para calcular tres valores diferentes que indique si es mayor, menor o igual:")
#Ingresar datos
A=int(input("Ingrese el primer número (A):"))
B=int(input("Ingrese el segundo número (B):"))
C=int(input("Ingrese el tercer número (C):"))
#Cacular datos
if A==B==C:
  print("Los tres números son iguales")
#Determinar el mayor
if A>B and A>C:
    Mayor=A
elif B>A and B>C:
  Mayor=B
else:
  Mayor=C
#Determinar el menor
if A<B and A<C:
  Menor=A
elif B<A and B<C:
  Menor=B
else:
  Menor=C
#Imprimir Datos
print("El número mayor es:" , Mayor)
print("El número menor es:" , Menor)