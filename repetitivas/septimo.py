"""La oficina de tránsito de Ibagué desea saber, de los n autos que entran a la ciudad de Ibagué,  
cuantos entran con calcomanía de cada color. 
Conociendo el ultimo dígito de la placa de cada carro, 
se puede determinar el color de la calcomanía utilizando la siguiente relación:  """
amarillo = 0
rosa = 0
roja = 0
verde = 0
azul = 0
while True:
    print("===== MENÚ =====")
    print("1. Ingresar")
    print("2. Salir")
    print("================")

    opcion = int(input("Elige una opción (1-2): "))

    if opcion == 1:
        print(">>> Has elegido INGRESAR.\n")
        digitar = int(input("digite la cantidad de autos: "))
        for i in range(digitar):
            placa = int(input(f"digite el ultimo digito de la placa del carro {i+1}: "))
            if placa == 1 or placa == 2:
                amarillo += 1
            elif placa == 3 or placa == 4:
                rosa += 1
            elif placa == 5 or placa == 6:
                roja += 1
            elif placa == 7 or placa == 8:
                verde += 1
            elif placa == 9 or placa == 0:
                azul += 1
        break
    elif opcion == 2:
        print(">>> Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print(">>> Opción no válida. Intenta de nuevo.\n")
        
print("-"*40)
print(f"la cantidad de autos con calcomania amarilla es de: {amarillo}")
print(f"la cantidad de autos con calcomania rosa es de: {rosa}")
print(f"la cantidad de autos con calcomania roja es de: {roja}")
print(f"la cantidad de autos con calcomania verde es de: {verde}")
print(f"la cantidad de autos con calcomania azul es de: {azul}")