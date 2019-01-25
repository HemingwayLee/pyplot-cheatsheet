from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')

x = [1,2,3,4,5]
y = [1,2,3,4,5]
z = [1,2,3,4,5]

ax.plot(x, y, z, label='parametric curve')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

plt.show()

