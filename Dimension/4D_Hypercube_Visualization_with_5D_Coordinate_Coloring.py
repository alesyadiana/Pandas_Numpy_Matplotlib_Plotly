import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.text import Annotation

# Define tesseract vertices
vertices = np.array([
    [-1, -1, -1, -1, -1],
    [-1, -1, -1, -1, 1],
    [-1, -1, -1, 1, -1],
    [-1, -1, -1, 1, 1],
    [-1, -1, 1, -1, -1],
    [-1, -1, 1, -1, 1],
    [-1, -1, 1, 1, -1],
    [-1, -1, 1, 1, 1],
    [-1, 1, -1, -1, -1],
    [-1, 1, -1, -1, 1],
    [-1, 1, -1, 1, -1],
    [-1, 1, -1, 1, 1],
    [-1, 1, 1, -1, -1],
    [-1, 1, 1, -1, 1],
    [-1, 1, 1, 1, -1],
    [-1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]  # Second dimension vertex
])


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
    ax.plot3D(*zip(vertices[edge[0]], vertices[edge[1]]), color='gray', linestyle='dashed', linewidth=1)

# Define rotation matrix
angle = np.pi / 4
rotation_matrix = np.array([[np.cos(angle), 0, -np.sin(angle), 0, 0],
                            [0, np.cos(angle), 0, -np.sin(angle), 0],
                            [np.sin(angle), 0, np.cos(angle), 0, 0],
                            [0, np.sin(angle), 0, np.cos(angle), 0],
                            [0, 0, 0, 0, 1]])

# Project vertices onto 3D space
projected_vertices = np.dot(vertices, rotation_matrix[:, :3])

# Plot projected vertices with labels
labels = [''.join(str(v) for v in vertex) for vertex in vertices]
sc = ax.scatter(projected_vertices[:, 0], projected_vertices[:, 1], projected_vertices[:, 2],
                s=100, c=vertices[:, 4], cmap='cool', alpha=0.9)
for i, label in enumerate(labels):
    annotation = Annotation(label, xy=(projected_vertices[i, 0], projected_vertices[i, 1]),
                            xytext=(3, 3), textcoords='offset points', fontsize=8,
                            ha='center', va='center')
    ax.add_artist(annotation)

# Create illusion lines connecting projected vertices
for i in range(len(projected_vertices)):
    for j in range(i+1, len(projected_vertices)):
        ax.plot([projected_vertices[i, 0], projected_vertices[j, 0]],
                [projected_vertices[i, 1], projected_vertices[j, 1]],
                [projected_vertices[i, 2], projected_vertices[j, 2]], 'k--', alpha=0.3)

# Add a color bar
cbar = fig.colorbar(sc, ax=ax, shrink=0.8)
cbar.set_label('Fifth Dimension')

# Function to update plot when rotating with mouse
def on_mouse_move(event):
    ax.view_init(elev=event.ydata, azim=event.xdata)

# Connect the mouse movement to the plot update function
fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)

# Display the plot
plt.show()
