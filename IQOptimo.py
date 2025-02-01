import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parámetros iniciales
mu_inicial = 100.0      # IQ promedio inicial
sigma = 15.0            # Desviación estándar
heritability = 0.6      # Heredabilidad del IQ
generations = 1         # Solo una generación para maximizar el cambio

# Definimos una grilla de IQ para realizar la integración numérica
iq_grid = np.linspace(0, 500, 10000)
delta = iq_grid[1] - iq_grid[0]

def weight(iq, mu_actual, iq_min, iq_max):
    """
    Función de peso con valores dinámicos de iq_min e iq_max.
    """
    w = np.ones_like(iq)
    k = mu_actual / mu_inicial  # Se calcula k dentro de la función
    
    w[(iq >= iq_min*k) & (iq <= iq_max*k)] = 1  
    w[iq > iq_max*k] = 1.5                  
    w[iq < iq_min*k] = 0.5                    
    return w

def evaluar_configuracion(iq_min, iq_max):
    """ Calcula el IQ promedio después de una generación con valores dados de iq_min e iq_max """
    mu_actual = mu_inicial
    phi = norm.pdf(iq_grid, mu_actual, sigma)
    w_iq = weight(iq_grid, mu_actual, iq_min, iq_max)

    numerador = np.sum(iq_grid * phi * w_iq) * delta
    denominador = np.sum(phi * w_iq) * delta
    mu_sel = numerador / denominador  # IQ promedio de los padres ponderado

    S = mu_sel - mu_actual
    return mu_actual + heritability * S  # IQ promedio en la siguiente generación

# Rango de valores para probar
iq_min_values = np.linspace(50, 100, 20)   # Rango de IQ mínimo
iq_max_values = np.linspace(100, 150, 20)  # Rango de IQ máximo

best_iq_min = None
best_iq_max = None
best_mu = -np.inf

# Buscar la mejor combinación de iq_min y iq_max
for iq_min in iq_min_values:
    for iq_max in iq_max_values:
        mu_next = evaluar_configuracion(iq_min, iq_max)
        if mu_next > best_mu:
            best_mu = mu_next
            best_iq_min = iq_min
            best_iq_max = iq_max

print(f"Valores óptimos encontrados:")
print(f" - IQ mínimo óptimo: {best_iq_min}")
print(f" - IQ máximo óptimo: {best_iq_max}")
print(f" - IQ promedio en la siguiente generación: {best_mu:.2f}")
