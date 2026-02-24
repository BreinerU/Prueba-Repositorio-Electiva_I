import matplotlib.pyplot as plt
import numpy as np

# Esta es una grafica
x= np.linspace(0,5,100)
y = x**2 

plt.plot(x,y, legend = "f(x) = 2x")