'''5. Calcular el número de pulsaciones que debe tener una persona 
por cada 10 segundos de ejercicio aeróbico; la fórmula que se aplica es: 
 cuando el sexo es femenino : núm. pulsaciones = (220 - edad)/10 
 y si el sexo es masculino : núm. pulsaciones = (210 - edad)/10 '''

print("bienvenid@")
print("-"*40)
nombre = input("ingresa tu nombre: ")
genero = input("ingresa tu genero(f/m): ")
edad = int(input("ingresa tu edad: "))
if genero.lower() == "femenino" or genero.lower() == "f":
    print("-"*40)
    pulsaciones = (220 -edad)/10
    print(f"{nombre} tu numero de pulsaciones por cada 10 segundos es de: {pulsaciones}")
elif genero.lower() == "masculino" or genero.lower() == "m":
    print("-"*40)
    pulsaciones = (210-edad)/10
    print(f"{nombre} tu numero de pulsaciones por cada 10 segundo es de: {pulsaciones}")
else:
    print("opcion incorrecta")