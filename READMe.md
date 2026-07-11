# Chemical Reactor Simulator

A Python project for learning chemical reaction engineering through simulation. and process simulation. 

## Current Features

- Calculate the Arrhenius rate constant from temperature
- Accept user temperature input
- Plot temperature versus rate constant
- Save generated figures automatically
- Calculate first-order reaction rate
- Plot Arrhenius equation
- Temperature sweep (300–800 K)

## Equation

The Arrhenius equation is:

k = A exp(-Ea / RT)

where:

- k is the reaction rate constant
- A is the pre-exponential factor
- Ea is the activation energy
- R is the gas constant
- T is the absolute temperature

Reaction rate

r = kC

## Files

```
src/
    main.py
    plot_arrhenius.py

figures/
    arrhenius_plot.png
```

## Example

For:

- Temperature = 350 K
- A = 1.0 × 10^7 1/s
- Ea = 80,000 J/mol

The program calculates:

- k ≈ 1.15 × 10^-5 1/s

Input

```
Temperature = 500 K
Concentration = 2 mol/L
```

Output

```
Rate Constant = 4.39e-02 1/s

Reaction Rate = 8.77e-02 mol/(L·s)
```

## Project Structure

```text
chemical-reactor-simulator/
├── figures/
│   └── arrhenius_plot.png
├── src/
│   ├── main.py
│   └── plot_arrhenius.py
├── README.md
└── requirements.txt

## Future Work

- Batch Reactor
- CSTR
- Plug Flow Reactor
- Multiple reactions
- Parameter fitting
- Optimization