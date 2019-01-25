import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
sales = [5280, 5501, 5469, 5480, 5533, 5554]
target = [5280, 5500, 5729, 5968, 6217, 6476]
ad = [1056, 950, 739, 528, 317, 316]
sn = [0, 106, 317, 528, 739, 739]

plt.xlabel('month')
plt.ylabel('money')
plt.plot(x, sales, 'red')
plt.plot(x, target, 'blue')
plt.plot(x, ad, 'green')
plt.plot(x, sn, 'black')
plt.legend(['sales', 'target', 'Ad cost', 'social network cost'])

plt.show()