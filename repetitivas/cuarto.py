"""Calcular e imprimir la tabla de multiplicar de un número cualquiera,
el cual se digitará por teclado. 
Imprimir el multiplicando, el multiplicador y el producto. """

numero = int(input("ingrese el numero para multiplicar: "))
for i in range(11):
    tabla = numero * i
    print(f"{numero} X {i} = {tabla} ")