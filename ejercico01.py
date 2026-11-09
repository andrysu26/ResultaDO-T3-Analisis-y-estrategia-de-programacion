import random
import math

print("--- CALCULO DE INTERSECCION ELIPSE E HIPERBOLA POR MONTECARLO ---")

# 1. Pedir los datos al usuario
a = float(input("Ingresa el valor de a (para la elipse): "))
b = float(input("Ingresa el valor de b (para la elipse): "))
c = float(input("Ingresa el valor de c (para la hiperbola): "))
d = float(input("Ingresa el valor de d (para la hiperbola): "))
cantidad = int(input("Ingresa la cantidad de puntos aleatorios a generar: "))

puntos_en_elipse = 0
puntos_en_interseccion = 0

# 2. Generar los puntos aleatorios y evaluar
for i in range(cantidad):
    # Generamos x entre -a y a, y y entre -b y b
    x = random.uniform(-a, a)
    y = random.uniform(-b, b)
    
    # Formula de la elipse: (x^2 / a^2) + (y^2 / b^2) <= 1
    es_elipse = (x**2 / a**2) + (y**2 / b**2) <= 1
    
    if es_elipse:
        puntos_en_elipse += 1
        
        # Formula de la hiperbola: (x^2 / c^2) - (y^2 / d^2) >= 1
        es_hiperbola = (x**2 / c**2) - (y**2 / d**2) >= 1
        
        # Si esta en la elipse y ademas cumple la condicion de la hiperbola, es la interseccion
        if es_hiperbola:
            puntos_en_interseccion += 1

# 3. Calcular el area real de la elipse por formula matematica
area_real_elipse = math.pi * a * b

# 4. Calcular el area aproximada de la interseccion por proporciones
if puntos_en_elipse > 0:
    area_aproximada_interseccion = (puntos_en_interseccion / puntos_en_elipse) * area_real_elipse
else:
    area_aproximada_interseccion = 0

# 5. Mostrar los resultados en pantalla
print("\n---------------- RESULTADOS ----------------")
print(f"Puntos aleatorios que cayeron dentro de la elipse: {puntos_en_elipse}")
print(f"Puntos aleatorios que cayeron en la interseccion: {puntos_en_interseccion}")
print(f"Area real de la elipse: {area_real_elipse:.4f}")
print(f"Area aproximada de la zona de interseccion: {area_aproximada_interseccion:.4f}")