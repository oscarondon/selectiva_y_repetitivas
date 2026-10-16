"""modificacion del segundo ejercicio"""
print("Hola Bienvenid@")
print("-"*40)
talla = int(input("ingrese la talla de las zapatillas: "))
precioCompra = int(input("ingrese el precio de compra de las zapatillas: "))

if talla < 17 or talla > 48:
    ganancia = 0
    print("ingrese una talla válida")
elif talla <= 30:
    ganancia = precioCompra * 0.30
elif talla <= 40:
    ganancia = precioCompra * 0.40
else:
    ganancia = precioCompra * 0.50

precio_venta = precioCompra + ganancia
print("-"*40)
print(f"el precio de compra es de: {precioCompra}")
print(f"la ganancia es de: {ganancia}")
print(f"el precio de venta es de: {precio_venta}")