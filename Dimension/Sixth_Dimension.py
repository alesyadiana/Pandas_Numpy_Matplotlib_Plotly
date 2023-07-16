import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define tesseract vertices with the sixth dimension
vertices = np.array([[-1, -1, -1, -1, -1, -1],
                     [-1, -1, -1, -1, -1,  1],
                     [-1, -1, -1, -1,  1, -1],
                     [-1, -1, -1, -1,  1,  1],
                     [-1, -1, -1,  1, -1, -1],
                     [-1, -1, -1,  1, -1,  1],
                     [-1, -1, -1,  1,  1, -1],
                     [-1, -1, -1,  1,  1,  1],
                     [-1,  1, -1, -1, -1, -1],
                     [-1,  1, -1, -1, -1,  1],
                     [-1,  1, -1, -1,  1, -1],
                     [-1,  1, -1, -1,  1,  1],
                     [-1,  1,  1, -1, -1, -1],
                     [-1,  1,  1, -1, -1,  1],
                     [-1,  1,  1, -1,  1, -1],
                     [-1,  1,  1, -1,  1,  1],
                     [ 1, -1, -1, -1, -1, -1],
                     [ 1, -1, -1, -1, -1,  1],
                     [ 1, -1, -1, -1,  1, -1],
                     [ 1, -1, -1, -1,  1,  1],
                     [ 1, -1,  1, -1, -1, -1],
                     [ 1, -1,  1, -1, -1,  1],
                     [ 1, -1,  1, -1,  1, -1],
                     [ 1, -1,  1, -1,  1,  1],
                     [ 1,  1, -1, -1, -1, -1],
                     [ 1,  1, -1, -1, -1,  1],
                     [ 1,  1, -1, -1,  1, -1],
                     [ 1,  1, -1, -1,  1,  1],
                     [ 1,  1,  1, -1, -1, -1],
                     [ 1,  1,  1, -1, -1,  1],
                     [ 1,  1,  1, -1,  1, -1],
                     [ 1,  1,  1, -1,  1,  1]])

# Define edges of the tesseract
edges = [(0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 3), (2, 6), (3, 7),
         (4, 5), (4, 6), (5, 7), (6, 7), (8, 9), (8, 10), (8, 12), (9, 11),
         (9, 13), (10, 11), (10, 14), (11, 15), (12, 13), (12, 14), (13, 15),
         (14, 15), (0, 8), (1, 9), (2, 10), (3, 11), (4, 12), (5, 13), (6, 14),
         (7, 15)]

# Create a figure and axis
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_aspect('auto')
ax.axis('off')

# Plot the tesseract edges
for edge in edges:
    ax.plot3D(*zip(vertices[edge[0]][:3], vertices[edge[1]][:3]), color='black')

# Define rotation matrix for the first three dimensions
angle = np.pi / 4
rotation_matrix_3d = np.array([[np.cos(angle), 0, -np.sin(angle)],
                               [0, np.cos(angle), 0],
                               [np.sin(angle), 0, np.cos(angle)]])

# Project vertices onto 3D space
projected_vertices_3d = np.dot(vertices[:, :3], rotation_matrix_3d)

# Define rotation matrix for the fourth, fifth, and sixth dimensions
rotation_matrix_456 = np.array([[1, 0, 0],
                                [0, np.cos(angle), -np.sin(angle)],
                                [0, np.sin(angle), np.cos(angle)]])

# Project vertices from 3D space to the fourth, fifth, and sixth dimensions
projected_vertices_456 = np.dot(projected_vertices_3d, rotation_matrix_456)

# Plot projected vertices with labels
labels = [''.join(str(v) for v in vertex) for vertex in vertices]
sc = ax.scatter(projected_vertices_3d[:, 0], projected_vertices_3d[:, 1], projected_vertices_3d[:, 2],
                s=100, c=projected_vertices_456[:, 2], cmap='viridis')
for i, label in enumerate(labels):
    ax.text(projected_vertices_3d[i, 0], projected_vertices_3d[i, 1], projected_vertices_3d[i, 2],
            label, fontsize=8, ha='center', va='center')

# Create illusion lines connecting projected vertices in 3D space
for i in range(len(projected_vertices_3d)):
    for j in range(i+1, len(projected_vertices_3d)):
        ax.plot([projected_vertices_3d[i, 0], projected_vertices_3d[j, 0]],
                [projected_vertices_3d[i, 1], projected_vertices_3d[j, 1]],
                [projected_vertices_3d[i, 2], projected_vertices_3d[j, 2]], 'k--', alpha=0.3)

# Add a color bar for the sixth dimension
cbar = fig.colorbar(sc, ax=ax, shrink=0.8)
cbar.set_label('Sixth Dimension')

# Display the plot
plt.show()
