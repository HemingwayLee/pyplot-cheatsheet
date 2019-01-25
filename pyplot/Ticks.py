import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,7,4]

plt.plot(x, y)
plt.xticks(np.arange(min(x), max(x)+1, 1.0))

plt.show()