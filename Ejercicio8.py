#Imprimir título
print("Programa para calcular las horas de trabajo:")
#Enumerar el tipo de empleado
print("Tipos de empleado:")
print("1 Planta:")
print("2 Administrativo:")
Tipo_Empleado=int(input("Ingrese el tipo de empleado:"))
#Verificar si el tipo de empleado es válido
if Tipo_Empleado not in (1 , 2):
  print("Error tipo de empleado no válido")
else:
#Solicitar las horas trabajadas
 Horas_Trabajadas=int(input("Ingrese el total de horas trabajadas:"))
#Calcular el pago por hora según el tipo de empleado
if Tipo_Empleado==1:
  Pago_por_Hora=20000
elif Tipo_Empleado==2:
  Pago_por_Hora=10000
#Calcular pago total
Pago_Total=Horas_Trabajadas*Pago_por_Hora
#Imprimir resultado
print("El pago total del empleado es:" , Pago_Total)