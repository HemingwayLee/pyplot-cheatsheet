import matplotlib.pyplot as plt
from matplotlib.text import TextPath

data = [["peach", 1.0, 1.0], 
    ["apples", 19, 3.5], 
    ["oranges", 7, 2.2], 
    ["grapes", 23, 7.8]]

for item in data:
    path = TextPath((0,0), item[0])
    plt.plot(item[1], item[2], c="r", marker=path, markersize=100)

plt.show()
