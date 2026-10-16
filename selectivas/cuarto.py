'''4. En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento
dependiendo de un color  que se escoge al azar. 
Si el color de la balota es rojo  el descuento es del 15% sobre el total de la compra, 
la balota es verde el descuento es del 20%.
Si  el color es diferente a los indicados no obtendrá descuento.
Imprimir el valor de la compra, el color de la balota,
el descuento y el valor a pagar. '''

import random

print("Bienvenid@")
print("-"*40)
colores = ["rojo","verde","amarillo","azul"]
girar = input("dale a enter para girar y saber cual es tu color de la suerte: ")
elegir = random.choice(colores)
if elegir == "rojo":
    print("-"*40)
    print("HAS SACADO LA BOLETA ROJA")
    print("tendras un descuento del 15%")
    valor= float(input("ingrese el total de su compra: "))
    descuento = valor*0.15
    total = valor-descuento
    print(f"el valor de la compra es de: {valor}")
    print(f"el color de la balota es: {elegir}")
    print(f"el descuento es de: {descuento}")
    print(f"el total a pagar es de: {total}")
elif elegir == "verde":
    print("-"*40)
    print("HAS SACADO LA BOLETA VERDE!!!")
    print("tendras un descuento del 20%")
    valor= float(input("ingrese el total de su compra: "))
    descuento = valor*0.20
    total = valor-descuento
    print(f"el valor de la compra es de: {valor}")
    print(f"el color de la balota es: {elegir}")
    print(f"el descuento es de: {descuento}")
    print(f"el total a pagar es de: {total}")
elif elegir != "verde" or elegir != "rojo":
    print("-"*40)
    print(f"Has sacado la boleta de color: {elegir}")
    print("no tendras descuento")
    valor= float(input("ingrese el total de su compra: "))
    print(f"el valor a pagar es de: {valor}")
    print(f"el color de la balota es: {elegir}")
else:
    print("color no existente")