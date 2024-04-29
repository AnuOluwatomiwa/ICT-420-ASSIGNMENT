import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import time
import sys

# Constants
T = 10  # Value of T
A = 26  # Last two digits of my matriculation number (210502126)

# Function definition based on the piecewise conditions
def f(t):
    if 0 <= t <= T / 2:
        return A - (4 * A / T) * t
    elif T / 2 < t <= T:
        return -3 * A + (4 * A / T) * t
    elif T < t <= 3 * T / 2:
        return 5 * A - (4 * A / T) * t
    elif 3 * T / 2 < t <= 2 * T:
        return -7 * A + (4 * A / T) * t

# Create the DataFrame
t_values = list(range(0, 2 * T + 1))
data = {'t': t_values, 'f(t)': [f(t) for t in t_values]}
df = pd.DataFrame(data)

# Print the table of values
formatted_table = tabulate(df.T, headers='keys', tablefmt='grid')
print(formatted_table)

# Plot the graph
plt.plot(df['t'], df['f(t)'], marker='o', linestyle='-', color='b')
plt.title("Plot of f(t) against t")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.grid(True)

# Add annotation at the top-right corner
name = "Bamidele Israel"
matric_no = "210502126"
plt.text(1.05, 1.05, f"Name: {name}\nMatriculation no: {matric_no}",
         horizontalalignment='right',
         verticalalignment='top',
         transform=plt.gca().transAxes)

# Non-blocking mode to ensure the plot renders without blocking
plt.show(block=False)

# Pause to ensure the graph has time to render
time.sleep(5)  # Increased delay for additional time to render the plot

# Ask the user if they want to exit
user_input = input("Would you like to exit the program? (y/yes to exit): ")

# If the user says 'y' or 'yes', exit the program
if user_input.lower() in ["y", "yes"]:
    sys.exit()  # Exit the program
