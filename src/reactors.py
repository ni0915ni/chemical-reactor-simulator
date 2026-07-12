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