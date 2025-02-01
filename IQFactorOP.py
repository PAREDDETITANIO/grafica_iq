import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from itertools import product  # Para probar combinaciones

# Parámetros iniciales
mu_inicial = 100.0      # IQ promedio inicial
sigma = 15.0            # Desviación estándar
heritability = 0.6      # Heredabilidad del IQ
generations = 1         # Solo una generación para optimizar parámetros

# Definimos una grilla de IQ para realizar la integración numérica
iq_grid = np.linspace(0, 200, 10000)
delta = iq_grid[1] - iq_grid[0]

def weight(iq, mu_actual, iq_min, iq_max, w_low, w_mid, w_high):
    """Función de peso con iq_min, iq_max y factores de reproducción ajustables."""
    w = np.ones_like(iq)
    k = mu_actual / mu_inicial  # Ajuste dinámico
    
    w[(iq >= iq_min*k) & (iq <= iq_max*k)] = w_mid  
    w[iq > iq_max*k] = w_high                  
    w[iq < iq_min*k] = w_low                    
    return w

def evaluar_configuracion(iq_min, iq_max, w_low, w_mid, w_high):
    """Calcula el IQ promedio después de una generación para una configuración dada."""
    mu_actual = mu_inicial
    phi = norm.pdf(iq_grid, mu_actual, sigma)
    w_iq = weight(iq_grid, mu_actual, iq_min, iq_max, w_low, w_mid, w_high)

    numerador = np.sum(iq_grid * phi * w_iq) * delta
    denominador = np.sum(phi * w_iq) * delta
    mu_sel = numerador / denominador  # IQ promedio de los padres ponderado

    S = mu_sel - mu_actual
    return mu_actual + heritability * S  # IQ promedio en la siguiente generación

# Rango de valores a probar
iq_min_values = np.linspace(50, 100, 10)   # Rango de IQ mínimo
iq_max_values = np.linspace(100, 150, 10)  # Rango de IQ máximo
w_low_values = np.linspace(0.1, 1.0, 5)    # Factores de reproducción para IQ bajo
w_mid_values = np.linspace(1.0, 2.0, 5)    # Factores de reproducción para IQ medio
w_high_values = np.linspace(1.5, 3.0, 5)   # Factores de reproducción para IQ alto

# Búsqueda de la mejor configuración
best_params = None
best_mu = -np.inf

# Explorar todas las combinaciones posibles
for iq_min, iq_max, w_low, w_mid, w_high in product(iq_min_values, iq_max_values, w_low_values, w_mid_values, w_high_values):
    mu_next = evaluar_configuracion(iq_min, iq_max, w_low, w_mid, w_high)
    
    if mu_next > best_mu:
        best_mu = mu_next
        best_params = (iq_min, iq_max, w_low, w_mid, w_high)

# Resultados óptimos
best_iq_min, best_iq_max, best_w_low, best_w_mid, best_w_high = best_params
print("Valores óptimos encontrados:")
print(f" - IQ mínimo óptimo: {best_iq_min}")
print(f" - IQ máximo óptimo: {best_iq_max}")
print(f" - Factor de reproducción (IQ bajo): {best_w_low}")
print(f" - Factor de reproducción (IQ medio): {best_w_mid}")
print(f" - Factor de reproducción (IQ alto): {best_w_high}")
print(f" - IQ promedio en la siguiente generación: {best_mu:.2f}")
