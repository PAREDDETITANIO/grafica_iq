from scipy.stats import norm

iq_p=160
iq_m=160


# Parámetros
mu =100+0.6*(((iq_p+iq_m)/2)-100)
sigma = 15
x =180


# Calcular Z
Z = (x - mu) / sigma

# Calcular la probabilidad acumulada
probabilidad = norm.cdf(Z)
if probabilidad < 0.5:
    print((probabilidad)*100,"%")
else:
    print((1-probabilidad)*100,"%")

#*(1.17*10**5)*(10**6))
print(mu)
