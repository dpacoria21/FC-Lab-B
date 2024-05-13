import numpy as np
import matplotlib.pyplot as plt


def calculate_electric_camp (q1, r):
    k = 9*(10**-9)
    return (k*q1)/(r)

def calculate_electric_force (q1, q2, r):
    k = 9*(10**-9)
    return (k*q1*q2)/(r)

def matplot_graph(x, y, xlabel, ylabel, title):
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.show()

is_continuous = True
while(is_continuous):

    option = input("1. Calcular campo electrico\n2. Calcular fuerza electrica\nIngrese una opcion: ")

    if option == "1":
        q1 = float(input("Ingrese la carga de q1: "))
        r = float(input("Ingrese la distancia entre las cargas: "))
        
        if r>0:
            tnp = np.linspace(1, r**2, 100)
            matplot_graph(tnp, calculate_electric_camp(q1, tnp), "r^2", "E", "Campo electrico")
        else:
            print("Ingrese datos invalidos (r no puede ser 0)")

    elif option == "2":
        q1 = float(input("Ingrese la carga de q1: "))
        q2 = float(input("Ingrese la carga de q2: "))
        r = float(input("Ingrese la distancia entre las cargas: "))

        if r>0:
            tnp = np.linspace(1, r**2, 100)
            matplot_graph(tnp, calculate_electric_force(q1, q2, tnp), "r^2", "F", "Fuerza electrica")
        else:
            print("Ingrese datos invalidos (r no puede ser 0)")
            
    value = input(f"Desea obtener otro valor? (Yes=y) (No=n): ")
    if value=="n" or value=="No" or value=="no" or value=="NO":
        print("Gracias por usar el programa!!!")
        is_continuous = False

