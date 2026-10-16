'''7. En una llantera se ha establecido una promoción de las llantas marca “Todo Terreno”,
dicha promoción consiste en lo siguiente:
Si se compran menos de cinco llantas el precio es de $300.000 cada una, 
de $250.000 si se compran de cinco a 10 y de $200.000 si se compran más de 10. 
Obtener la cantidad de dinero que una persona 
tiene que pagar por cada una de las llantas que compre. '''

print("bienvenid@")
print("-"*40)
cantidad = int(input("ingrese la cantidad de llantas que va llevar: "))
if cantidad < 5:
    precio = cantidad * 300000
    print(f"la cantidad a pagar por las {cantidad} llantas es de: {precio}")
elif cantidad >=5 and cantidad <=10:
    precio = cantidad * 250000
    print(f"la cantidad a pagar por las {cantidad} llantas es de: {precio}")
elif cantidad >=11:
    precio = cantidad * 200000
    print(f"la cantidad a pagar por las {cantidad} llantas es de: {precio}")
else:
    print("digite un valor correcto")