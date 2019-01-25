import matplotlib.pyplot as plt

plt.subplot(221)
plt.scatter([1,2,3], [5,7,4])

plt.subplot(222)
plt.scatter([3,5,7], [1,2,9])

plt.subplot(223)
plt.scatter([9,3,6], [4,5,0])

plt.subplot(224)
plt.scatter([6,2,7], [2,2,4])
plt.legend(['test'])
plt.show()

# These are subplot grid parameters encoded as a single integer. 
# For example, "111" means "1x1 grid, first subplot" 
#  and "234" means "2x3 grid, 4th subplot".