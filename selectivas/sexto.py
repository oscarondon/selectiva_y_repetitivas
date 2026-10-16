'''6.  Se ha establecido un programa para estimular a los alumnos, el cual consiste en lo siguiente: 
si el promedio obtenido por un alumno en el último periodo es mayor o igual que 4.0, 
se le hará un descuento del 30% sobre la pensión;
si el promedio obtenido es menor que 4.0 deberá pagar la pensión completa,
la cual incluye el 10% de IVA. 
Obtener cuanto debe pagar un alumno. '''

print("bienvenid@")
print("-"*40)
promedio = float(input("ingrese su promedio de notas(1.0-5.0)"))
if promedio >= 4.0:
    print("SE TE HA OTORGADO UN DESCUENTO")
    print("tu valor a pagar era de 150.000")
    descuento = 150000-(150000 * 0.30)
    print("con un descuento del 30% por tu rendimiento academico")
    print(f"tu total a pagar es de: {descuento}")
elif promedio < 4.0:
    print("tu valor a pagar de la pension es de 150.000")
    iva = 150000-(150000 * 0.10)
    