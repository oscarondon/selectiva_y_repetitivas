'''Una empresa quiere hacer una compra de varias piezas de la misma clase a una fábrica de bolsos. 
La empresa, dependiendo del monto total de la compra, 
decidirá qué hacer para pagar al fabricante:
 Si el monto total de la compra excede de $500 000 la empresa 
tendrá la capacidad de invertir de su propio dinero un 55% del monto de la compra,
pedir prestado al banco un 30% 
y el resto lo pagará solicitando un crédito al fabricante. 
 Si el monto total de la compra no excede de $500 000 la empresa tendrá
capacidad de invertir de su propio dinero un 70% y el restante 30% 
lo pagará solicitando crédito al fabricante. 
El fabricante cobra por concepto de intereses un 20% sobre la cantidad que se le pague a crédito.
Imprimir el valor invertido de su propio dinero, 
el valor prestado al banco, 
y el valor del crédito solicitado al fabricante, según sea el caso'''

print("bienvenid@s")
print("-"*40)
cantidad = float(input("ingrese el monto total de la compra: "))
if cantidad > 500000:
    dinerop = cantidad * 0.55
    banco = cantidad * 0.30
    totalFabricante = cantidad*0.15
    print(f"el valor invertido propio es de: {dinerop}")
    print(f"el valor prestado al banco es de: {banco}")
    print(f"el valor de credito solicitado al fabricante es de: {totalFabricante}")
elif cantidad <= 500000:
    dinerop = cantidad * 0.70
    fabricante = cantidad *0.30
    interesFabricante = fabricante*0.20
    totalFabricante = fabricante + interesFabricante
    print(f"el valor invertido propio es de: {dinerop}")
    print(f"el valor de credito solicitado al fabricante es de: {totalFabricante}")

else:
    print("ingrese datos correctos")
    
