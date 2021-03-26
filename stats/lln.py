

import matplotlib.pyplot as plt
import numpy as np

# parameters
pop_size = 2.0e5


# generate shuffled sample population data and plot
population = 1 / np.logspace(np.log10(.001),np.log10(5),int(pop_size))
np.random.shuffle(population)
plt.plot(population[::int(1e3)], 'o')
plt.xlabel('sample')
plt.ylabel('Data value')
plt.show()

