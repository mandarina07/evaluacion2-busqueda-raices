import numpy as np

# Metodo de biseccion ---------------------------------------------------------------

def biseccion(f, a, b, tol=1e-6, max_iter=100):

    fa = f(a)
    fb = f(b)
    errores = []
    historial = []

    # Verificamos si un extremo ya es una raiz
    if fa == 0:
        return {
            "raiz": a,
            "iteraciones": 0,
            "errores": errores,
            "historial": historial,
            "convergencia": True
        }

    if fb == 0:
        return {
            "raiz": b,
            "iteraciones": 0,
            "errores": errores,
            "historial": historial,
            "convergencia": True
        }

    # Para biseccion debe existir cambio de signo
    if fa * fb > 0:
        return {
            "raiz": None,
            "iteraciones": 0,
            "errores": errores,
            "historial": historial,
            "convergencia": False
        }

    xm_anterior = None

    for i in range(1, max_iter + 1):

        xm = (a + b) / 2
        fxm = f(xm)

        # Calculamos el error entre aproximaciones
        if xm_anterior is None:
            error = (b - a) / 2
        else:
            error = abs(xm - xm_anterior)

        errores.append(error)
        historial.append(xm)

        # Comprobamos el criterio de parada
        if error < tol or fxm == 0:
            return {
                "raiz": xm,
                "iteraciones": i,
                "errores": errores,
                "historial": historial,
                "convergencia": True
            }

        # Actualizamos el intervalo
        if fa * fxm < 0:
            b = xm
            fb = fxm
        else:
            a = xm
            fa = fxm

        xm_anterior = xm

    return {
        "raiz": xm,
        "iteraciones": max_iter,
        "errores": errores,
        "historial": historial,
        "convergencia": False
    }



# Metodo de falsa posicion ---------------------------------------------------------------------
def falsa_posicion(f, a, b, tol=1e-6, max_iter=100):

    fa = f(a)
    fb = f(b)

    errores = []
    historial = []

    # Comprobamos si alguno de los extremos es una raiz
    if fa == 0:
        return {
            "raiz": a,
            "iteraciones": 0,
            "errores": errores,
            "historial": historial,
            "convergencia": True
        }

    if fb == 0:
        return {
            "raiz": b,
            "iteraciones": 0,
            "errores": errores,
            "historial": historial,
            "convergencia": True
        }

    # Verificamos que exista un cambio de signo
    if fa * fb > 0:
        return {
            "raiz": None,
            "iteraciones": 0,
            "errores": errores,
            "historial": historial,
            "convergencia": False
        }

    # Guardamos la aproximacion anterior
    xr_anterior = None

    # Iniciamos el proceso iterativo
    for i in range(1, max_iter + 1):

        # Aplicamos la formula de falsa posicion
        xr = (a * fb - b * fa) / (fb - fa)
        fxr = f(xr)

        # Calculamos el error entre aproximaciones
        if xr_anterior is None:
            error = abs(b - a)
        else:
            error = abs(xr - xr_anterior)

        errores.append(error)
        historial.append(xr)

        # Comprobamos el criterio de parada
        if error < tol or fxr == 0:
            return {
                "raiz": xr,
                "iteraciones": i,
                "errores": errores,
                "historial": historial,
                "convergencia": True
            }

        # Actualizamos el intervalo segun el cambio de signo
        if fa * fxr < 0:
            b = xr
            fb = fxr
        else:
            a = xr
            fa = fxr

        # Guardamos la aproximacion actual
        xr_anterior = xr

    # Si se alcanza el maximo de iteraciones
    return {
        "raiz": xr,
        "iteraciones": max_iter,
        "errores": errores,
        "historial": historial,
        "convergencia": False
    }



