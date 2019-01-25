import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,7,4]

plt.plot(x, y, 'bo')
plt.plot(x, y, color='green', linestyle="dashed")

plt.show()