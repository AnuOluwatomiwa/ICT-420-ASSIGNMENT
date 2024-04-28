from tabulate import tabulate
import pandas as pd

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

# Create a DataFrame for the table
table = {'t': t_values, 'f(t)': [f(t) for t in t_values]}

# Use tabulate to format the table
formatted_table = tabulate(pd.DataFrame(table), headers='keys', tablefmt='grid')

# Display the formatted table
print(formatted_table)
