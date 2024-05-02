#We import the necessary libraries
#import matplotlib.pyplot as plt
#import numpy as np
#
#t = np.arange(0, 4*np.pi, 0.1)
#y1 = 400/np.pi*np.cos(0.2*np.pi*t)
#y2 = -400/(3*np.pi)*np.cos(0.6*np.pi*t)
#yt1 = y1 + y2
#
#plt.plot(t, y1, t, y2, t, yt1)

#We import the necessary libraries
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0,5,0.1)
y1 = 100 - 400 * t / 10
t = np.arange(5,10,0.1)
y1 = 400 * t / 10 - 300