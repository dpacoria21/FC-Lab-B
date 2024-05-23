# !pip install magpylib==2.3.0b0  TODO: usar  esto en google colab

# Antes de correr el codigo usar TODO: pip install magpylib==2.3.0b0
import numpy as np
import matplotlib.pyplot as plt

from magpylib.source.magnet import Box, Cylinder
from magpylib import Collection, displaySystem

#Crea las figuras
caja = Box(mag=(0, 0, 600), dim=(3,3,3), pos=(-4,0,3))
cilindro = Cylinder(mag=(0, 0, 500), dim=(3, 5))

#Se agrupan ambos imanes en una colección para tratarlos conjuntamente.
collect = Collection(caja, cilindro)

caja.rotate(45, (0,1,0), anchor=(0,0,0))
cilindro.move((5,0,-4))

collect.move((-2,0,0))

posx = np.linspace(-10,10,33)
posz = np.linspace(-10, 10, 44)
POS = np.array([(x,0,z) for z in posz for x in posx])
calculateB = collect.getB(POS).reshape(44,33,3)

fig = plt.figure(figsize=(9,5))

#un gráfico 3D que muestra la disposición de los imanes
plane3D = fig.add_subplot(121, projection='3d')
#un gráfico 2D que muestra las líneas de flujo del campo magnético en el plano
plane2D = fig.add_subplot(122)

displaySystem(collect, subplotAx=plane3D, suppress=True)

X,Z = np.meshgrid(posx, posz)
U,V = calculateB[:,:,0], calculateB[:,:,2]

#dibuja las líneas de flujo del campo magnético, coloreadas según la magnitud del campo magnético en cada punto
plane2D.streamplot(X,Z,U,V, color=np.log(U**2+V**2))
plt.show()