import matplotlib.pyplot as plt
from numpy.random import random

lo = plt.scatter(random(10), random(10), marker='x', color='r')
hi = plt.scatter(random(10), random(10), marker='o', color='b')

plt.legend((lo, hi), ('Low Outlier', 'High Outlier'), fontsize=8)
plt.show()