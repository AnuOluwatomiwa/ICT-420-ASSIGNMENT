import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import time  # for sleep

# Constants
T = 10  # Value of T
A = 26  # Last two digits of my matriculation number (210502126)

# Function definition
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

# Display the table
formatted_table = tabulate(df.T, headers='keys', tablefmt='grid')
print(formatted_table)  # Print the table before plotting

# Plot the graph
plt.plot(df['t'], df['f(t)'], marker='o', linestyle='-', color='b')
plt.title("Plot of f(t) against t")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.grid(True)

# Annotate the graph with top-right text
name = "John Doe"
matric_no = "12345678"
plt.text(1.05, 1.05, f"name: {name}\nmatriculation no: {matric_no}",
         horizontalalignment='right',
         verticalalignment='top',
         transform=plt.gca().transAxes)

# Show the graph and wait for 5 seconds, then close and exit
plt.show()
time.sleep(5)  # Wait for a few seconds before closing the plot
plt.close()  # Close the plot to automatically exit the program
