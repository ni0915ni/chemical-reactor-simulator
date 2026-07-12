import math
import matplotlib.pyplot as plt


A = 1e7       # Pre-exponential factor, 1/s
Ea = 80000    # Activation energy, J/mol
R = 8.314     # Gas constant, J/(mol·K)

temperatures = []
rate_constants = []

for temperature in range(300, 801, 10):
    k = A * math.exp(-Ea / (R * temperature))

    temperatures.append(temperature)
    rate_constants.append(k)

plt.plot(temperatures, rate_constants)
plt.xlabel("Temperature (K)")
plt.ylabel("Rate Constant k (1/s)")
plt.title("Effect of Temperature on Reaction Rate Constant")
plt.yscale("log")
plt.grid(True)
plt.savefig("figures/arrhenius_plot.png")
plt.show()