import numpy as np

# Funcion polinomica de raiz simple. f(x) = x^3 - x - 2 -------------------------------------------
def funcion_polinomica(x):
    return np.power(x, 3) - x - 2

def derivada_polinomica(x):
    return 3 * (x ** 2) - 1



# Funcion polinomica de raiz doble. f(x) = (x - 2)^2 -------------------------------------------
def funcion_raiz_doble(x):
    return np.power(x - 2, 2)

def derivada_raiz_doble(x):
    return 2 * x - 4



# Funcion logaritmica. f(x) = ln(x) + x - 4 ---------------------------------------------------
def funcion_logaritmica(x):
    if x <= 0:
        raise ValueError("El valor de x debe ser mayor que 0.")
    return np.log(x) + x - 4

def derivada_logaritmica(x):
    if x == 0:
        raise ValueError("El valor de x debe ser distinto que 0.")
    return (1 / x) + 1



# Funcion exponencial. f(x) = e^(−x) − x ------------------------------------------------------
def funcion_exponencial(x):
    return np.exp(-x) - x

def derivada_exponencial(x):
    return (- np.exp(-x)) - 1



# Funcion trigonométrica. f(x) = cos(x) − x -----------------------------------------
def funcion_trigonometrica(x):
    return np.cos(x) - x

def derivada_trigonometrica(x):
    return - np.sin(x) - 1



# Funcion mixta f(x). = √x − cos(x) -----------------------------------
def funcion_mixta(x):
    return np.sqrt(x) - np.cos(x)

def derivada_mixta(x):
    return 1 / (2* np.sqrt(x)) + np.sin(x)


if __name__ == "__main__":

    a = 1
    b = 2

    fa = funcion_polinomica(a)
    fb = funcion_polinomica(b)

    # Prueba funcion polinomica de raiz simple.
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



    # Prueba de la funcion exponencial.
    print("\nFuncion: f(x) = e^(-x) - x")

    a = 0
    b = 1

    fa = funcion_exponencial(a)
    fb = funcion_exponencial(b)

    print("f(0) =", fa)
    print("f(1) =", fb)

    if fa * fb < 0:
        print("Existe cambio de signo en el intervalo.")
    else:
        print("No existe cambio de signo en el intervalo.")


    # Prueba de la funcion trigonometrica.
    print("\nFuncion: f(x) = cos(x) - x")

    a = 0
    b = 1

    fa = funcion_trigonometrica(a)
    fb = funcion_trigonometrica(b)

    print("f(0) =", fa)
    print("f(1) =", fb)

    if fa * fb < 0:
        print("Existe cambio de signo en el intervalo.")
    else:
        print("No existe cambio de signo en el intervalo.")


    # Prueba de la funcion mixta.
    print("\nFuncion: f(x) = sqrt(x) - cos(x)")

    a = 0
    b = 1

    fa = funcion_mixta(a)
    fb = funcion_mixta(b)

    print("f(0) =", fa)
    print("f(1) =", fb)

    if fa * fb < 0:
        print("Existe cambio de signo en el intervalo.")
    else:
        print("No existe cambio de signo en el intervalo.")