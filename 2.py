import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Constants
T = 10  # 10 units of time
A = 26  # Last two digits of matriculation number
ω = 2 * np.pi / T

# Define time points
time_points = np.array([T/6, T/3, T/2, 2 * T/3, 5 * T/6, T, 7 * T/6, 4 * T/3, 3 * T/2, 5 * T/3, 11 * T/6, 2 * T])
t = np.linspace(0, 2 * T, 1000)

# Signal f(t)
f_t = 0.8 * A * np.cos(ω * t)

# Create the table of values
table_data = {
    't': time_points,
    'f(t)': 0.8 * A * np.cos(ω * time_points),
}
table_df = pd.DataFrame(table_data)

# Print the table of values
print("Table of values for f(t) = 0.8A * cos(ωt)")
print(table_df)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(t, f_t, label='f(t) = 0.8A * cos(ωt)', color='b', linestyle='-', linewidth=2)
plt.scatter(time_points, 0.8 * A * np.cos(ω * time_points), color='r', label='Sample Points')

plt.xlabel('t (units of time)')
plt.ylabel('f(t) (volts)')
plt.title('Plot of f(t) against t from t = 0 to t = 2T')
plt.legend()
plt.grid(True)
plt.show()


























#import numpy as np
#import matplotlib.pyplot as plt
#
## Constants
#T = 10e-6  # 10 microseconds
#A = 26  # Last two digits of matriculation number
#ω = 2 * np.pi / T
#
## Define time points
#time_points = np.array([T/6, T/3, T/2, 2 * T/3, 5 * T/6, T, 7 * T/6, 4 * T/3, 3 * T/2, 5 * T/3, 11 * T/6, 2 * T])
#t = np.linspace(0, 2 * T, 1000)
#
## Signal f(t)
#f_t = 0.8 * A * np.cos(ω * t)
#
## Create the plot
#plt.figure(figsize=(10, 6))
#plt.plot(t, f_t, label='f(t) = 0.8A*cos(ωt)', color='b', linestyle='-', linewidth=2)
#plt.scatter(time_points, 0.8 * A * np.cos(ω * time_points), color='r', label='Sample Points')
#
#plt.xlabel('t (seconds)')
#plt.ylabel('f(t) (volts)')
#plt.title('Plot of f(t) against t from t = 0 to t = 2T')
#plt.legend()
#plt.grid(True)
#plt.show()
#