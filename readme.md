# Heat Equation 2D

This repository contains code to solve the Heat Equation numerically and does so in two dimensions.

## How to run

To run the code, you need to have Python, Numpy and Scipy installed. You can then run the code by running the following command in the terminal:

```bash
python3 main.py
```

## How to use

The `config.py` file contains a handful of parameters that change the behaviour of the code. It is recommended to leave the `XYResolution` parameter on default. Tweaking this may cause unexpected behaviour. The time parameters can be safely altered.

In `main.py`, you can define your starting functions. These functions are used to calculate the initial temperature distribution. There are a handful of functions predefined.

Lastly, you have to define the program to run your function. This requires you to define the boundary condition and its behaviour. This can be done with two variables in the `plotHeatEquation` and `animateHeatEquation` functions. The `boundaryValue` variable is a function that takes a single argument, the temperature at the boundary. The `boundaryFixed` variable is a boolean that determines whether the boundary is fixed or not. If fixed, the boundary will be heated/cooled to the value of `boundaryValue`. If not fixed, the boundary value will only be set to the value of `boundaryValue` at the start of the simulation.
