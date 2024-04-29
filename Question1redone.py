import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import time
#import os   for forcing exit
import sys  # for forcing exit

# Constants
T = 10
A = 26

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

# Annotate the graph with top-right text
name = "Bamidele Israel"
matric_no = "210502126"
plt.text(1.05, 1.05, f"Name: {name}\nMatriculation number: {matric_no}",
         horizontalalignment='right',
         verticalalignment='top',
         transform=plt.gca().transAxes)

# Display the plot for a set duration, then close and exit
plt.show(block=False)  # Non-blocking mode
time.sleep(5)  # Adjust the sleep time as needed
plt.close()  # Close the plot after delay

# Force the program to exit
sys.exit()  # or os._exit(0)