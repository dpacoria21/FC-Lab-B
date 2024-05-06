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

isContinue = True
while(isContinue):

    print("Que variable del MRU desea hallar?")
    variable = int(input("1. ∆x (en metros)\n2. ∆t (en segundos)\n3. v (en m/s)\nIngrese una opción: "));

    # assert(5<2);

    if variable == 1:
        v = float(input("Ingrese v: "));
        t = float(input("Ingrese ∆t: "));

        if isPositive(t):
            print(f"El resultado de ∆x es: {v*t} m")
        else:
            print("No existe el tiempo negativo")

    elif variable == 2:
        v = float(input("Ingrese v: "));
        x = float(input("Ingrese ∆x: "));
        if isGreaterThanZero(v):
            print(f"El resultado de ∆x es: {x/v} s")
        else:
            print("No se puede hacer la division entre 0")
            
    elif variable == 3:
        x = float(input("Ingrese ∆x: "));
        t = float(input("Ingrese ∆t: "));
        if isGreaterThanZero(t):
            print(f"El resultado de v es: {x/t} m/s")
        else:
            print("No existe tiempo negativo o la division no puede ser entre 0")
            
    else:
        print("Elija una opción válida")
    value = input(f"Desea obtener otro valor? (Yes=y) (No=n): ")
    if value=="n":
        isContinue = False

