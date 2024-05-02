import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# Constants
T = 10  # Period in seconds
A = 26  # Last two digits of my matriculation number (210502126)
omega = 2 * np.pi / T

# Time instances and values
time_points = np.array([T/6, T/3, T/2, 2*T/3, 5*T/6, T,
                        7*T/6, 4*T/3, 3*T/2, 5*T/3, 11*T/6, 2*T])
f_t_values = 0.8 * A * np.cos(omega * time_points)

# Create a table with tabulate
table_data = [["Time (s)", "f(t) (Volts)"]]
for tp, fv in zip(time_points, f_t_values):
    table_data.append([f"{tp:.2e}", f"{fv:.2f}"])

print(tabulate(table_data, headers='firstrow', tablefmt='fancy_grid'))

# Plot the signal
t = np.linspace(0, 2 * T, 1000)
f_t = 0.8 * A * np.cos(omega * t)

plt.plot(t, f_t, 'r-', label='f(t) = 0.8A cos(ωt)')
plt.plot(time_points, f_t_values, 'bo', label='Given points')

# Adding personal information to the plot in the top-right corner
name = "Bamidele Israel"
matriculation_number = "210502126"
date = "April 19th, 2024"

# Place the text slightly outside the plot area to avoid touching the data
plt.text(1.07, 1.07, f"Name: {name}\nMatriculation No.: {matriculation_number}\nDate: {date}",
         ha='right',  # Horizontal alignment
         va='top',  # Vertical alignment
         transform=plt.gca().transAxes)  # Ensure coordinates are in axes space

# Plot adjustments
plt.subplots_adjust(top=0.85)  # Increase top margin to create space
plt.title("Signal f(t) from t = 0 to t = 2T")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (V)")
plt.grid(True)
plt.legend()
plt.show()
