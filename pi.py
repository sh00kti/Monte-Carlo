#! /usr/bin/python3.9

import numpy as np

POINTS = 100000
RADIUS = 5  # The dimensions of the square & circle are largely unimportant

def findPi(pts, rad):
    inside = 0

    for i in range(pts):
        # generate a random (x, y) coordinate:
        x = np.random.uniform(-rad, rad)
        y = np.random.uniform(-rad, rad)
        # check if that point is within the circle, if inside, increment 'inside'
        if x**2 + y**2 <= rad**2:
            inside += 1

    pi = (4*inside) / pts
    return pi

print(findPi(POINTS, RADIUS))
