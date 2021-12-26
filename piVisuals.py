#! /usr/bin/python3.9

import numpy as np
import matplotlib.pyplot as plt
import time


RADIUS = 5
POINTS = 100_000
POINTS_IGNORE = 2000
POINTS_STEP = 400
AVERAGE_OVER = 5


def drawCircleSquare(rad):
    # badly draw a square
    plt.plot([-rad, -rad, rad, rad, -rad], [-rad, rad, rad, -rad, -rad], c="red")

    # inefficiently draw a circle
    angles = np.linspace(0, 2*np.pi, 150)
    xs = rad*np.cos(angles)
    ys = rad*np.sin(angles)
    plt.plot(xs, ys, c="b")

def drawPoints(rad, pts):
    xin = []
    yin = []
    xout = []
    yout = []

    for i in range(pts):
        # generate a random x, y coordinate
        x = np.random.uniform(-rad, rad)
        y = np.random.uniform(-rad, rad)
        if x**2 + y**2 <= rad**2:
            xin.append(x)
            yin.append(y)
        else:
            xout.append(x)
            yout.append(y)

    plt.scatter(xin, yin, s=8, c="cyan")
    plt.scatter(xout, yout, s=8, c="brown")

def findPi(rad, pts):
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

def monteVsActual(rad, pts, step, ptsIgnore = 1, avgOver = None, avg = False):
    pis = []
    ptsRange = list(range(ptsIgnore, pts, step))
    tic = time.time()

    if avg == False:
        for i in ptsRange:
            pis.append(findPi(rad, i))
    else:
        for i in ptsRange:
            pi = 0
            for j in range(avgOver):
                pi += findPi(rad, i)
            pis.append(pi / avgOver)

    toc = time.time()
    print(f"Time taken = {round(toc - tic, 3)}s")
    plt.xlabel("Number of points")
    plt.ylabel("Value of pi")
    plt.plot(ptsRange, np.ones_like(pis)*np.pi)
    plt.plot(ptsRange, pis)


drawCircleSquare(RADIUS)
drawPoints(RADIUS, POINTS)
# monteVsActual(RADIUS, POINTS, POINTS_STEP, POINTS_IGNORE, AVERAGE_OVER, avg=False)
plt.show()
