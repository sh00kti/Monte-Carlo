#! /usr/bin/python3.9

import numpy as np

POINTS = 1_000_000
LIM1 = -2
LIM2 = 3

def func(x):
    return np.sin(x**2)

def hitormiss(func, lim1, lim2, pts):
    xs = np.linspace(lim1, lim2, 300)
    ys = func(xs)
    insidePos = 0  # points in the area above the x-axis
    insideNeg = 0  # points in the area below the x-axis

    for i in range(pts):
        # generate a random (x, y) coordinate
        x = np.random.uniform(lim1, lim2)
        y = np.random.uniform(min(ys), max(ys))
        funcVal = func(x)
        if funcVal >= 0 and y <= funcVal and y > 0:
            # points above the x axis
            insidePos += 1
        elif funcVal < 0 and y >= funcVal and y < 0:
            # points below the x axis
            insideNeg += 1

    totalArea = (lim2 - lim1) * abs(max(ys) - min(ys))
    posArea = (insidePos / pts) * totalArea
    negArea = (insideNeg / pts) * totalArea
    integral = posArea - negArea
    return integral

print(hitormiss(func, LIM1, LIM2, POINTS))