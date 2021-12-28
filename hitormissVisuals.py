#! /usr/bin/python3.9

import numpy as np
import matplotlib.pyplot as plt
import pretty_errors
import time

POINTS = 5000
LIM1, LIM2 = -2, 3
STEP = 500
TRUE_VALUE = 1.5783
POINTS_IGNORE = 10_000
AVERAGE_OVER = 5

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

def drawFunc(func, lim1, lim2):
    xs = np.linspace(lim1, lim2, 300)
    ys = func(xs)
    plt.plot(xs, ys, c="black")

def drawPoints(func, lim1, lim2, pts):
    xs = np.linspace(lim1, lim2, 300)
    ys = func(xs)
    xinPos, xoutPos = [], []
    xinNeg, xoutNeg = [], []
    yinPos, youtPos = [], []
    yinNeg, youtNeg = [], []

    for i in range(pts):
        x = np.random.uniform(lim1, lim2)
        y = np.random.uniform(min(ys), max(ys))
        funcVal = func(x)
        if funcVal > 0 and y <= funcVal and y > 0:
            xinPos.append(x)
            yinPos.append(y)
        elif funcVal < 0 and y >= funcVal and y < 0:
            xinNeg.append(x)
            yinNeg.append(y)
        elif funcVal > 0:
            xoutPos.append(x)
            youtPos.append(y)
        else:
            xoutNeg.append(x)
            youtNeg.append(y)

    size = 6
    plt.scatter(xinPos, yinPos, c="orange", s=size)
    plt.scatter(xinNeg, yinNeg, c="cyan", s=size)
    plt.scatter(xoutNeg + xoutPos, youtNeg + youtPos, c="black", s = 1)

def monteVsActual(func, lim1, lim2, pts, step, trueVal, ptsIgnore=1, avgOver=False):
    integrals = []
    ptsRange = list(range(ptsIgnore, pts, step))
    tic = time.time()

    if not avgOver:
        for i in ptsRange:
            integrals.append(hitormiss(func, lim1, lim2, i))
    else:
        for i in ptsRange:
            integral = 0
            for j in range(avgOver):
                integral += hitormiss(func, lim1, lim2, i)
            integrals.append(integral / avgOver)

    toc = time.time()
    print(f"Time taken = {round(toc - tic, 3)}s")
    plt.xlabel("Number or points")
    plt.ylabel("Value of integral")
    plt.plot(ptsRange, np.ones_like(ptsRange)*trueVal)
    plt.plot(ptsRange, integrals)


# print(hitormiss(func, LIM1, LIM2, POINTS))
drawFunc(func, -2, 3)
drawPoints(func, -2, 3, POINTS)
# monteVsActual(func, LIM1, LIM2, POINTS, STEP, TRUE_VALUE)
plt.show()