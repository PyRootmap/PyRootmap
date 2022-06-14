# PyRootmap: A Python implementation of Diggle's (1988) Rootmap algorithm

National Autonomous University of Mexico (UNAM).

- Karime Ochoa Jacinto ([Kadkam8a](https://github.com/Kadkam8a))
- Arely Hilda Luis Tiburcio ([areelu](https://github.com/areelu))
- Anton Pashkov ([anton-pashkov](https://github.com/anton-pashkov))

The contents of this repository are licensed under the GNU General Public License version 3. Visit https://www.gnu.org/licenses/gpl-3.0.html for more information.

## Introduction

This project consists of an implementation of the Rootmap root growth model displayed in Diggle's (1988) paper, in order to output a graphical visualization of a plant root, whose shape and size will rely on the imposed initial conditions.

This project was arranged to facilitate future research efforts which require some sort of plant root modeling, such as the simulation of ancient or extreme environments to infer the potential anatomical structure of plant roots.

Plants are composed of two basic parts: the **shoot system** (above ground) and the **root system** (usually below ground). Roots provide anatomical support for plants, and absorb water and minerals. As the shoot system grows and develops, the amount of nutrients and support required by the plant increases. To fulfill both requirements, roots must grow over the course of a plant's life in order to have a larger absorption area from which to get the resources. The entire process of growth of any given root happens in the root's **tip**, which has an extension of approximately one centimeter. The root tip can divided into three parts, which, starting from the root's end and going inwards, are the following:

1. Area of **cell division**: It is the area where new cells are created and are initially small in size.
2. Area of **elongation**: Here, the cells increase in size, thereby lengthening the root.
3. Area of **maturation**: This is the last part of the tip, and it's where the "full-sized" cells specialize in order to carry out different functions.

<img src="https://openstax.org/apps/archive/20220509.174553/resources/6dabd05289996e847856c2fa43247194ba786e17">

Image taken from Clark et al. (2020).

When a seed germinates, it initiates the first root, known as the **primary root**. After reaching a certain length, the primary root produces branches known as **secondary roots**. A similar branching process happens with these secondary roots, creating the **tertiary roots**. A plant can theoretically produce roots of any branching order, though it often stops in the third level. The general configuration of roots differs from plant type to plant type. In this project, we simulate the growth of fibrous roots up to the second order (i.e. it creates primary and secondary roots).

## Objectives

- Implement the root growth model which allows the inputting of different initial conditions.
- Create a graphical visualization of the root model from the imposed initial conditions.

## Methodology

### Mathematical Background

This model proposed by Diggle (1988), mantains a representation of the roots updated in time steps for an imposed duration, using a recursive routine that traces the entire tree in each time step and creates records as a binary tree of branch and root tip records. This composed as follows:
- **Branch records**: Contain the location of the branch in three dimensional coordinates, the age of the branch and the length of root between that branch and the preceding one.
- **Root tip records**: Contains the location of the root tip, the length of root between the tip and the last branch, and direction in which that tip grew in the last time step.

The locations in space of the branches and root tips are controlled by 2 parameters in addition to the tip growth rate. These parameters are the **deflection index**, which controls the tendency of the root tips to deflect from the direction in which they grew in the last time step, and the **geotropism index** , which controls the tendency for the deflections to occur preferentially downward. Both of these indices are numbers in the range 0 to 100. 
A deflection index of 0 results in no deflection from the past heading of that tip, a value of 100 results in a random deflection. Reciprocally, geotropism index of 0 results in no bias toward downward growth and an index of 100 causes all deflections to be in the direction that is nearest to straight down.

In each time step a direction of growth is calculated for each root tip from the past direction of growth for that tip, and the deflection and geotropism indices according to the following equations:

<img src='https://github.com/PyRootmap/PyRootmap/blob/main/img/form1.png'>

Where:

- $(x, y, z)$ are the cartesian coordinates of a vector of unit length oriented in the past direction of growth.
- $(x', y', z')$ are the the coordinates representing the new direction of growth.
- $\phi$ is the angle of deflection of the new direction from the old one.
- $\theta$ is te angle of orientation of the deflection relative to the deflection which would be most nearly straight down.
- $D$ is the deflection index.
- $G$ is the geotropism index.
- $R$ is a random number in the range $(0,1)$.
- $\alpha=\arccos z$
- $\beta=\arctan\frac{y}{x}$
The new location of the tip is calculated from the previous location of the tip, the direction of growth, and the growth rate as follows:

<img src='https://github.com/PyRootmap/PyRootmap/blob/main/img/form2.png'>

Where:

- (X Y Z) are the coordinates of the previous tip location.
- (X' Y' Z') are the coordinates of the new tip location.
- W is the growth rate.
- T is the tome step.

### Computational Implementation

To create the simulation, our team followed these steps:

1. Import the necessary libraries (numpy, matplotlib, and pandas).
2. Implement the growth function which, given the previous coordinates, the growth rate, and the time step, returns the new location of the root tip.
3. Create the rootmap function that calculates the new direction of growth, given the previous direction of growth and the deflection and geotropism indices.
4. Generate a graphical visualization of the primary root.
5. On each node of the primary root, append a secondary root, whose initial conditions depend on the state of the respective node.

For the implementation of this project, two functions were created:

- `growth_function`: Receives the initial coordinates and growth direction, growth rate, time step, deflection index and gravitropism index. It returns the new location of the root tip.

- `root_map`. Calculates the new growth direction, given the previous growth direction and the deviation and geotropism rates.

We use the following libraries:

- **Numpy** to perform all necesarry mathematical computations.

- **Pandas**. To create a series of Pandas from a dictionary.

- **Matplotlib**. To create the graphical representation of the root.

## Results

<img src='https://github.com/PyRootmap/PyRootmap/blob/main/img/root_v3.png'>

This image is produced from the following initial conditions:

- Primary root (drawn in red):
	- Growth rate: 2.
	- Time step: 4/60.
	- Deflection index: 30.
	- Geotropism index: 65.
	- Initial direction and coordinates set to 0.
- Secondary roots (drawn in grey):
	- Growth rate: 0.4.
	- Time step: 4/60.
	- Deflection index: 30.
	- Geotropism index: 0.
	- Initial direction and coordinates set to primary root condition.

The thin red line is the primary root, whereas the grey lines are the secondary roots.

## Conclusions

The indices of gravitropism and deflection are essential in the final shape and size of a root. As such, it is possible to apply this model within environments we can't access (such as the ones from other geological eras or other planets) and predict the spatial distribution of these roots. However, an important thing to consider is that this model only produces fibrous root systems; to simulate other types of roots (such as the ones produced by trees), other kinds of models are required.

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

- Clark, M. A., et al. (2020). Plant Form and Physiology. In *Biology* (2nd Edition, pp. 829-870). OpenStax. Retrieved from: https://openstax.org/details/books/biology-2e
- Diggle, A. J. (1988). Rootmap: a root growth model. *Mathematics and Computers in Simulation*, 30(1), 175-180. DOI: [10.1016/0378-4754(88)90121-8](https://doi.org/10.1016/0378-4754(88)90121-8)
