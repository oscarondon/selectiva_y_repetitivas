"""Leer 20 números e imprimir cuantos son  positivos, cuantos negativos y cuantos neutros. """
positivo = 0
negativo = 0 
neutro = 0
for i in range(20):
    numero = float(input(f"ingrese el numero {i+1}: "))
    if numero >= 1:
        positivo += 1
    elif numero <= -1:
        negativo += 1
    elif numero == 0:
        neutro += 1
    else:
        print("ingrese un dato correcto")
        
print(f"numero positivos: {positivo}")
print(f"numeros negativos: {negativo}")
print(f"numeros neutros: {neutro}")