import matplotlib.pyplot as plt
import vertical

X, y = vertical.create_data(samples=100, classes=3)
plt.scatter(X[:, 0 ], X[:, 1 ], c = y, s = 40 , cmap = 'brg' )
plt.show()

