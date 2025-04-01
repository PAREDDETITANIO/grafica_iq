import math
import numpy as np
import matplotlib.pyplot as plt


k=100
m=1
g=9.8
l=1


w1 = math.sqrt(((k/m) + ((2*g)/l) + math.sqrt((k**2)/(m**2) + (4*g**2)/(l**2))) / 2)
w2 = math.sqrt(((k/m) + ((2*g)/l) - math.sqrt((k**2)/(m**2) + (4*g**2)/(l**2))) / 2)

A=1
p1=0
p2=0

t_values = []
x1_values = []
x2_values = []


for t in range(0, 100):  
    t_real = t * 0.1  
    x1 = A * math.cos(w1 * t_real + p1) + A * math.cos(w2 * t_real + p2)
    x2 = ((g/l) / ((g/l) + w1**2)) * A * math.cos(w1 * t_real + p1) + ((g/l) / ((g/l) + w2**2)) * A * math.cos(w2 * t_real + p2)

    # Guardamos los valores
    t_values.append(t_real)
    x1_values.append(x1)
    x2_values.append(x2)


plt.figure(figsize=(10, 5))
plt.plot(t_values, x1_values, label="x1(t)", color="blue")
plt.plot(t_values, x2_values, label="x2(t)", color="red", linestyle="dashed")
plt.xlabel("Tiempo (s)")
plt.ylabel("Desplazamiento")
plt.title("Oscilaciones acopladas")
plt.legend()
plt.grid()
plt.show()