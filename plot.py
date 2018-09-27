""" This will create a very nice plot
"""
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 3, 1000)

U = np.sin(5 * np.pi * t)

plt.plot(t, U, label="Spannung")
plt.xlabel('t / s')
plt.ylabel('U / V')
plt.legend()
plt.savefig('build/plot.pdf')
