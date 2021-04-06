# Using graphs to examine the law of large numbers and how 
# it differs from central limit theory

import matplotlib.pyplot as plt
import numpy as np

# parameters
population_size = 2.0e5
sample_size = 50
num_of_samples = 500


# generate shuffled sample population data and plot
population = 1 / np.logspace(np.log10(.001),np.log10(5),int(population_size))
np.random.shuffle(population)
plt.plot(population[::int(1e3)], 'o', label='Population')
plt.title("Population", fontsize=14)
plt.xlabel('Sample Number')
plt.ylabel('Data Value')
plt.show(block=False)
plt.pause(3)
plt.close()

# obtaining multiple sample means via monte carlo samplimg 
# (random sampling from the population)
sample_means = [np.mean(np.random.choice(population, size=sample_size)) for expirement in range(num_of_samples)]
trueMean = np.mean(population)
plt.plot(sample_means, 'ko', label='Sample Means')
plt.title("Sample Means", fontsize=14)
plt.plot([0, num_of_samples], [trueMean, trueMean], 'r', linewidth=5, label='True mean')
plt.xlabel('sample Number')
plt.ylabel('Mean Value')
plt.legend()
plt.show(block=False)
plt.pause(3)
plt.close()

# cumalitive averages
cumave = np.cumsum(sample_means) / np.arange(1,num_of_samples+1)
plt.plot(cumave,'ko',label='Cumulative averages')
plt.plot([0,num_of_samples],[trueMean,trueMean],'r',linewidth=5,label='True mean')
plt.xlabel('Sample number')
plt.ylabel('Mean value')
plt.legend()
plt.show()
plt.pause(3)
plt.close()