"""Una persona debe realizar un muestreo con 50 personas para determinar el promedio de peso de los niños,
jóvenes, adultos y ancianos  que existen en su zona. 
Las categorías se determinar de acuerdo a la siguiente tabla:  """
cantidadn = 0
ninos = 0
cantidadj = 0
jovenes = 0
cantidada = 0
adultos = 0
cantidadan = 0
ancianos = 0
while True:
    print("===== MENÚ =====")
    print("1. Ingresar")
    print("2. Salir")
    print("================")

    opcion = int(input("Elige una opción (1-2): "))

    if opcion == 1:
        print(">>> Has elegido INGRESAR.\n")
        for i in range(50):
            print("eliga la categoria")
            print("1)niños")
            print("2)jovenes")
            print("3)adultos")
            print("4)ancianos")
            elegir = int(input("digite su opcion: "))
            if elegir == 1:
                cantidadn += 1
                peso = float(input("digite el peso del menor: "))
                print("-"*40)
                ninos += peso
            elif elegir == 2:
                cantidadj +=1
                peso = float(input("digite el peso del joven: "))
                print("-"*40)
                jovenes += peso
            elif elegir == 3:
                cantidada += 1
                peso = float(input("digite el peso del adulto: "))
                print("-"*40)
                adultos += peso
            elif elegir == 4:
                cantidadan +=1
                peso = float(input("digite el peso del anciano: "))
                print("-"*40)
                ancianos += peso
            else:
                print("digite una opcion correcta")
        break
    elif opcion == 2:
        print(">>> Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print(">>> Opción no válida. Intenta de nuevo.\n")

print(f"el promedio de peso de los niños es de: {round(ninos/cantidadn,2)}")
print(f"el promedio de peso de los jovenes es de: {round(jovenes/cantidadj,2)}")
print(f"el promedio de peso de los adultos es de: {round(adultos/cantidada,2)}")
print(f"el promedio de peso de los ancianos es de: {round(ancianos/cantidadan,2)}")