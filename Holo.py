import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Crear datos 3D para visualizar
theta = np.linspace(0, 2*np.pi, 100)
z = np.linspace(0, 1, 100)
r = z**2 + 1

x = r * np.cos(theta)
y = r * np.sin(theta)

# Crear la figura y los ejes 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujar el objeto 3D giratorio
ax.plot(x, y, z)

# Mostrar el holograma
plt.show()
