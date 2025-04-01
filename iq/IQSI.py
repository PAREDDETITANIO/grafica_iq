import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Parámetros iniciales
mu = 100  # Media inicial del IQ
sigma = 15  # Desviación estándar inicial del IQ
h2 = 0.8  # Heredabilidad del IQ
threshold = 100  # Umbral de selección (IQ < 100 no se reproduce)
generations = 100  # Número de generaciones

# Función para calcular la media y desviación estándar truncada
def truncate_distribution(mu, sigma, threshold):
    alpha = (threshold - mu) / sigma  # Puntaje Z del umbral
    Z = 1 - norm.cdf(alpha)  # Proporción de la población por encima del umbral
    mu_trunc = mu + sigma * norm.pdf(alpha) / Z  # Media truncada
    sigma_trunc_sq = sigma**2 * (1 + alpha * norm.pdf(alpha) / Z - (norm.pdf(alpha) / Z)**2)  # Varianza truncada
    sigma_trunc = np.sqrt(sigma_trunc_sq)  # Desviación estándar truncada
    return mu_trunc, sigma_trunc

# Simulación a lo largo de las generaciones
mu_history = [mu]  # Lista para almacenar la media en cada generación
sigma_history = [sigma]  # Lista para almacenar la desviación estándar en cada generación

for gen in range(1, generations + 1):
    # Calcula la media y desviación estándar truncada
    mu_trunc, sigma_trunc = truncate_distribution(mu, sigma, threshold)
    
    # Calcula el cambio en la media debido a la selección
    S = mu_trunc - mu  # Diferencial de selección
    delta_mu = h2 * S  # Cambio en la media
    
    # Actualiza la media y la desviación estándar para la siguiente generación
    mu = mu + delta_mu
    sigma = np.sqrt(h2 * sigma_trunc**2 + (1 - h2) * sigma**2)
    
    # Guarda los valores en la historia
    mu_history.append(mu)
    sigma_history.append(sigma)

# Resultados finales
print(f"Media final después de {generations} generaciones: {mu_history[-1]:.2f}")
print(f"Desviación estándar final después de {generations} generaciones: {sigma_history[-1]:.2f}")

# Gráfica de la evolución
plt.figure(figsize=(10, 6))
plt.plot(range(generations + 1), mu_history, label="Media del IQ", color="blue")
plt.plot(range(generations + 1), sigma_history, label="Desviación estándar del IQ", color="red")
plt.axhline(y=100, color="black", linestyle="--", label="Media inicial (100)")
plt.axhline(y=15, color="green", linestyle="--", label="Desviación estándar inicial (15)")
plt.xlabel("Generación")
plt.ylabel("Valor")
plt.title("Evolución del IQ promedio y desviación estándar a lo largo de las generaciones")
plt.legend()
plt.grid()
plt.show()