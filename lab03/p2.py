import numpy as np
import matplotlib.pyplot as plt

# Definimos las cargas como una lista de tuplas, donde cada tupla representa una carga.
# Cada tupla tiene tres elementos: (posición_x, posición_y, magnitud_de_la_carga)
cargas = [(-2, 0, -10), (2, 0, 10)]

# Definimos las posiciones del campo en el plano XY
pos_x1, pos_y1 = -5, -5
pos_x2, pos_y2 = 5, 5

# Definimos la resolución del campo (cuántos puntos en cada dirección)
lres = 10
m, n = lres * (pos_y2 - pos_y1), lres * (pos_x2 - pos_x1)

# Creamos una cuadrícula de puntos en el plano XY
x, y = np.linspace(pos_x1, pos_x2, n), np.linspace(pos_y1, pos_y2, m)
x, y = np.meshgrid(x, y)

# Inicializamos los componentes del campo eléctrico (Ex y Ey) como matrices de ceros
Ex = np.zeros((m, n))
Ey = np.zeros((m, n))

# Constante de Coulomb
k = 9 * 10**9

# El campo electrico
E = 0

# Calculamos el campo eléctrico en cada punto de la cuadrícula
for i in range(m):
    for j in range(n):
        xp, yp = x[i][j], y[i][j]
        for q in cargas:
            # Calculamos la distancia entre el punto de la cuadrícula y la carga
            deltaX = xp - q[0]
            deltaY = yp - q[1]
            d = (deltaX**2 + deltaY**2)**0.5
            
            # Calculamos la magnitud del campo eléctrico en este punto debido a esta carga
            E = (k * q[2]) / (d**2)
            
            # Componentes del campo eléctrico en dirección X e Y
            Ex[i][j] += E * (deltaX / d)
            Ey[i][j] += E * (deltaY / d)

# Creamos la figura y los ejes para la visualización
fig, ax = plt.subplots()
ax.set_aspect('equal')

# Graficamos las cargas como puntos rojos, donde el tamaño refleja la magnitud de la carga
ax.scatter([q[0] for q in cargas], [q[1] for q in cargas], c='red', s=[abs(q[2])*25 for q in cargas], zorder=1)

# Agregamos etiquetas a las cargas para indicar su magnitud
for q in cargas:
    ax.text(q[0]+0.1, q[1]-0.3, '{} unidades'.format(q[2]), color='black', zorder=2)

# Graficamos las líneas de campo eléctrico
# El grosor de las lineas va a depender de la magnitud del campo electrico
ax.streamplot(x, y, Ex, Ey, linewidth=E/k*7/2, density=1.5, zorder=0)

# Añadimos título a la visualización
plt.title('Simulación de las lineas del Campo Eléctrico')
plt.show()