from pathlib import Path

import matplotlib.pyplot as plt


FIGURES_DIR = Path(__file__).resolve().parent.parent / "figures"
FIGURES_DIR.mkdir(exist_ok=True)


def plot_concentration_profile(
    x_values,
    concentration_values,
    *,
    title,
    x_label,
    filename,
):
    plt.figure(figsize=(8, 5))
    plt.plot(x_values, concentration_values)

    plt.xlabel(x_label)
    plt.ylabel("Concentration (mol/L)")
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(FIGURES_DIR / filename, dpi=300)
    plt.show()
    plt.close()


def plot_batch(time_history, concentration_history):
    plot_concentration_profile(
        time_history,
        concentration_history,
        title="Batch Reactor Concentration Profile",
        x_label="Time (s)",
        filename="batch_reactor_plot.png",
    )


def plot_pfr(residence_time_history, concentration_history):
    plot_concentration_profile(
        residence_time_history,
        concentration_history,
        title="Plug Flow Reactor Concentration Profile",
        x_label="Residence Time (s)",
        filename="pfr_concentration_profile.png",
    )


def plot_cstr(
    residence_times,
    conversions,
):
    plt.figure(figsize=(8, 5))
    plt.plot(residence_times, conversions)

    plt.xlabel("Residence Time (s)")
    plt.ylabel("Conversion")
    plt.title("CSTR Conversion vs Residence Time")
    plt.ylim(0, 1)
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(
        FIGURES_DIR / "cstr_conversion_plot.png",
        dpi=300,
    )
    plt.show()
    plt.close()


def plot_temperature_sweep(
    temperatures,
    conversions,
):
    plt.figure(figsize=(8, 5))
    plt.plot(temperatures, conversions)

    plt.xlabel("Temperature (K)")
    plt.ylabel("Conversion")
    plt.title("CSTR Conversion vs Temperature")
    plt.ylim(0, 1)
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(
        FIGURES_DIR / "temperature_sweep.png",
        dpi=300,
    )
    plt.show()
    plt.close()