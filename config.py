from imports import *

# Grid resolution
XYResolution = 40
TimeSteps = 10000
dt = 1

# Pretty plots (no axis, no ticks, no grid)
pretty = False

def getConfig():
    return XYResolution, TimeSteps, dt, pretty
