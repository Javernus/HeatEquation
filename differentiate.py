from imports import *
from grid import getGrid
from correlate import Correlate
from plot import Plot
from config import getConfig

# Get the configuration
XYResolution, TimeSteps, dt, pretty = getConfig()


def getPlot(initialValuesFunction, boundaryValue, boundaryFixed, pretty=True, save=True):
    X, Y, Z, dx = getGrid(XYResolution, TimeSteps, initialValuesFunction, boundaryValue)

    # Diffusion constant
    a = 1.172E-5 * dt / dx ** 2

    # Fill the grid with the values of the heat equation over time
    Z = Correlate(Z, TimeSteps, boundaryFixed, boundaryValue, a).correlate()

    # Create the images and gifs folders if they doesn't exist
    if not os.path.exists('images'):
        os.makedirs('images')
    if not os.path.exists('gifs'):
        os.makedirs('gifs')

    return Plot(X, Y, Z, TimeSteps, boundary=boundaryValue, pretty=pretty, save=save)


def animateHeatEquation(fileName, initialValuesFunction, boundaryValue, boundaryFixed, show=False):
    plot = getPlot(initialValuesFunction, boundaryValue, boundaryFixed, pretty=pretty, save=False)

    # Animate the heat equation
    animation = FuncAnimation(plot.getFig(), plot.plot, frames=TimeSteps, interval=60)

    # Either show the animation or save it
    if show:
        plt.show()
    else:
        animation.save(f'gifs/{fileName}-animation.gif', fps=60, writer='ffmpeg')


def plotHeatEquation(fileName, initialValuesFunction, boundaryValue, boundaryFixed, timestamps=None):
    plot = getPlot(initialValuesFunction, boundaryValue, boundaryFixed, pretty=pretty)

    if timestamps is None:
        timestamps = np.linspace(0, TimeSteps - 1, 5, dtype=int)

    for timestamp in timestamps:
        plot.plot(timestamp, f'images/{fileName}-{timestamp}.png')
