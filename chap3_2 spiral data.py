import numpy as np
import matplotlib.pyplot as plt

import spiral

x, y = spiral.create_data(samples=100, classes=3)
plt.scatter(x[:,0], x[:,1], c=y, cmap='brg')
plt.show()
