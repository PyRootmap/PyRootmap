# PyRootmap: A Python implementation of Diggle's (1988) Rootmap algorithm

National Autonomous University of Mexico (UNAM).

- Karime Ochoa Jacinto ([Kadkam8a](https://github.com/Kadkam8a))
- Arely Hilda Luis Tiburcio ([areelu](https://github.com/areelu))
- Anton Pashkov ([anton-pashkov](https://github.com/anton-pashkov))

The contents of this repository are licensed under the GNU General Public License version 3. Visit https://www.gnu.org/licenses/gpl-3.0.html for more information.

## Introduction

This project consists of an implementation of the Rootmap root growth model displayed in Diggle's (1988) paper, in order to output a graphical visualization of a plant root, whose shape and size will rely on the imposed initial conditions.

This project was arranged to facilitate future research efforts which require some sort of plant root modeling, such as the simulation of ancient or extreme environments to infer the potential anatomical structure of plant roots.

## Objectives

- Implement the root growth model which allows the inputting of different initial conditions.
- Create a set of graphical visualizations of the root model from the imposed initial conditions.

## Methodology
### How does the model works?
This model proposed by Diggle (1988), mantains a representation of the roots updated in time steps for an imposed duration, using a recursive routine that traces the entire tree in each time step and creates records as a binary tree of branch and root tip records. This composed as follows:
- **Branch records**: Contain the location of the branch in three dimensional coordinates, the age of the branch and the length of root between that branch and the preceding one.
- **Root tip records**: Contains the location of the root tip, the length of root between the tip and the last branch, and direction in which that tip grew in the last time step.

The locations in space of the branches and root tips are controlled by 2 parameters in addition to the tip growth rate. These parameters are the **deflection index**, which controls the tendency of the root tips to deflect from the direction in which they grew in the last time step, and the **geotropism index** , which controls the tendency for the deflections to occur preferentially downward. Both of these indices are numbers in the range 0 to 100. 
A deflection index of 0 results in no deflection from the past heading of that tip, a value of 100 results in a random deflection. Reciprocally, geotropism index of 0 results in no bias toward downward growth and an index of 100 causes all deflections to be in the direction that is nearest to straight down.

In each time step a direction of growth is calculated for each root tip from the past direction of growth for that tip, and the deflection and geotropism indices according to the following equations:

<img src='https://raw.githubusercontent.com/PyRootmap/PyRootmap/main/img/1.png'>
<img src='https://raw.githubusercontent.com/PyRootmap/PyRootmap/main/img/2.png'>

Where:
- $(x, y, z)$ are the cartesian coordinates of a vector of unit length oriented in the past direction of growth.
- $(x', y', z')$ are the the coordinates representing the new direction of growth.
- $\phi$ is the angle of deflection of the new direction from the old one.
- $\theta$ is te angle of orientation of the deflection relative to the deflection which would be most nearly straight down.
- $D$ is the deflection index.
- $G$ is the geotropism index.
- $R$ is a random number in the range $(0,1)$.
- $\alpha=\, arcos\, z$
- $\beta=\,arctan\frac{y}{x}$
The new location of the tip is calculated from the previous location of the tip, the direction of growth, and the growth rate as follows:
<img src='https://raw.githubusercontent.com/PyRootmap/PyRootmap/main/img/3.png'>
Where:

- (X Y Z) are the coordinates of the previous tip location.
- (X' Y' Z') are the coordinates of the new tip location.
- W is the growth rate.
- T is the tome step.



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
