from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
theta = np.linspace(-4*np.pi, 4*np.pi, 100)

z = np.linspace(-2,2,100)
r = z**2 + 1
x = r*np.sin(theta)
y = r*np.cos(theta)

ax.scatter(x, y, z)
ax.legend()
plt.show()

