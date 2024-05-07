# import math

# def isPositive(x):
#     if x>=0:
#         return True
#     else:
#         return False

# def isGreaterThanZero(x):
#     if x>0:
#         return True
#     else:
#         return False

# def isPossibleToGet(b, a, c):
#     if (b*b) - (4*a*c) < 0 :
#         return [False, -1]
#     else:
#         return [True, (-b+math.sqrt(b*b - 4*a*c))/(2*a)]

# isContinue = True
# while(isContinue):

#     # distancia no es necesaria para resolver este problema
#     m = float(input("Ingrese la masa del movil (en kg): "))
#     t = float(input("Ingrese el tiempo del movimiento (en s): "))
#     vi = float(input("Ingrese la velocidad inicial (en m/s): "))
#     vf = float(input("Ingrese la velocidad final (en m/s): "))

#     value = input(f"Desea obtener otro valor? (Yes=y) (No=n): ")
#     if value=="n" or value=="No" or value=="no" or value=="NO":
#         print("Gracias por usar el programa!!!")
#         isContinue = False

import matplotlib.pyplot as plt

def calcular_fuerza(m, vi, vf, t):
    return m * (vf - vi) / t

def graficar_proceso(t, fuerza):
    plt.plot(t, fuerza)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Fuerza (N)')
    plt.title('Fuerza durante el cambio de velocidad')
    plt.grid(True)
    plt.show()

def main():

    #Distancia no es necesaria para este calculo
    m = float(input("Ingrese la masa del móvil (kg): "))
    vi = float(input("Ingrese la velocidad inicial (m/s): "))
    vf = float(input("Ingrese la velocidad final (m/s): "))
    t = float(input("Ingrese el tiempo tomado (s): "))
    
    fuerza = calcular_fuerza(m, vi, vf, t)
    print("La fuerza que experimenta el móvil es:", fuerza, "N")
    
    # Crear un arreglo de tiempo para graficar
    tiempo_grafica = [0, t]
    fuerza_grafica = [0, fuerza]
    
    graficar_proceso(tiempo_grafica, fuerza_grafica)

main()