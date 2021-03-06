#!/usr/bin/env python3
#    A Python implementation of Diggle's (1988) Rootmap algorithm
#
#    Title     Rootmap: a root growth model
#    Author    A. J. Diggle
#    Journal   Mathematics and Computers in Simulation
#    Volume    30
#    Number    1
#    Pages     175-180
#    Year      1988
#    ISSN      0378-4754
#    DOI       https://doi.org/10.1016/0378-4754(88)90121-8
#
#    Copyright (C) 2022  Karime Ochoa Jacinto
#                        Arely Hilda Luis Tiburcio
#                        Anton Pashkov
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# W índice de crecimiento
# T saltos de tiempo
# D índice de flexión
# G índice de gravitopismo

def growth_function(old_x_pos, old_y_pos, old_z_pos, x_dir, y_dir, z_dir, W, T, D, G):
    new_dir = root_map(x_dir, y_dir, z_dir, D, G)
    new_pos = np.array([[old_x_pos],
                     [old_y_pos],
                     [old_z_pos]]) + W * T * new_dir
    return pd.Series({'pos': new_pos, 'dir': new_dir})

def root_map(x, y, z, D, G):
    if x == 0:
        x = 0.00001
    alpha = np.radians(np.arccos(np.radians(z)))
    beta = np.radians(np.arctan(np.radians(y / x)))
    R = np.random.random()
    while R == 0:
        R = np.random.random()
    phi = np.radians((200 * np.pi * np.exp(np.log(R / 2))) / D)
    theta = np.radians(100 * np.pi * np.exp(np.log(R)) / (G - 100))
    a1 = np.array([np.cos(alpha) * np.cos(beta), -y * np.sin(alpha) - z * np.cos(alpha) * np.sin(beta), x])
    a2 = np.array([np.cos(alpha) * np.sin(beta), x * np.sin(alpha) + z * np.cos(alpha) * np.cos(beta), y])
    a3 = np.array([-np.sin(alpha), x * np.cos(alpha) * np.sin(beta) - y * np.cos(alpha) * np.cos(beta), z])
    a = np.array([a1, a2, a3])
    b1 = np.sin(phi) * np.cos(theta)
    b2 = np.sin(phi) * np.sin(theta)
    b3 = np.cos(phi)
    b = np.array([[b1], [b2], [b3]])
    return np.dot(a, b)


points = np.empty(shape=(300, 3, 1))
directions = np.empty(shape=(300, 3, 1))
t_x, t_y, t_z = 0, 0, 0
x_dir, y_dir, z_dir = 0, 0, 0
W, T, D, G = 1, 1, 30, 65
directions[0] = np.array([[x_dir], [y_dir], [z_dir]])
points[0] = np.array([[t_x], [t_y], [t_z]])

fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
ax = fig.add_subplot(111)

# Crear raíz primaria
for i in range(1, len(points)):
    result = growth_function(t_x, t_y, t_z, x_dir, y_dir, z_dir, W, T, D, G)
    t_x, t_y, t_z = result.pos
    t_x, t_y, t_z = t_x[0], t_y[0], t_z[0]
    x_dir, y_dir, z_dir = result.dir
    x_dir, y_dir, z_dir = x_dir[0], y_dir[0], z_dir[0]
    points[i] = np.array([[t_x], [t_y], [t_z]])
    directions[i] = np.array([[x_dir], [y_dir], [z_dir]])

x = points[:, 0, 0]
y = points[:, 1, 0]
z = points[:, 2, 0]
# ax.plot3D(x, y, z, c='red')
ax.plot(y, x, c='red')

W, D, G = 0.3, 30, 0

# Crear raices secundarias
for j in range(1, len(points)):
    points_2 = np.empty(shape=(len(points)-j, 3, 1))
    directions_2 = np.empty(shape=(len(points)-j, 3, 1))
    t_x, t_y, t_z = points[j]
    x_dir, y_dir, z_dir = directions[j]
    t_x, t_y, t_z = t_x[0], t_y[0], t_z[0]
    x_dir, y_dir, z_dir = (np.random.random() * x_dir[0],
                          np.random.random() * y_dir[0],
                          np.random.random() * z_dir[0])
    directions_2[0] = np.array([[x_dir], [y_dir], [z_dir]])
    points_2[0] = np.array([[t_x], [t_y], [t_z]])
    for i in range(1, len(points_2)):
        result = growth_function(t_x, t_y, t_z, x_dir, y_dir, z_dir, W, T, D, G)
        t_x, t_y, t_z = result.pos
        t_x, t_y, t_z = t_x[0], t_y[0], t_z[0]
        x_dir, y_dir, z_dir = result.dir
        x_dir, y_dir, z_dir = x_dir[0], y_dir[0], z_dir[0]
        points_2[i] = np.array([[t_x], [t_y], [t_z]])
        directions_2[i] = np.array([[x_dir], [y_dir], [z_dir]])

    x = points_2[:, 0, 0]
    y = points_2[:, 1, 0]
    z = points_2[:, 2, 0]
    # ax.plot3D(x, y, z, c='grey')
    ax.plot(y, x, c='grey')

limits = ax.get_ylim()
lim = abs(limits[1] - limits[0])/2
ax.set_xlim(-lim, lim)

ax.invert_yaxis()
plt.grid()
plt.show()
