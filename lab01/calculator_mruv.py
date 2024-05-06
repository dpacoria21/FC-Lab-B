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
    variable = input("1. ∆x (en metros)\n2. ∆t (en segundos)\n3. Vi (en m/s)\n4. a (en m/s^2)\nIngrese una opción: ");

    # assert(5<2);

    if variable == "1":
        v = float(input("Ingrese Vi: "))
        t = float(input("Ingrese ∆t: "))
        a = float(input("Ingrese a: "))

        if isPositive(t):
            print(f"El resultado de ∆x es: {v*t + (a*t*t)/2} m")
        else:
            print("No existe el tiempo negativo")

    elif variable == "2":
        v = float(input("Ingrese Vi: ")) 
        x = float(input("Ingrese ∆x: "))
        a = float(input("Ingrese a: "))

        res = isPossibleToGet(2*v, a, -2*x)
        if res[0]:
            if isPositive(res[1]):
                print(f"El  resultado de ∆t es: {res[1]} s")
            else:
                print(f"El tiempo no puede ser negativo")
        else:
            print("No existe una respuesta en los reales")
            
    elif variable == "3":
        x = float(input("Ingrese ∆x: "))
        t = float(input("Ingrese ∆t: "))
        a = float(input("Ingrese a: "))
        if isGreaterThanZero(t):
            print(f"La velocidad inicial es: {(x/t) - (a*t)/2} m/s")
        else:
            print("No existe tiempo negativo y la division no puede ser entre 0")

    elif variable == "4":
        v = float(input("Ingrese Vi: "))
        x = float(input("Ingrese ∆x: "))
        t = float(input("Ingrese ∆t: "))
        if isGreaterThanZero(t):
            print(f"La aceleración es: {2*(x-v*t)/(t*t)} m/s^2")
        else:
            print("No existe el tiempo negativo y la division no puede ser entre 0")
    else:
        print("Elija una opción válida")
        continue
    value = input(f"Desea obtener otro valor? (Yes=y) (No=n): ")
    if value=="n" or value=="No" or value=="no" or value=="NO":
        print("Gracias por usar el programa!!!")
        isContinue = False

