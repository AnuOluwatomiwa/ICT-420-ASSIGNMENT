import pandas as pd
from tabulate import tabulate

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

# Create a DataFrame
t_values = list(range(0, 2 * T + 1))
data = {'t': t_values, 'f(t)': [f(t) for t in t_values]}
df = pd.DataFrame(data)

# Transpose the DataFrame to render it horizontally
df_transposed = df.T

# Render the table horizontally with tabulate
formatted_table = tabulate(df_transposed, headers='keys', tablefmt='grid')

# Display the transposed table
print(formatted_table)
