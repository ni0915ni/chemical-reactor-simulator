from plot_batch import plot_batch
from reactors import batch_reactor
from kinetics import calculate_rate_constant
import math

def main():
    print("=" * 40)
    print("Chemical Reactor Simulator")
    print("Version 0.1")
    print("Author: Connie Yu")
    print("=" * 40)

    temperature = float(input("Enter temperature (K): "))
    concentration = float(input("Enter concentration (mol/L): "))
    reaction_order = int(input("Reaction order (0/1/2): "))

    simulation_time = float(input("Simulation time (s): "))
    dt = float(input("Time step (s): "))

    A = 1e7        # 1/s
    Ea = 80000     # J/mol
    R = 8.314      # J/(mol·K)

    k = calculate_rate_constant(
    A,
    Ea,
    R,
    temperature
    )

    time_history = []
    concentration_history = []

    time = 0.0
    current_concentration = concentration

    time_history, concentration_history = batch_reactor(
    concentration,
    k,
    reaction_order,
    simulation_time,
    dt,
    )

    plot_batch(time_history, concentration_history)

    print(f"\nTemperature = {temperature:.1f} K")
    print(f"Simulation Time = {simulation_time:.1f} s")
    print(f"Final Concentration = {concentration_history[-1]:.2f} mol/L")
    print(f"Reaction Order = {reaction_order}")
    print(f"Rate Constant = {k:.6e} 1/s")

if __name__ == "__main__":
    main()