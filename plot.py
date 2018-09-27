import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 1, 1000)

U = np.sin(5 * np.pi * t)

plt.plot(t, U)
plt.xlabel('t / s')
plt.ylabel('U / V')
plt.savefig('build/plot.pdf')
