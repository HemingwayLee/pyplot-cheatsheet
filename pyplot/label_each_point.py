import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(10, 1)
y = np.random.randn(10, 1)
txts = ['one','two','three','four','five','six','seven','eight','nine','ten']

fig, ax = plt.subplots()
ax.scatter(x, y)

for i, txt in enumerate(txts):
  ax.annotate(txt, (x[i],y[i]))

plt.show()