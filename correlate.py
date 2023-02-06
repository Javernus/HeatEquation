from imports import *
from grid import setBoundaryConditions


class Correlate:
  def __init__(self, Z, TimeSteps, BoundaryFixed, BoundaryValue, diffusionConstant):
    self.Z = Z
    self.TimeSteps = TimeSteps
    self.BoundaryFixed = BoundaryFixed
    self.BoundaryValue = BoundaryValue

    # 2D convolution filter (Five point stencil)
    self.filter = np.array([
      [ 0,                  diffusionConstant,          0                 ],
      [ diffusionConstant,  1 - 4 * diffusionConstant,  diffusionConstant ],
      [ 0,                  diffusionConstant,          0                 ]
      ])

  def correlate(self):
    for k in range(0, self.TimeSteps-1):
      self.Z[:, :, k+1] = signal.convolve2d(self.Z[:, :, k], self.filter, boundary="symm", mode="same")

      if self.BoundaryFixed:
        setBoundaryConditions(self.Z[:, :, k+1], self.BoundaryValue)

    return self.Z
