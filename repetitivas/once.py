"""Pedir los datos de los alumnos, estos son: sexo, edad y altura. 
Al final del programa se deberá mostrar la cantidad de hombres, la cantidad de mujeres, 
la altura promedio ,la cantidad de alumnos que tienen una altura mayor a 1.70 cm, 
la cantidad de alumnos que tiene una altura  menor o igual a 1.50 cm. 
El programa debe finalizar cuando la edad sea igual a 0. """


hombres = 0
mujeres = 0
sumaalturas = 0
cantidadalumnos = 0
mayores170 = 0
menores150 = 0

while True:
    edad = int(input("Ingrese la edad del alumno (0 para finalizar): "))

    if edad == 0:
        break

    sexo = input("Ingrese el sexo (h/m): ").lower()
    altura = float(input("Ingrese la altura en metros: "))

    cantidadalumnos += 1
    sumaalturas += altura

    if sexo == "h":
        hombres += 1
    elif sexo == "m":
        mujeres += 1

    if altura > 1.70:
        mayores170 += 1

    if altura <= 1.50:
        menores150 += 1

print("-"*40)
print("Cantidad de hombres:", hombres)
print("Cantidad de mujeres:", mujeres)

if cantidadalumnos > 0:
    promedio = sumaalturas / cantidadalumnos
    print("Altura promedio:", round(promedio, 2), "metros")
else:
    print("No se ingresaron alumnos.")

print("Alumnos con altura mayor a 1.70 m:", mayores170)
print("Alumnos con altura menor o igual a 1.50 m:", menores150)
