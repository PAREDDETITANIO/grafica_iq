import matplotlib.pyplot as plt
import numpy as np
import math

m = 1
k = 100
g=9.8
l=1


w1 = math.sqrt((g/l)*(2-math.sqrt(2)))
w2 = math.sqrt((g/l)*(2+math.sqrt(2)))


A = 1  
t_values = np.linspace(0, 10, 500)  
x1_values = []
x2_values = []

for t in t_values:
    x1 = A * math.cos(w1 * t) + A * math.cos(w2 * t)
    x2 = A * (1+math.sqrt(2)) * math.cos(w1 * t) + A * (1-math.sqrt(2)) * math.cos(w2 * t)
    x1_values.append(x1)
    x2_values.append(x2)


plt.figure(figsize=(10, 5))
plt.plot(t_values, x1_values, label="x1(t)", linestyle="--", color="blue")
plt.plot(t_values, x2_values, label="x2(t)", linestyle="-", color="red")
plt.xlabel("Tiempo (s)")
plt.ylabel("Desplazamiento")
plt.title("Movimiento de los osciladores acoplados")
plt.legend()
plt.grid()
plt.show()