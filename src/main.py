import math

def main():
    print("=" * 40)
    print("Chemical Reactor Simulator")
    print("Version 0.1")
    print("Author: Connie Yu")
    print("=" * 40)

    temperature = float(input("Enter temperature (K): "))
    concentration = float(input("Enter concentration (mol/L): "))

    A = 1e7        # 1/s
    Ea = 80000     # J/mol
    R = 8.314      # J/(mol·K)

    k = A * math.exp(-Ea / (R * temperature))
    reaction_rate = k * concentration
    
    print(f"\nTemperature = {temperature:.1f} K")
    print(f"Concentration = {concentration:.2f} mol/L")
    print(f"Rate Constant = {k:.6e} 1/s")
    print(f"Reaction Rate = {reaction_rate:.6e} mol/(L·s)")

if __name__ == "__main__":
    main()