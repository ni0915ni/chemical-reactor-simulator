def batch_reactor(
    concentration,
    k,
    reaction_order,
    simulation_time,
    dt,
):
    time_history = []
    concentration_history = []

    time = 0.0
    current_concentration = concentration

    while time <= simulation_time:

        if reaction_order == 0:
            reaction_rate = k

        elif reaction_order == 1:
            reaction_rate = k * current_concentration

        elif reaction_order == 2:
            reaction_rate = k * current_concentration ** 2

        else:
            raise ValueError("Invalid reaction order.")

        time_history.append(time)
        concentration_history.append(current_concentration)

        current_concentration = max(
            0.0,
            current_concentration - reaction_rate * dt,
        )

        time += dt

    return time_history, concentration_history

def cstr_steady_state(
    inlet_concentration,
    k,
    reaction_order,
    residence_time,
):
    if reaction_order == 0:
        outlet_concentration = inlet_concentration - k * residence_time

    elif reaction_order == 1:
        outlet_concentration = inlet_concentration / (
            1 + k * residence_time
        )

    elif reaction_order == 2:
        a = k * residence_time
        b = 1.0
        c = -inlet_concentration

        discriminant = b**2 - 4 * a * c

        outlet_concentration = (
            -b + discriminant**0.5
        ) / (2 * a)

    else:
        raise ValueError("Invalid reaction order.")

    return max(0.0, outlet_concentration)

def pfr_reactor(
    inlet_concentration,
    k,
    reaction_order,
    residence_time,
    dt,
):
    time_history = []
    concentration_history = []

    time = 0.0
    current_concentration = inlet_concentration

    while time <= residence_time:
        if reaction_order == 0:
            reaction_rate = k
        elif reaction_order == 1:
            reaction_rate = k * current_concentration
        elif reaction_order == 2:
            reaction_rate = k * current_concentration**2
        else:
            raise ValueError("Invalid reaction order.")

        time_history.append(time)
        concentration_history.append(current_concentration)

        current_concentration = max(
            0.0,
            current_concentration - reaction_rate * dt,
        )

        time += dt

    return time_history, concentration_history