# Metodo de la secante ------------------------------------------------------------------------
def secante(f, x0, x1, tol=1e-6, max_iter=100):
    errores = []
    historial = []

    for i in range(1, max_iter + 1):

        fx0 = f(x0)
        fx1 = f(x1)

        # Comprobamos si la aproximacion actual ya es raiz
        if abs(fx1) < tol:
            return {
                "raiz": x1,
                "iteraciones": i - 1,
                "errores": errores,
                "historial": historial,
                "convergencia": True
            }

        denominador = fx1 - fx0

        # Evitamos la division por cero
        if denominador == 0:
            return {
                "raiz": x1,
                "iteraciones": i - 1,
                "errores": errores,
                "historial": historial,
                "convergencia": False
            }

        # Aplicamos la formula de la secante
        x2 = x1 - fx1 * (x1 - x0) / denominador

        # Calculamos el error entre aproximaciones
        error = abs(x2 - x1)

        historial.append(x2)
        errores.append(error)

        # Comprobamos el criterio de parada
        if error < tol or f(x2) == 0:
            return {
                "raiz": x2,
                "iteraciones": i,
                "errores": errores,
                "historial": historial,
                "convergencia": True
            }

        # Actualizamos las aproximaciones
        x0 = x1
        x1 = x2

    # Si se alcanza el maximo de iteraciones
    return {
        "raiz": x2,
        "iteraciones": max_iter,
        "errores": errores,
        "historial": historial,
        "convergencia": False
    }



# Metodo punto fijo ---------------------------------------------------------------------
def punto_fijo(g, x0, tol=1e-6, max_iter=100):

    errores = []
    historial = []

    for i in range(1, max_iter + 1):

        x1 = g(x0)

        error = abs(x1 - x0)
        historial.append(x1)
        errores.append(error)

        # Verificamos el criterio de parada
        if error < tol:
            return {
                "raiz": x1,
                "iteraciones": i,
                "errores": errores,
                "historial": historial,
                "convergencia": True
            }

        x0 = x1

    return {
        "raiz": x1,
        "iteraciones": max_iter,
        "errores": errores,
        "historial": historial,
        "convergencia": False
    }


# Metodo Newton-raphson ---------------------------------------------------------------------
def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    errores = []
    historial = []

    for i in range(1, max_iter + 1):
        fx = f(x0)
        dfx = df(x0)

        # Si ya encontramos una raíz aproximada
        if abs(fx) < tol:
            return {
                "raiz": x0,
                "iteraciones": i - 1,
                "errores": errores,
                "historial": historial,
                "convergencia": True
            }

        # Evitar división por cero
        if dfx == 0:
            return {
                "raiz": x0,
                "iteraciones": i - 1,
                "errores": errores,
                "historial": historial,
                "convergencia": False
            }

        # Fórmula de Newton-Raphson
        x1 = x0 - fx / dfx

        # Error entre aproximaciones consecutivas
        error = abs(x1 - x0)

        historial.append(x1)
        errores.append(error)

        # Comprobar convergencia
        if error < tol and abs(f(x1)) < tol:
            return {
                "raiz": x1,
                "iteraciones": i,
                "errores": errores,
                "historial": historial,
                "convergencia": True
            }

        x0 = x1

    return {
        "raiz": x0,
        "iteraciones": max_iter,
        "errores": errores,
        "historial": historial,
        "convergencia": False
    }


# Metodo Newton-raphson Modificado ---------------------------------------------------------------------
def newton_raphson_mejorado(f, df, d2f, x0, tol=1e-6, max_iter=100):
    errores = []
    historial = []

    for i in range(1, max_iter + 1):
        fx = f(x0)
        dfx = df(x0)
        d2fx = d2f(x0)

        # Comprobar si ya encontramos una raíz aproximada
        if abs(fx) < tol:
            return {
                "raiz": x0,
                "iteraciones": i - 1,
                "errores": errores,
                "historial": historial,
                "convergencia": True
            }

        # Calcular el denominador de la fórmula
        denominador = dfx**2 - fx * d2fx

        # Evitar división por cero
        if abs(denominador) < 1e-14:
            return {
                "raiz": x0,
                "iteraciones": i - 1,
                "errores": errores,
                "historial": historial,
                "convergencia": False
            }

        # Fórmula de Newton-Raphson mejorado
        x1 = x0 - (fx * dfx) / denominador

        # Error entre aproximaciones consecutivas
        error = abs(x1 - x0)

        historial.append(x1)
        errores.append(error)

        # Comprobar convergencia
        if error < tol and abs(f(x1)) < tol:
            return {
                "raiz": x1,
                "iteraciones": i,
                "errores": errores,
                "historial": historial,
                "convergencia": True
            }

        x0 = x1

    return {
        "raiz": x0,
        "iteraciones": max_iter,
        "errores": errores,
        "historial": historial,
        "convergencia": False
    }
