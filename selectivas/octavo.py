'''8. Tomando como base los resultados obtenidos en un laboratorio de análisis clínicos, 
un médico determina si una persona tiene anemia o no,
lo cual depende de su nivel de hemoglobina en la sangre, de su edad y de su sexo. 
Si el nivel de hemoglobina que tiene una persona es menor que el rango que le corresponde,
se determina su resultado como positivo y en caso contrario como negativo. 
La tabla en la que el médico se basa para obtener el resultado es la siguiente: 
EDAD NIVEL HEMOGLOBINA 
0 - 1 mes             13 - 26 g% 
> 1 y < = 6 meses       10 - 18 g% 
> 6 y < = 12 meses     11 - 15 g% 
> 1 y < = 5 años       11.5 - 15 g% 
> 5 y < = 10 años     12.6 - 15.5 g% 
> 10 y < = 15 años    13 - 15.5 g% 
mujeres > 15 años    12 - 16 g% 
hombres > 15 años   14 - 18 g% '''

print("bienvenid@")
print("-"*40)
sexo = input("Sexo (M/F): ").upper()
edad = float(input("Edad: "))
unidad = input("La edad está en años o meses? (a/m): ").lower()
hemoglobina = float(input("Nivel de hemoglobina (g%): "))

if unidad == "m":
    edad_meses = edad
    edad_anios = edad / 12
else:
    edad_anios = edad
    edad_meses = edad * 12

if edad_meses <= 1:
    minimo = 13
elif edad_meses <= 6:
    minimo = 10
elif edad_meses <= 12:
    minimo = 11
elif edad_anios <= 5:
    minimo = 11.5
elif edad_anios <= 10:
    minimo = 12.6
elif edad_anios <= 15:
    minimo = 13
elif sexo == "F":
    minimo = 12
else:
    minimo = 14

if hemoglobina < minimo:
    print("Resultado: POSITIVO (tiene anemia)")
else:
    print("Resultado: NEGATIVO (no tiene anemia)")