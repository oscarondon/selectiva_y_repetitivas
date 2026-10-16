'''1. Determinar si un aprendiz aprueba o desaprueba Algoritmia,
sabiendo que aprobará si su promedio de tres calificaciones es mayor 
o igual a 70;
reprueba en caso contrario. '''
print("Hola Bienvenid@")
print("-"*40)
nombre = input("ingrese el nombre del aprendiz: ")
calificacion1 = float(input("ingrese la primera nota 1: "))
print("-"*40)
calificacion2 = float(input("ingrese la primera nota 2: "))
print("-"*40)
calificacion3 = float(input("ingrese la primera nota 3: "))
print("-"*40)
promedio = (calificacion1+calificacion2+calificacion3)/3
if promedio <= 69:
    print(f"{nombre} usted desaprueba")
    print(f"ya que su promedio es de: {promedio}")
elif promedio >= 70:
    print(f"{nombre} usted aprueba")
    print(f"ya que su promedio es de: {promedio}")
else:
    print("ingrese los datos correctos")