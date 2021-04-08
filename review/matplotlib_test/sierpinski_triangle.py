import numpy
import matplotlib.pyplot as pplot


n = 10000 # number of points

# initialize vectors
x_vect = numpy.zeros(n)
y_vect = numpy.zeros(n)

for i in range(1, n):
    rando = numpy.random.randint(1, 4)
    x_vect[i] = x_vect[i-1]/2 + rando - 1
    y_vect[i] = y_vect[i-1]/2 + rando - 1

    if rando==2:
        y_vect[i] += 2

pplot.plot(x_vect, y_vect, 'k.', markersize=3)
pplot.title('Sierpinski Triangle')
pplot.axis('off')
pplot.show()
