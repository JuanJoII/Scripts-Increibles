import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the curve to be revolved (e.g., a parabola y = x^2 from x=0 to x=1)
def original_curve(x):
    return x**2  # Change this to whatever curve you want to revolve

# Create the plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Parameters
theta = np.linspace(0, 2*np.pi, 50)  # Rotation angles
x = np.linspace(0, 1, 20)            # x-coordinates of original curve
y = original_curve(x)                 # y-coordinates of original curve

# Create the surface by revolving around x-axis
X = np.outer(np.ones_like(theta), x)
Y = np.outer(np.cos(theta), y)
Z = np.outer(np.sin(theta), y)

# Plot the surface
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.8)

# Add original curve for reference
ax.plot(x, y, np.zeros_like(x), 'r-', linewidth=3, label='Original Curve')

# Set labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Surface of Revolution')
ax.legend()

plt.tight_layout()
plt.show()