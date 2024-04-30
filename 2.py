import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate

# Constants
T = 10  # 10 units of time
A = 26  # Last two digits of matriculation number
ω = 2 * np.pi / T

# Define time points
time_points = np.array([T/6, T/3, T/2, 2 * T/3, 5 * T/6, T, 7 * T/6, 4 * T/3, 3 * T/2, 5 * T/3, 11 * T/6, 2 * T])

# Signal f(t)
f_t_values = 0.8 * A * np.cos(ω * time_points)

# Create a table of values
table_data = {
    't': [f"{tp:.6f}" for tp in time_points],  # Format time points for readability
    'f(t)': [f"{ft:.2f}" for ft in f_t_values],  # Format f(t) for consistency
}

# Use tabulate to render the table horizontally
print("Table of values for f(t) = 0.8 * A * cos(ωt)")
print(tabulate(table_data, headers='keys', tablefmt='plain', showindex=False))

# Create the plot
t = np.linspace(0, 2 * T, 1000)  # Generate time samples
f_t = 0.8 * A * np.cos(ω * t)  # Calculate f(t)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, f_t, label='f(t) = 0.8 * A * cos(ωt)', color='b', linestyle='-', linewidth=2)  # Main plot
plt.scatter(time_points, f_t_values, color='r', label='Sample Points')  # Highlight sample points

plt.xlabel('t (units of time)')
plt.ylabel('f(t) (volts)')
plt.title('Plot of f(t) against t from t = 0 to t = 2T')
plt.legend()
plt.grid(True)
plt.show()
