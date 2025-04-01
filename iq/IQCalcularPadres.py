from scipy.stats import norm

iq_p=160
iq_m=160


# Parámetros
mu =100+0.8*(((iq_p+iq_m)/2)-100)
sigma = 15
x =160
p=45000000

# Calcular Z
Z = (x - mu) / sigma
print("media:",mu)
# Calcular la probabilidad acumulada
probabilidad = norm.cdf(Z)
if probabilidad < 0.5:
    print(round((probabilidad)*100, 5),"%")
    print("en el mundo hay","{:,.2f}".format((probabilidad)*8*10**9).replace(",", "X").replace(".", ",").replace("X", "."))
    print("en la poblacion hay","{:,.2f}".format((probabilidad)*8*10**9).replace(",", "X").replace(".", ",").replace("X", "."))
else:
    print(round((1-probabilidad)*100, 5),"%")
    print("en el mundo hay","{:,.2f}".format((1-probabilidad)*8*10**9).replace(",", "X").replace(".", ",").replace("X", "."))
    print("en la poblacion hay","{:,.2f}".format((1-probabilidad)*p).replace(",", "X").replace(".", ",").replace("X", "."))
#*(1.17*10**5)*(10**6))

