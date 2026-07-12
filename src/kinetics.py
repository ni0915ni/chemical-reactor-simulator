import math

def calculate_rate_constant(A, Ea, R, temperature):
    return A * math.exp(-Ea / (R * temperature))