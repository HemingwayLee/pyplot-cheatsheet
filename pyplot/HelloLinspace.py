import numpy as np
import matplotlib.pyplot as plt

N = 8
y = np.zeros(N)
print(y)

x1 = np.linspace(0, 10, N, endpoint=True)
print(x1)

x2 = np.linspace(0, 10, N, endpoint=False)
print(x2)

plt.plot(x1, y, 'o')
plt.plot(x2, y + 0.5, 'o')

plt.show()