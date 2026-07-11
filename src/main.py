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

    A = 1e7        # 1/s
    Ea = 80000     # J/mol
    R = 8.314      # J/(mol·K)

    k = A * math.exp(-Ea / (R * temperature))
    if reaction_order == 0:
        reaction_rate = k
    elif reaction_order == 1:
        reaction_rate = k * concentration
    elif reaction_order == 2:
        reaction_rate = k * concentration ** 2
    else:
        print("Invalid reaction order.")
        return

    print(f"\nTemperature = {temperature:.1f} K")
    print(f"Concentration = {concentration:.2f} mol/L")
    print(f"Rate Constant = {k:.6e} 1/s")
    print(f"Reaction Rate = {reaction_rate:.6e} mol/(L·s)")
    print(f"Reaction Order = {reaction_order}")

if __name__ == "__main__":
    main()