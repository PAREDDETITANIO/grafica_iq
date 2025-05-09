import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parámetros iniciales
mu_inicial = 100.0      # IQ promedio inicial
sigma = 15.0            # Desviación estándar
heritability = 0.5      # Heredabilidad del IQ
generations = 100        # Número de generaciones (años) a simular

# Definimos una grilla de IQ para realizar la integración numérica
iq_grid = np.linspace(0, 200, 10000)
delta = iq_grid[1] - iq_grid[0]

def weight(iq):
    """
    Función de peso que asigna el factor reproductivo según el IQ:
      - IQ de 0 a 70: factor 1.0
      - IQ de 71 a 129: factor 1.1
      - IQ de 130 en adelante: factor 1.2
    """
    w = np.ones_like(iq)
    w[(iq >= 71) & (iq <= 129)] = 1.2
    w[iq >= 130] = 1.5
    w[iq < 70] = 0.5
    
    return w

# Lista para almacenar el IQ promedio de cada generación
mu_list = []
mu_actual = mu_inicial

# Simulación generación por generación
for gen in range(generations):
    mu_list.append(mu_actual)
    
    # Calcular la función de densidad normal con el IQ promedio actual
    phi = norm.pdf(iq_grid, mu_actual, sigma)
    w_iq = weight(iq_grid)
    
    # Cálculo de la integral ponderada (numerador y denominador)
    numerador = np.sum(iq_grid * phi * w_iq) * delta
    denominador = np.sum(phi * w_iq) * delta
    mu_sel = numerador / denominador  # IQ promedio de los padres ponderado
    
    # Diferencial de selección S
    S = mu_sel - mu_actual
    
    # Actualización del IQ promedio usando la ecuación del criador
    mu_actual = mu_actual + heritability * S

# Graficar la evolución del IQ promedio por generación
plt.figure(figsize=(8,5))
plt.plot(range(generations), mu_list, marker='o', linestyle='-', color='b')
plt.xlabel("Generación (años)")
plt.ylabel("IQ promedio")
plt.title("Evolución del IQ promedio por generación")
plt.grid(True)
plt.show()