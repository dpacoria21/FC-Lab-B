import math

def isPositive(x):
    if x>=0:
        return True
    else:
        return False

def isGreaterThanZero(x):
    if x>0:
        return True
    else:
        return False

def isPossibleToGet(b, a, c):
    if (b*b) - (4*a*c) < 0 :
        return [False, -1]
    else:
        return [True, (-b+math.sqrt(b*b - 4*a*c))/(2*a)]

isContinue = True
while(isContinue):

    print("Que variable del MRUV desea hallar?")
    variable = input("1. Vf (en m/s)\n2. ∆t (en segundos)\n3. Vi (en m/s)\n4. a (en m/s^2)\nIngrese una opción: ");

    # assert(5<2);

    if variable == "1":
        v = float(input("Ingrese Vi: "))
        t = float(input("Ingrese ∆t: "))
        a = float(input("Ingrese a: "))

        if isPositive(t):
            print(f"El resultado de ∆x es: {v+a*t} m/s")
        else:
            print("No existe el tiempo negativo")

    elif variable == "2":
        vf = float(input("Ingrese Vf: ")) 
        vi = float(input("Ingrese Vi: "))
        a = float(input("Ingrese a: "))

        if a!=0:
            t = (vf - vi)/a
            if t >= 0:
                print(f"El resultado de ∆t es: {(vf-vi)/a} s")
            else:
                print(f"No existe el tiempo negativo")
        else:   
            print("No existe la división entre 0")
            
    elif variable == "3":
        vf = float(input("Ingrese Vf: "))
        t = float(input("Ingrese ∆t: "))
        a = float(input("Ingrese a: "))
        if t>=0:
            print(f"La velocidad inicial es: {vf - a*t} m/s")
        else:
            print("No existe tiempo negativo")

    elif variable == "4":
        vf = float(input("Ingrese Vf: "))
        vi = float(input("Ingrese Vi: "))
        t = float(input("Ingrese ∆t: "))
        if isGreaterThanZero(t):
            print(f"La aceleración es: {(vf-vi)/t} m/s^2")
        else:
            print("No existe el tiempo negativo y la division no puede ser entre 0")
    else:
        print("Elija una opción válida")
        continue
    value = input(f"Desea obtener otro valor? (Yes=y) (No=n): ")
    if value=="n" or value=="No" or value=="no" or value=="NO":
        print("Gracias por usar el programa!!!")
        isContinue = False

