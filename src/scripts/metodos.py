import numpy as np

# Metodo de biseccion
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

    for i in range(1, max_iter + 1):

        xm = (a + b) / 2

        fxm = f(xm)

        error = abs(fxm)

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

        # Si hay cambio de signo entre a y xm,
        # conservamos la mitad izquierda
        if fa * fxm < 0:
            b = xm
            fb = fxm
        else:
            a = xm
            fa = fxm

    # Si se alcanza el maximo de iteraciones
    return {
        "raiz": xm,
        "iteraciones": max_iter,
        "errores": errores,
        "historial": historial,
        "convergencia": False
    }


# Metodo de falsa posicion
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

    if fa * fb > 0:
        return {
            "raiz": None,
            "iteraciones": 0,
            "errores": errores,
            "historial": historial,
            "convergencia": False
        }

    # Iniciamos el proceso iterativo
    for i in range(1, max_iter + 1):

        # Aplicamos la formula de falsa posicion
        xr = (a * fb - b * fa) / (fb - fa)

        fxr = f(xr)

        error = abs(fxr)

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

        # Si existe cambio de signo en el lado izquierdo,
        # actualizamos el extremo derecho
        if fa * fxr < 0:
            b = xr
            fb = fxr

        # En caso contrario actualizamos el izquierdo
        else:
            a = xr
            fa = fxr

    return {
        "raiz": xr,
        "iteraciones": max_iter,
        "errores": errores,
        "historial": historial,
        "convergencia": False
    }



# Metodo de la secante
def secante(f, x0, x1, tol=1e-6, max_iter=100):

    errores = []
    historial = []

    for i in range(1, max_iter + 1):

        fx0 = f(x0)
        fx1 = f(x1)

        if abs(fx1) < tol:
            return {
                "raiz": x1,
                "iteraciones": i - 1,
                "errores": errores,
                "historial": historial,
                "convergencia": True
            }

        denominador = fx1 - fx0

        if denominador == 0:
            return {
                "raiz": x1,
                "iteraciones": i - 1,
                "errores": errores,
                "historial": historial,
                "convergencia": False
            }

        x2 = x1 - fx1 * (x1 - x0) / denominador

        error = abs(f(x2))

        historial.append(x2)
        errores.append(error)

        # Verificamos el criterio de parada
        if error < tol:
            return {
                "raiz": x2,
                "iteraciones": i,
                "errores": errores,
                "historial": historial,
                "convergencia": True
            }

        x0 = x1
        x1 = x2

    return {
        "raiz": x2,
        "iteraciones": max_iter,
        "errores": errores,
        "historial": historial,
        "convergencia": False
    }



if __name__ == "__main__":

    from funciones import funcion_polinomica
    
    from funciones import funcion_raiz_doble

    # Ejecutamos biseccion
    resultado = biseccion(
        funcion_polinomica,
        1,
        2,
        1e-6,
        100
    )

    print("METODO DE BISECCION")
    print("Raiz aproximada:", resultado["raiz"])
    print("Iteraciones:", resultado["iteraciones"])
    print("Convergencia:", resultado["convergencia"])

    print("\nHISTORIAL DE ITERACIONES")

    for i in range(len(resultado["historial"])):
        print(
            "Iteracion:", i + 1,
            "Raiz:", resultado["historial"][i],
            "Error:", resultado["errores"][i]
        )


    # Prueba del metodo de falsa posicion
    print("\nMETODO DE FALSA POSICION")

    resultado = falsa_posicion(
        funcion_polinomica,
        1,
        2,
        1e-6,
        100
    )

    print("Raiz aproximada:", resultado["raiz"])
    print("Iteraciones:", resultado["iteraciones"])
    print("Convergencia:", resultado["convergencia"])

    # Mostramos las aproximaciones.
    print("\nHISTORIAL DE ITERACIONES")

    for i in range(len(resultado["historial"])):
        print(
            "Iteracion:", i + 1,
            "Raiz:", resultado["historial"][i],
            "Error:", resultado["errores"][i]
        )


    # Ejecutamos el metodo de la secante
    resultado = secante(
        funcion_polinomica,
        1,
        2,
        1e-6,
        100
    )

    print("METODO DE LA SECANTE")
    print("Raiz:", resultado["raiz"])
    print("Iteraciones:", resultado["iteraciones"])
    print("Convergencia:", resultado["convergencia"])

    print("\nHISTORIAL DE ITERACIONES")

    for i in range(len(resultado["historial"])):
        print(
            "Iteracion:", i + 1,
            "Raiz:", resultado["historial"][i],
            "Error:", resultado["errores"][i]
        )
        
        