""" Calcular la cantidad de hombres y mujeres presentes en un salón de clases con un total de n personas."""
mujer = 0
hombre = 0
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
            elif genero.lower() == "h":
                hombre += 1
        break
    elif opcion == 2:
        print(">>> Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print(">>> Opción no válida. Intenta de nuevo.\n")
        
print(f"la cantidad de mujeres entre {digitar} personas es de: {mujer}")
print(f"la cantidad de hombres entre {digitar} personas es de: {hombre}")