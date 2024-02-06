import random
import matplotlib.pyplot as plt


valores = [47, 43, 21, 20, 20]
num_muestras = 25
media = 0
x = [20, 21, 31, 32, 33, 34, 43, 47]
f = [9, 1, 3, 4, 3, 1, 3, 1]
mediana = 0.0
V_muestras = 0.0

print(" Muestra     Media       Mediana       S^2 ")
for i in range(1, num_muestras+1):
    muestra1 = random.choice(valores)
    muestra2 = random.choice(valores)

    media = (muestra1 + muestra2) / 2
    V_muestras = (muestra1 - media) ** 2 + (muestra2 - media) ** 2

    print(f"{i}:({muestra1},{muestra2})     {media}         {media}          {V_muestras}")

print()
print(" X      Frecuencia         P(x/n)")
for j in range(8):
    print(f"{x[j]}           {f[j]}                {f[j]}/25")

print()
for i in range(8):
    resultado = (x[i] * f[i]) / 25.0
    mediana += resultado
    print(f"{x[i]}*{f[i]}/25", end="")
    if i < 7:
        print(" + ", end="")
print(f"\n Mediana: {mediana}")

print()
valores2 = [47, 43, 21, 20, 20]
mediana2 = 29.24
varianza = 0
for i in range(5):
    resultado2 = (valores2[i] - mediana2) ** 2
    varianza += resultado2
    print(f"({valores2[i]} - {mediana2})^2 +", end="")
print("/25")

var2 = varianza / 25
print(f"\n Varianza: {var2}")

D_Medias = var2 / 5
print("\nLa distribucion de medias es:", D_Medias)

# Datos para graficar
x = [20, 21, 31, 32, 33, 34, 43, 47]
f = [9, 1, 3, 4, 3, 1, 3, 1]

# Graficar los datos de frecuencia
plt.bar(x, f)
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('Datos de Frecuencia')
plt.show()