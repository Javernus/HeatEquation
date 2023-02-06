from differentiate import *

def f(x, y):
    return np.sin(2 * np.pi * x) * np.sin(2 * np.pi * y)

def fRaised(x, y):
    return np.sin(2 * np.pi * x) * np.sin(2 * np.pi * y) + 0.25

def g(x, y):
    # If x or y is between 0.4 and 0.6, return 2, else return 0
    return np.where((x > 0.4) & (x < 0.6) & (y > 0.4) & (y < 0.6), 2, 0)

def zero(x, y):
    return 0


def one(x, y):
    return 1


def halfSine(x, y):
    return np.sin(np.pi * x) * np.sin(np.pi * y)


# If x + y is under 0.666, return -1, if under 1.333 return 0, else return 1
def steps(x, y):
    return np.where(x + y < 0.666, -1, np.where(x + y < 1.333, 0, 1))


def random(x, y):
    return np.random.uniform(-1, 1, x.shape)

def main():
    plotHeatEquation('random', random, 0, False, timestamps=[0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
    plotHeatEquation('steps', steps, 0, False)
    plotHeatEquation('halfSineCooled', halfSine, 0, True)
    plotHeatEquation('heatPillar', g, 0, True)
    plotHeatEquation('heatPillarNoCooling', g, 0, False)
    plotHeatEquation('sineQuads', f, 0, False)
    plotHeatEquation('sineQuadsCooled', f, 0, True)
    plotHeatEquation('sineQuadsRaised', fRaised, 0.25, False)
    plotHeatEquation('zeroHeated', zero, 1, True)
    plotHeatEquation('oneCooled', one, 0, True)


if __name__ == '__main__':
    main()
