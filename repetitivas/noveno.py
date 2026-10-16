"""Calcular el promedio de edades de hombres, mujeres y de todo un grupo de alumnos.  """

mujer = 0
edadm = 0
edadh = 0
hombre = 0
promedio = 0
while True:
    print("===== MENÚ =====")
    print("1. Ingresar")
    print("2. Salir")
    print("================")

    opcion = int(input("Elige una opción (1-2): "))

    if opcion == 1:
        print(">>> Has elegido INGRESAR.\n")
        digitar = int(input("digite la cantidad de personas: "))
        for i in range(digitar):
            genero = input(f"digite si es mujer(m) o hombre(h) la persona numero {i+1}: ")
            if genero.lower() == "m":
                mujer += 1
                edad = int(input("digite la edad: "))
                edadm += edad
                promedio += edad
            elif genero.lower() == "h":
                hombre += 1
                edad = int(input("digite la edad: "))
                edadh += edad
                promedio += edad
        break
    elif opcion == 2:
        print(">>> Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print(">>> Opción no válida. Intenta de nuevo.\n")
        
print("-"*40)
print(f"el promedio de edad de las mujeres es de: {round(edadm/mujer,0)}")
print(f"el promedio de edad de los hombres es de: {round(edadh/hombre,0)}")
print(f"el promedio de edad del salon es de: {round(promedio/(hombre+mujer),0)}")