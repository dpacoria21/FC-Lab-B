# !pip install magpylib==2.3.0b0 ipywidgets

# en vscode poner en la terminal pip install magpylib==2.3.0b0 ipywidgets

import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

from magpylib.source.magnet import Box, Cylinder
from magpylib import Collection, displaySystem

# Función para actualizar la visualización basada en las posiciones ingresadas
def update_display(caja_x, caja_y, caja_z, cilindro_x, cilindro_y, cilindro_z):
    # Crear las figuras
    caja = Box(mag=(0, 0, 600), dim=(3, 3, 3), pos=(caja_x, caja_y, caja_z))
    cilindro = Cylinder(mag=(0, 0, 500), dim=(3, 5), pos=(cilindro_x, cilindro_y, cilindro_z))

    # Agrupar ambos imanes en una colección para tratarlos conjuntamente
    collect = Collection(caja, cilindro)

    # Rotar la caja
    caja.rotate(45, (0, 1, 0), anchor=(0, 0, 0))
    cilindro.move((5, 0, -4))

    # Mover la colección
    collect.move((-2, 0, 0))

    # Calcular el campo magnético
    posx = np.linspace(-10, 10, 33)
    posz = np.linspace(-10, 10, 44)
    POS = np.array([(x, 0, z) for z in posz for x in posx])
    calculateB = collect.getB(POS).reshape(44, 33, 3)

    fig = plt.figure(figsize=(12, 6))

    # Un gráfico 3D que muestra la disposición de los imanes
    plane3D = fig.add_subplot(121, projection='3d')
    # Un gráfico 2D que muestra las líneas de flujo del campo magnético en el plano
    plane2D = fig.add_subplot(122)

    # Ajustar los espacios entre los subplots
    plt.subplots_adjust(wspace=0.4, hspace=0.4)

    displaySystem(collect, subplotAx=plane3D, suppress=True)

    X, Z = np.meshgrid(posx, posz)
    U, V = calculateB[:, :, 0], calculateB[:, :, 2]

    # Dibujar las líneas de flujo del campo magnético, coloreadas según la magnitud del campo magnético en cada punto
    plane2D.streamplot(X, Z, U, V, color=np.log(U**2 + V**2))

    # Añadir texto con las posiciones del cubo y cilindro
    fig.text(0.5, 0.02, f'\n\nCube(x={caja_x:.1f}, y={caja_y:.1f}, z={caja_z:.1f}), Cylinder(x={cilindro_x:.1f}, y={cilindro_y:.1f}, z={cilindro_z:.1f})', ha='center', fontsize=12)

    plt.show()

# Crear widgets para la entrada de la posición de la caja y del cilindro
caja_x_widget = widgets.FloatSlider(min=-10, max=10, step=0.1, value=-4, description='Caja X:')
caja_y_widget = widgets.FloatSlider(min=-10, max=10, step=0.1, value=0, description='Caja Y:')
caja_z_widget = widgets.FloatSlider(min=-10, max=10, step=0.1, value=3, description='Caja Z:')
cilindro_x_widget = widgets.FloatSlider(min=-10, max=10, step=0.1, value=0, description='Cilindro X:')
cilindro_y_widget = widgets.FloatSlider(min=-10, max=10, step=0.1, value=0, description='Cilindro Y:')
cilindro_z_widget = widgets.FloatSlider(min=-10, max=10, step=0.1, value=0, description='Cilindro Z:')

# Botón para actualizar la visualización
update_button = widgets.Button(description="Actualizar Visualización")

# Función para manejar el evento de clic del botón
def on_update_button_clicked(b):
    update_display(caja_x_widget.value, caja_y_widget.value, caja_z_widget.value,
                   cilindro_x_widget.value, cilindro_y_widget.value, cilindro_z_widget.value)

update_button.on_click(on_update_button_clicked)

# Mostrar widgets
display(caja_x_widget, caja_y_widget, caja_z_widget, cilindro_x_widget, cilindro_y_widget, cilindro_z_widget, update_button)

# Mostrar visualización inicial
update_display(caja_x_widget.value, caja_y_widget.value, caja_z_widget.value,
               cilindro_x_widget.value, cilindro_y_widget.value, cilindro_z_widget.value)