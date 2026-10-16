"""Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos. 
Realizar un algoritmo para calcular el promedio  
y la calificación más alta y  más baja de todo el grupo.  """

alta = 0
baja = 999
notas = 0
print("Bienvenid@")
while True:
    print("===== MENÚ =====")
    print("1. Ingresar")
    print("2. Salir")
    print("================")

    opcion = int(input("Elige una opción (1-2): "))

    if opcion == "1":
        print(">>> Has elegido INGRESAR.\n")
        for i in range(20):
             alumnos = float(input(f"ingrese la nota {i+1}: "))
             notas += alumnos
             if alumnos > alta:
                 alta = alumnos
             if alumnos < baja:
                baja = alumnos
        
        final = notas/20
        print("-"*40)
        print(f"el promedio final es de: {final}")
        print(f"la nota mas alta es de: {alta}")
        print(f"la nota mas baja es de: {baja}")
    elif opcion == "2":
        print(">>> Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print(">>> Opción no válida. Intenta de nuevo.\n")