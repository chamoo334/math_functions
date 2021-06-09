import numpy as np
import matplotlib.pyplot as plt


def gaussian(t, h):
    """Returns Gaussian from """
    return np.exp(-4*np.log(2)*t**2 / h**2 )


t = np.linspace(-.03, .03, 1001)
h = .000999
g = gaussian(t, h)
plt.plot(t,g)
plt.xlabel('t')
plt.ylabel('y')
plt.show()