import numpy as np


# Funcion polinomica de raiz simple. f(x) = x^3 - x - 2
def funcion_polinomica(x):
    resultado = np.power(x, 3) - x - 2
    return resultado


# Funcion polinomica de raiz doble. f(x) = (x - 2)^2
def funcion_raiz_doble(x):
    resultado = np.power(x - 2, 2)
    return resultado



# Funcion logaritmica f(x) = ln(x) + x - 4
def funcion_logaritmica(x):

    if x <= 0:
        raise ValueError("El valor de x debe ser mayor que 0.")

    resultado = np.log(x) + x - 4

    return resultado


if __name__ == "__main__":

    a = 1
    b = 2

    fa = funcion_polinomica(a)
    fb = funcion_polinomica(b)
    
    # PRueba funcion polinomica de raiz simple.
    print("Funcion: f(x) = x^3 - x - 2")
    print("f(1) =", fa)
    print("f(2) =", fb)

    if fa * fb < 0:
        print("Existe cambio de signo en el intervalo.")
    else:
        print("No existe cambio de signo en el intervalo.")

    
    
    # Prueba de la funcion con raiz doble.
    print("\nFuncion: f(x) = (x - 2)^2")

    x1 = 1
    x2 = 2
    x3 = 3

    print("f(1) =", funcion_raiz_doble(x1))
    print("f(2) =", funcion_raiz_doble(x2))
    print("f(3) =", funcion_raiz_doble(x3))

    if funcion_raiz_doble(x2) == 0:
        print("La funcion tiene una raiz en x = 2")

    if funcion_raiz_doble(x1) * funcion_raiz_doble(x3) < 0:
        print("Existe cambio de signo.")
    else:
        print("No existe cambio de signo.")

    
    # Prueba de la funcion logaritmica.
    print("\nFuncion: f(x) = ln(x) + x - 4")

    a = 2
    b = 3

    fa = funcion_logaritmica(a)
    fb = funcion_logaritmica(b)

    print("f(2) =", round(fa, 6))
    print("f(3) =", round(fb, 6))

    if fa * fb < 0:
        print("Existe cambio de signo en el intervalo.")
    else:
        print("No existe cambio de signo en el intervalo.")
