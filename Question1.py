import pandas as pd
import numpy as np

# Constants
T = 10  # Value of T
A = 26  # Last two digits of my matriculation number (210502126)
t_values = np.linspace(0, T / 2, 11)  # t values from 0 to T/2 (inclusive) with 11 points

# Function to calculate f(t)
def f(t):
    return A - (4 * A / T) * t

# Calculate f(t) for each t in t_values
f_values = [f(t) for t in t_values]

# Create a DataFrame to represent the table of values
table = pd.DataFrame({
    't': t_values,
    'f(t)': f_values
})

table  # Return the table of values
