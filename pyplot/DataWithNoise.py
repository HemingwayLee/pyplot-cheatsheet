import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(10, 1)
y = 2*x + 3 + 0.1*np.random.randn(10, 1)

plt.scatter(x, y)
plt.show()