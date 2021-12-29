#! /usr/bin/python3.9

import numpy as np
import matplotlib.pyplot as plt
from itertools import product, combinations

fig = plt.figure()
ax = fig.add_subplot(132, projection='3d')

def drawCube(side):
    # draw cube
    r = [-1, 1]
    for s, e in combinations(np.array(list(product(r, r, r))), 2):
        if np.sum(np.abs(s-e)) == r[1]-r[0]:
            ax.plot3D(*zip(s, e), color="green")
    ax.set_title("Cube")

def drawPoints(points):
    xs = []
    ys = []
    zs = []

    for i in range(points):
        xs.append(np.random.uniform(-1, 1))
        ys.append(np.random.uniform(-1, 1))
        zs.append(np.random.uniform(-1, 1))

    ax.scatter3D(xs, ys, zs)

drawCube(2)
drawPoints(300)
plt.show()