m1 = float(input("Ingrese la masa de m1 (en kg): "))
m2 = float(input("Ingrese la masa de m2 (en kg): "))

g = 0
while g<=0: #gravedades disponibles >9.7 y <=10
    print("Por favor, ingrese una gravedad valida")
    g = float(input("Ingrese la gravedad con la que desea trabajar: "))


if m1>0 and m2>0:
    if m1>m2:

        a = ((m1-m2)*g)/(m1+m2)
        t = m2*(a+g)

        print(f"La aceleración (a) es: {a} m/s^2\nLa tensión (T) en la cuerda sin peso es: {t}N")

    elif m1<m2:
        a = ((m2-m1)*g)/(m1+m2)
        t = m1*(a+g)

        print(f"La aceleración (a) es: {a} m/s^2\nLa tensión (T) en la cuerda sin peso es: {t}N")
    else:

        a = 0
        t = m1*g
        print(f"La aceleración (a) es: {a} m/s^2\nLa tensión (T) en la cuerda sin peso es: {t}N")

else:
    print("Los valores ingresados son inválidos")