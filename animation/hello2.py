import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from sklearn import datasets

digits = datasets.load_digits()
images_and_labels = list(zip(digits.images, digits.target))

fig = plt.figure()
i=0
im = plt.imshow(images_and_labels[0][0], animated=True, cmap='gray')

def updatefig(*arg):
    global i
    if (i < len(images_and_labels)):
        i += 1
    else:
      i = 0

    im.set_array(images_and_labels[i][0])
    return im,

anim = animation.FuncAnimation(fig, updatefig, blit=True)
plt.show()
