import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parámetros iniciales
mu_inicial = 100.0      # IQ promedio inicial
sigma = 15.0            # Desviación estándar
heritability = 0.6      # Heredabilidad del IQ
generations = 10     # Número de generaciones (años) a simular

# Definimos una grilla de IQ para realizar la integración numérica
iq_grid = np.linspace(0, 500, 10000)
delta = iq_grid[1] - iq_grid[0]

def weight(iq):
    """
    Función de peso que asigna el factor reproductivo según el IQ:
      - IQ de 0 a iq_min_op: factor 0.5
      - IQ de iq_min_op a iq_max_op: factor 1.1
      - IQ de iq_max_op en adelante: factor 1.5
    """
    w = np.ones_like(iq)
    k=mu_actual/mu_inicial
        
    w[(iq >= 100*k) & (iq < 105.26315789473685*k)] = 1.1  
    w[iq >= 105.26315789473685*k] = 1.5                  
    w[iq < 100*k] = 0.5                    
    return w

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
    
    
    




plt.figure(figsize=(8,5))
plt.plot(range(generations), mu_list, marker='o', linestyle='-', color='b')
# plt.xscale('log')
plt.xlabel("Generación (años)")
plt.ylabel("IQ promedio")
plt.title("Evolución del IQ promedio por generación")
plt.grid(True)
plt.show()
print(mu_actual)