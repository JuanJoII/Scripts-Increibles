import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def original_curve(x):
    return x**2  


fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

theta = np.linspace(0, 2*np.pi, 50)  
x = np.linspace(0, 1, 20)           
y = original_curve(x)                

X = np.outer(np.ones_like(theta), x)
Y = np.outer(np.cos(theta), y)
Z = np.outer(np.sin(theta), y)

ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.8)

ax.plot(x, y, np.zeros_like(x), 'r-', linewidth=3, label='Original Curve')

# Set labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Surface of Revolution')
ax.legend()

plt.tight_layout()
plt.show()