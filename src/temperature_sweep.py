import matplotlib.pyplot as plt

from kinetics import calculate_rate_constant
from reactors import cstr_steady_state
def temperature_sweep():

    concentration = float(input("Feed concentration (mol/L): "))
    reaction_order = int(input("Reaction order (0/1/2): "))
    residence_time = float(input("Residence time (s): "))

    A = 1e7
    Ea = 80000
    R = 8.314

    temperatures = []
    conversions = []

    for temperature in range(300, 801, 10):
        k = calculate_rate_constant(A, Ea, R, temperature)

        outlet_concentration = cstr_steady_state(
            concentration,
            k,
            reaction_order,
            residence_time,
        )

        conversion = (
            concentration - outlet_concentration
            ) / concentration

        temperatures.append(temperature)
        conversions.append(conversion)

    plt.plot(temperatures, conversions)
    plt.xlabel("Temperature (K)")
    plt.ylabel("Conversion")
    plt.title("Temperature Sweep")

    plt.grid(True)

    plt.savefig("figures/temperature_sweep_plot.png")
    
    plt.show()