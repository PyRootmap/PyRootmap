# PyRootmap: A Python implementation of Diggle's (1988) Rootmap algorithm

National Autonomous University of Mexico (UNAM).

- Karime Ochoa Jacinto ([Kadkam8a](https://github.com/Kadkam8a))
- Arely Hilda Luis Tiburcio ([areelu](https://github.com/areelu))
- Anton Pashkov ([anton-pashkov](https://github.com/anton-pashkov))

The contents of this repository are licensed under the GNU General Public License version 3. Visit https://www.gnu.org/licenses/gpl-3.0.html for more information.

## Introduction

This project consists of an implementation of the Rootmap root growth model displayed in Diggle's (1988) paper, in order to output a graphical visualization of a plant root, whose shape and size will rely on the imposed initial conditions. In this model, each new direction of growth is defined by the past direction of growth, and the deflection and geotropism indices, based on the following equations:

<div markdown = '1' style = 'margin-left: 20%; margin-right: 20%'>

<img src='https://raw.githubusercontent.com/PyRootmap/PyRootmap/main/img/form1.png'>

</div>

Each new triple of coordinates is calculated from the previous coordinates, growth rate, time step and the direction of growth:

<div markdown = '1' style = 'margin-left: 35%; margin-right: 35%'>

<img src='https://raw.githubusercontent.com/PyRootmap/PyRootmap/main/img/form2.png'>

</div>

This project was arranged to facilitate future research efforts which require some sort of plant root modeling, such as the simulation of ancient or extreme environments to infer the potential anatomical structure of plant roots.

## Objectives

- Implement the root growth model which allows the inputting of different initial conditions.
- Create a set of graphical visualizations of the root model from the imposed initial conditions.

## Methodology

To create the simulation, our team followed these steps:

1. Import the necessary libraries (numpy, matplotlib, and pandas).
2. Implement the growth function which, given the previous coordinates, the growth rate, and the time step, returns the new location of the root tip.
3. Create the rootmap function that calculates the new direction of growth, given the previous direction of growth and the deflection and geotropism indices.
4. Generate a graphical visualization of the primary root.
5. On each node of the primary root, append a secondary root, whose initial conditions depend on the state of the respective node.

## Results

<img src='https://raw.githubusercontent.com/PyRootmap/PyRootmap/main/img/root_v1.png'>

This image is produced by the following initial conditions:

- Primary root (drawn in red):
	- Growth rate: 2.
	- Time step: 4/60.
	- Deflection index: 30.
	- Geotropism index: 65.
- Secondary roots (drawn in grey):
	- Growth rate: 0.4.
	- Time step: 4/60.
	- Deflection index: 30.
	- Geotropism index: 0.

## Conclusions



## Execution requirements

Clone the repository to your device by running:

```text
git clone https://github.com/PyRootmap/PyRootmap/
```

This program requires [Python 3](https://www.python.org/) and has the following dependencies:

- [Numpy](https://numpy.org/).
- [Matplotlib](https://matplotlib.org/).
- [Pandas](https://pandas.pydata.org/).

Change to the directory where `PyRootmap.py` is located with `cd PyRootmap/`. The program can be run from the command line by typing:

```text
./PyRootmap.py
```

## References

- Diggle, A. J. (1988). Rootmap: a root growth model. *Mathematics and Computers in Simulation*, 30(1), 175-180. DOI: [10.1016/0378-4754(88)90121-8](https://doi.org/10.1016/0378-4754(88)90121-8)

