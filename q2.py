import matplotlib.pyplot as plt
import numpy as np

from Point import Point

points = np.random.rand(4,2)
print(points)

plt.plot(points[:,0], points[:,1], 'o')