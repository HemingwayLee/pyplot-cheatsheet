from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# With y = x, you don't actually have 2 lists. The assignment just copies the reference to the list, not actual list
x = np.linspace(-5,5,num=20)
y = list(x)
z = list(x)

for i, e in enumerate(x):
  x[i] = e + 1.5*np.random.rand()

for i, e in enumerate(x):
  y[i] = e + 1.3*np.random.rand()

for i, e in enumerate(x):
  z[i] = e + 1.7*np.random.rand()

ax.scatter(x, y, z)
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

print(x)
print(y)
print(z)

plt.show()

