import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

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

# Generate a list of t values from 0 to 2T in integer steps
t_values = list(range(0, 2 * T + 1))

# Create a DataFrame
data = {'t': t_values, 'f(t)': [f(t) for t in t_values]}
df = pd.DataFrame(data)

# Transpose the DataFrame to render it horizontally
df_transposed = df.T

# Render the table horizontally with tabulate
formatted_table = tabulate(df_transposed, headers='keys', tablefmt='grid')

# Plot the graph of f(t) against t
plt.plot(df['t'], df['f(t)'], marker='o', linestyle='-', color='b')
plt.title("Plot of f(t) against t")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.grid(True)  # Optional: Adds a grid to the plot for better readability
plt.show()  # Display the plot

# Display the transposed table in a designed format
print(formatted_table)
