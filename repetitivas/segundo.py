"""Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos números. """

numero1 = 0
numero2 = 0
for i in range(10):
    numero = float(input(f"ingrese el numero {i+1} negativo: "))
    numero1 = -1 * numero
    numero2 += numero1
    
print(f"la suma de los numero es de: {numero2}")
            
