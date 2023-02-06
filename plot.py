from imports import *

class Plot:
  def __init__(self, X, Y, Z, TimeSteps, boundary=None, pretty=True, save=False):
    self.X = X
    self.Y = Y
    self.Z = Z
    self.TimeSteps = TimeSteps
    self.pretty = pretty
    self.save = save
    self.boundary = boundary

    self.fig = plt.figure(figsize=(16, 9))
    self.ax = self.fig.add_subplot(projection='3d')


  def getFig(self):
    return self.fig


  def setPretty(self, pretty):
    self.pretty = pretty


  def setSave(self, save):
    self.save = save


  def plot(self, time, name=None):
    self.ax.clear()
    self.ax.set_xlim(0, 1)
    self.ax.set_ylim(0, 1)
    self.ax.set_zlim(-1, 1)

    self.ax.set_xlabel('x')
    self.ax.set_ylabel('y')
    self.ax.set_zlabel('z')

    # Plot two grey lines behind the plot to indicate the boundaries
    if self.boundary is not None:
      self.ax.plot([0, 0], [0, 1], [self.boundary, self.boundary], color='grey', linewidth=1)
      self.ax.plot([0, 1], [1, 1], [self.boundary, self.boundary], color='grey', linewidth=1)

    # Make the surface not have checkerboard pattern
    self.ax.plot_surface(self.X, self.Y, self.Z[:, :, time], cmap=cm.seismic, vmin=-1, vmax=1, linewidth=0, antialiased=True, shade=True, rstride=1, cstride=1)

    # Plot two grey lines in front of the plot to indicate the boundaries
    self.ax.plot([0, 1], [0, 0], [self.boundary, self.boundary], color='grey', linewidth=0.65, zorder=10)
    self.ax.plot([1, 1], [0, 1], [self.boundary, self.boundary], color='grey', linewidth=0.65, zorder=10)

    if self.pretty:
      # Don't show self.axes, ticks, etc. just the plot
      self.ax.axis('off')
      padding = 0
    else:
      # self.ax.set_title('Heat Diffusion')
      padding = 0.05

    if self.save:
      plt.savefig(name, bbox_inches='tight', pad_inches=padding, dpi=200)
