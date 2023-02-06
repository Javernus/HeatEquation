from imports import *


def getGrid(XYResolution, TimeSteps, f, BoundaryValue):
  x = np.linspace(0, 1, XYResolution, endpoint=True)
  y = np.linspace(0, 1, XYResolution, endpoint=True)
  X, Y = np.meshgrid(x, y)
  Z = np.zeros((XYResolution, XYResolution, TimeSteps))
  Z[:, :, 0] = f(X, Y)
  setBoundaryConditions(Z[:, :, 0], BoundaryValue)
  dx = x[1] - x[0]

  return X, Y, Z, dx


def setBoundaryConditions(Z, boundaryValue):
  Z[0, :] = boundaryValue
  Z[-1, :] = boundaryValue
  Z[:, 0] = boundaryValue
  Z[:, -1] = boundaryValue

  return Z
