#! /usr/bin/python3.9

import numpy as np
import matplotlib.pyplot as plt

POINTS = 1_000_000
MASS = 1  # kg
SIDE = 5  # m

def monteMoment(pts, mass, side):
    dm = mass / pts  # the mass of each infinitesimal cube element
    ixx = 0
    ixy = 0

    for i in range(pts):
        x = np.random.uniform(0, side)
        y = np.random.uniform(0, side)
        z = np.random.uniform(0, side)
        ixx += dm*(y**2 + z**2)
        ixy -= dm*x*y

    return (ixx, ixy)

ixx, ixy = monteMoment(POINTS, MASS, SIDE)
ixxt = 2*MASS*(SIDE**2) / 3  # theoretical value
ixyt = -MASS*(SIDE**2) / 4  # theoretical value
print(f"Ixx = {round(ixx, 4)} kg*m^2  Ixxt = {round(ixxt, 4)} kg*m^2")
print(f"Ixy = {round(ixy, 4)} kg*m^2  Ixyt = {round(ixyt, 4)} kg*m^2")