from temperature_sweep import temperature_sweep
from reactors import batch_reactor, cstr_steady_state, pfr_reactor
from plotting import plot_batch, plot_pfr, plot_cstr
from kinetics import calculate_rate_constant

def main():
    print("=" * 40)
    print("Chemical Reactor Simulator")
    print("Version 0.1")
    print("Author: Connie Yu")
    print("=" * 40)

    print("\nSelect Reactor")
    print("1. Batch Reactor")
    print("2. CSTR")
    print("3. PFR")
    print("4. Temperature Sweep")

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

        cstr_residence_times = []
        cstr_conversions = []

        number_of_points = 51

        for index in range(number_of_points):
            current_residence_time = (
                residence_time * index / (number_of_points - 1)
            )

            current_outlet_concentration = cstr_steady_state(
                concentration,
                k,
                reaction_order,
                current_residence_time,
            )

            current_conversion = (
                concentration - current_outlet_concentration
            ) / concentration

            cstr_residence_times.append(current_residence_time)
            cstr_conversions.append(current_conversion)

        plot_cstr(
            cstr_residence_times,
            cstr_conversions,
        )
    
    elif choice == "3":
        residence_time = float(input("Residence time (s): "))
        dt = float(input("Time step (s): "))

        time_history, concentration_history = pfr_reactor(
            concentration,
            k,
            reaction_order,
            residence_time,
            dt,
        )

        outlet_concentration = concentration_history[-1]

        conversion = (
            concentration - outlet_concentration
        ) / concentration

        print("\nReactor Type = PFR")
        print(f"Temperature = {temperature:.1f} K")
        print(f"Residence Time = {residence_time:.1f} s")
        print(
            f"Outlet Concentration = "
            f"{outlet_concentration:.4f} mol/L"
        )
        print(f"Conversion = {conversion:.2%}")
        print(f"Reaction Order = {reaction_order}")
        print(f"Rate Constant = {k:.6e} 1/s")

        plot_pfr(
        time_history,
        concentration_history,
        )
    
    elif choice == "4":
        temperature_sweep()

    else:
        print("Invalid reactor selection.")

if __name__ == "__main__":
    main()