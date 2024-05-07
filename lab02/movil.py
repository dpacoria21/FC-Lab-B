import matplotlib.pyplot as plt

def calcular_fuerza(m, vi, vf, t):
    # formula para hallar la aceleracion con la vi, vf y t
    return m * (vf - vi) / t

def graficar_proceso(t, fuerza):
    plt.plot(t, fuerza)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Fuerza (N)')
    plt.title('Fuerza durante el cambio de velocidad')
    plt.grid(True)
    plt.show()

def main():

    isContinue = True
    while(isContinue):

        #Distancia no es necesaria para este calculo
        m = float(input("Ingrese la masa del móvil (kg): "))
        vi = float(input("Ingrese la velocidad inicial (m/s): "))
        vf = float(input("Ingrese la velocidad final (m/s): "))
        t = float(input("Ingrese el tiempo tomado (s): "))
        
        f = calcular_fuerza(m, vi, vf, t)
        print(f"La fuerza que experimenta el móvil es: {f} N")
        
        # Crear un arreglo de tiempo para graficar
        t_x = [0, t]
        f_y = [0, f]
        
        graficar_proceso(t_x, f_y)

        value = input(f"¿Desea usar otra vez el programa? (Yes=y) (No=n): ")
        if value=="n" or value=="No" or value=="no" or value=="NO":
            print("Gracias por usar el programa!!!")
            isContinue = False

main()