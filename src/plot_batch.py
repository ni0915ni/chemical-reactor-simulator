import matplotlib.pyplot as plt


def plot_batch(time_history, concentration_history):
    plt.plot(time_history, concentration_history)

    plt.xlabel("Time (s)")
    plt.ylabel("Concentration (mol/L)")
    plt.title("Batch Reactor Concentration Profile")
    plt.grid(True)

    plt.savefig("figures/batch_reactor_plot.png")
    plt.show()