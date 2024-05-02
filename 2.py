import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# Constants
T = 10  # Period
A = 26  # Last two digits of my matriculation number (210502126)
omega = 2 * np.pi / T

# Time instances
time_points = np.array([T/6, T/3, T/2, 2*T/3, 5*T/6, T,
                        7*T/6, 4*T/3, 3*T/2, 5*T/3, 11*T/6, 2*T])

# Compute f(t) for each time point
f_t_values = 0.8 * A * np.cos(omega * time_points)

# Create a table for time points and corresponding f(t) values
table = [["Time (s)", "f(t) (Volts)"]]
for tp, fv in zip(time_points, f_t_values):
    table.append([f"{tp:.2e}", f"{fv:.2f}"])

# Display the table with tabulate
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

# Smooth curve for plotting
t = np.linspace(0, 2 * T, 1000)
f_t = 0.8 * A * np.cos(omega * t)

# Plotting the signal
plt.figure()
plt.plot(t, f_t, 'r-', label='f(t) = 0.8A cos(ωt)')
plt.plot(time_points, f_t_values, 'bo', label='Given points')

# Adding personal information to the plot in the top-right corner
name = "Bamidele Israel"
matriculation_number = "210502126"
date = "April 19th, 2024"

# Use plt.text() to add information to the plot
# Coordinates are given in axis fractions to position text at the top-right corner
plt.text(1.05, 1.05, f"Name: {name}\nMatriculation no: {matriculation_number}",
         horizontalalignment='right',
         verticalalignment='top',
         transform=plt.gca().transAxes)

# Plot title and labels
plt.title("Signal f(t) from t = 0 to t = 2T")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (V)")
plt.grid(True)
plt.legend()
plt.show()
