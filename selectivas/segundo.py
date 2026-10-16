'''Calcular el total a pagar por la compra de zapatillas. Si se compran tres  
o más zapatillas se aplica un descuento del 20% sobre el total de la compra 
y si son menos de tres zapatillas un descuento del 10%. 
Mostrar en pantalla, el valor de la compra, 
el valor del descuento y el valor a pagar una vez aplicado el descuento. '''
print("Hola Bienvenid@")
print("-"*40)
cantidad = int(input("ingrese la cantidad de zapatillas: "))
precio = int(input("ingrese el precio de las zapatillas: "))
subtotal = cantidad * precio
if cantidad >= 3:
    descuento = subtotal * 0.20
    
elif cantidad < 3:
    descuento = subtotal * 0.10
else:
    print("ingrese los datos correctos")

total = subtotal - descuento
print("-"*40) 
print(f"el valor de su compra es de: {subtotal}")
print(f"el valor del descuento es de: {descuento}")
print(f"el valor a pagar con descuento es de: {total}")