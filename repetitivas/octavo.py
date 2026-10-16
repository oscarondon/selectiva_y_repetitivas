"""un grupo de 23 estudiantes presentan un examen de algoritmia.
Hacer un algoritmo que lea por cada estudiante la calificación obtenida. 
Al finalizar calcule e imprima: 
• La cantidad de estudiantes que obtuvieron una calificación menor a 50. 
• La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero menor que 70.
• La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero menor que 80.  
• La cantidad de estudiantes que obtuvieron una calificación de 80 o más. 
La calificación obtenida en el examen de algoritmia debe ser entre 1 y 100. """

menor50 = 0
mayori50menor70 = 0
mayori70menor80 = 0
calificacional = 0
while True:
    print("===== MENÚ =====")
    print("1. Ingresar")
    print("2. Salir")
    print("================")

    opcion = int(input("Elige una opción (1-2): "))

    if opcion == 1:
        print(">>> Has elegido INGRESAR.\n")
        for i in range(5):
            nota = int(input(f"digite la nota del estudiante {i+1}: "))
            if nota >= 1 and nota <= 49:
                menor50 += 1
            elif nota >= 50 and nota <= 69:
                mayori50menor70 += 1
            elif nota >= 70 and nota <= 79:
                mayori70menor80 += 1
            elif nota >= 80 and nota <= 100:
                calificacional += 1
            else:
                print("digite una nota valida")
        break
    elif opcion == 2:
        print(">>> Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print(">>> Opción no válida. Intenta de nuevo.\n")
        
print("-"*40)
print(f"la cantidad de alumnos con notas menor a 50 es de: {menor50}")
print(f"la cantidad de alumnos con notas mayor o igual que 50 pero menor a 70 es de: {mayori50menor70}")
print(f"la cantidad de alumnos con notas mayor o igual que 70 pero menor a 80 es de: {mayori70menor80}")
print(f"la cantidad de alumnos que notas mayor o igual que 80: {calificacional}")