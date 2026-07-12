from temperature_sweep import temperature_sweep
from reactors import batch_reactor, cstr_steady_state
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

    print("\nSelect Reactor")
    print("1. Batch Reactor")
    print("2. CSTR")
    print("3. Temperature Sweep")

    choice = input("Choice: ")

    temperature = float(input("Enter temperature (K): "))
    concentration = float(input("Enter concentration (mol/L): "))
    reaction_order = int(input("Reaction order (0/1/2): "))

    A = 1e7        # 1/s
    Ea = 80000     # J/mol
    R = 8.314      # J/(mol·K)

    k = calculate_rate_constant(
    A,
    Ea,
    R,
    temperature
    )

    if choice == "1":
        simulation_time = float(input("Simulation time (s): "))
        dt = float(input("Time step (s): "))

        time_history, concentration_history = batch_reactor(
            concentration,
            k,
            reaction_order,
            simulation_time,
            dt,
        )

        print(f"\nReactor Type = Batch Reactor")
        print(f"Temperature = {temperature:.1f} K")
        print(f"Simulation Time = {simulation_time:.1f} s")
        print(
            f"Final Concentration = "
            f"{concentration_history[-1]:.4f} mol/L"
        )
        print(f"Reaction Order = {reaction_order}")
        print(f"Rate Constant = {k:.6e} 1/s")

        plot_batch(
            time_history,
            concentration_history,
        )

    elif choice == "2":
        residence_time = float(input("Residence time (s): "))

        outlet_concentration = cstr_steady_state(
            concentration,
            k,
            reaction_order,
            residence_time,
        )
    elif choice == "3":
        temperature_sweep()

        conversion = (
            concentration - outlet_concentration
        ) / concentration

        print(f"\nReactor Type = CSTR")
        print(f"Temperature = {temperature:.1f} K")
        print(f"Residence Time = {residence_time:.1f} s")
        print(
            f"Outlet Concentration = "
            f"{outlet_concentration:.4f} mol/L"
        )
        print(f"Conversion = {conversion:.2%}")
        print(f"Reaction Order = {reaction_order}")
        print(f"Rate Constant = {k:.6e} 1/s")

    else:
        print("Invalid reactor selection.")

if __name__ == "__main__":
    main()