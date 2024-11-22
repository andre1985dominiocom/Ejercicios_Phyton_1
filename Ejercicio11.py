#Imprimir título
print("Programa para calcular la nota promedio de los estudiantes:")
#Ingresar estudiantes
Estudiantes=5
print("Ingrese los datos de 5 estudiantes del curso de computación:")
#Se utiliza el range y el bucle for i in para solicitar los datos de los estudiantes
for i in range(1, 6):
    print("Número de estudiantes:")
#Solicitar nombre
Nombre=input("Nombre:")
if not Nombre:
    print("Error el nombre no puede estar vacio. Intente de nuevo:")
#Solicitar apellido
Apellido=input("Apellido:")
if not Apellido:
    print("Error el apellido no puede estar vacio intente de nuevo:")
#Solicitar edad
Edad=input("Edad:")
if not Edad:
    print("Error la edad debe ser un número entero intentelo de nuevo:")
else:
    Edad=int("Edad:")
if Edad<0 or Edad>60:
    print("Error la edad debe estar entre 0 y 60 intentelo de nuevo:")
else:
    Nota_Promedio=float("Nota promedio:")
    if Nota_Promedio<0.0 or Nota_Promedio>10.0:
        print("Error la nota promedio debe estar entre 0.0 y 10.0 intente de nuevo")
#Solicitar los datos de los estudiantes
Nombre="Nombre:"
Apellido="Apellido:"
Edad="Edad:"
Nota_Promedio="Nota Promedio:"
#Imprimir los datos
if Estudiantes:
    print("Datos de los estudiantes:")
    for i, Estudiantes in enumerate(Estudiantes, start=1):
        print("Estudiantes:")
        print("Nombre:" , Nombre)
        print("Apellido:" , Apellido)
        print("Edad:" , Edad)
        print("Nota Promedio:" , Nota_Promedio)
else:
    print("No se ingresaron datos válidos:")
