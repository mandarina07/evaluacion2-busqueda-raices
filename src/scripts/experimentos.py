import csv
import numpy as np
from pathlib import Path

# Importamos los seis metodos numericos.
from metodos import (
    biseccion, falsa_posicion, secante, punto_fijo, newton_raphson,newton_raphson_mejorado
)
# Importamos las seis funciones, sus derivadas y las funciones g(x)
from funciones import (
    fun_polinomica, fun_raiz_doble, fun_logaritmica,
    fun_exponencial, fun_trigonometrica, fun_mixta,
    derivada_polinomica, derivada_raiz_doble, derivada_logaritmica,
    derivada_exponencial, derivada_trigonometrica, derivada_mixta,
    segunda_derivada_polinomica, segunda_derivada_raiz_doble, segunda_derivada_logaritmica,
    segunda_derivada_exponencial, segunda_derivada_trigonometrica, segunda_derivada_mixta,
    g_polinomica, g_raiz_doble, g_logaritmica,
    g_exponencial, g_trigonometrica, g_mixta
)


# Diccionario que contiene las funciones matematicas y
# los datos necesarios para ejecutar los seis metodos.
funciones = {
    "Polinomica": {
        "funcion": fun_polinomica,
        "derivada": derivada_polinomica,
        "segunda_derivada": segunda_derivada_polinomica,
        "g": g_polinomica,
        "a": 1,
        "b": 2,
        "x0": 1.5,
        "x1": 2
    },

    "Raiz doble": {
        "funcion": fun_raiz_doble,
        "derivada": derivada_raiz_doble,
        "segunda_derivada": segunda_derivada_raiz_doble,
        "g": g_raiz_doble,
        "a": 1,
        "b": 3,
        "x0": 1.2,
        "x1": 3
    },

    "Logaritmica": {
        "funcion": fun_logaritmica,
        "derivada": derivada_logaritmica,
        "segunda_derivada": segunda_derivada_logaritmica,
        "g": g_logaritmica,
        "a": 2,
        "b": 3,
        "x0": 2.5,
        "x1": 3
    },

    "Exponencial": {
        "funcion": fun_exponencial,
        "derivada": derivada_exponencial,
        "segunda_derivada": segunda_derivada_exponencial,
        "g": g_exponencial,
        "a": 0,
        "b": 1,
        "x0": 0.5,
        "x1": 1
    },

    "Trigonometrica": {
        "funcion": fun_trigonometrica,
        "derivada": derivada_trigonometrica,
        "segunda_derivada": segunda_derivada_trigonometrica,
        "g": g_trigonometrica,
        "a": 0,
        "b": 1,
        "x0": 0.5,
        "x1": 1
    },

    "Mixta": {
        "funcion": fun_mixta,
        "derivada": derivada_mixta,
        "segunda_derivada": segunda_derivada_mixta,
        "g": g_mixta,
        "a": 0.1,
        "b": 1,
        "x0": 0.5,
        "x1": 1
    }

}

def ejecutar_metodos(datos, tolerancia, max_iteraciones):

    # Obtenemos la funcion original.
    f = datos["funcion"]
    # Obtenemos la primera derivada.
    df = datos["derivada"]
    # Obtenemos la segunda derivada.
    d2f = datos["segunda_derivada"]
    # Obtenemos la transformacion para punto fijo.
    g = datos["g"]

    # Obtenemos los extremos del intervalo.
    a = datos["a"]
    b = datos["b"]

    # Obtenemos las estimaciones iniciales.
    x0 = datos["x0"]
    x1 = datos["x1"]

    # Diccionario para almacenar los resultados.
    resultados = {}

    # Metodo de biseccion.
    resultados["Biseccion"] = biseccion(
        f, a, b, tolerancia, max_iteraciones
    )

    # Metodo de falsa posicion.
    resultados["Falsa posicion"] = falsa_posicion(
        f, a, b, tolerancia, max_iteraciones
    )

    # Metodo de la secante.
    resultados["Secante"] = secante(
        f, x0, x1, tolerancia, max_iteraciones
    )

    # Metodo de punto fijo.
    resultados["Punto fijo"] = punto_fijo(
        g, x0, tolerancia, max_iteraciones
    )

    # Metodo de Newton-Raphson.
    resultados["Newton-Raphson"] = newton_raphson(
        f, df, x0, tolerancia, max_iteraciones
    )

    # Metodo de Newton-Raphson mejorado.
    resultados["Newton mejorado"] = newton_raphson_mejorado(
        f, df, d2f, x0, tolerancia, max_iteraciones
    )

    # Devolvemos los resultados de los seis metodos.
    return resultados


def guardar_resumen(resultados_generales):

    # Definimos la carpeta donde guardaremos los CSV.
    carpeta = Path(__file__).resolve().parent.parent / "data"

    # Creamos la carpeta si no existe.
    carpeta.mkdir(parents=True, exist_ok=True)

    # Definimos la ruta del archivo.
    ruta = carpeta / "resumen_convergencia.csv"

    # Abrimos el archivo CSV.
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:

        escritor = csv.writer(archivo)

        # Escribimos el encabezado.
        escritor.writerow([
            "Funcion",
            "Metodo",
            "Raiz",
            "Iteraciones",
            "Error_residual",
            "Convergencia"
        ])

        # Recorremos las seis funciones.
        for nombre, resultados in resultados_generales.items():

            # Obtenemos la funcion matematica correspondiente.
            f = funciones[nombre]["funcion"]

            # Recorremos los resultados de cada metodo.
            for metodo, resultado in resultados.items():

                # Obtenemos los datos del resultado.
                raiz = resultado["raiz"]
                iteraciones = resultado["iteraciones"]
                convergencia = resultado["convergencia"]

                # Calculamos el error residual si existe una raiz.
                if raiz is not None and np.isfinite(raiz):

                    error_residual = abs(f(raiz))

                else:

                    # Dejamos la celda vacia cuando no hay una
                    # aproximacion valida.
                    error_residual = ""

                    if raiz is not None:
                        raiz = ""

                # Guardamos una fila en el CSV.
                escritor.writerow([
                    nombre,
                    metodo,
                    raiz if raiz is not None else "",
                    iteraciones,
                    error_residual,
                    convergencia
                ])

    print("\nResumen guardado en:", ruta)


def guardar_datos_fun(nombre, funcion, a, b, cantidad=200):

    # Definimos la carpeta de los datos.
    carpeta = Path(__file__).resolve().parent.parent / "data"

    # Creamos la carpeta si no existe.
    carpeta.mkdir(parents=True, exist_ok=True)

    # Convertimos el nombre a un nombre de archivo.
    nombre_archivo = nombre.lower().replace(" ", "_") + ".csv"

    # Definimos la ruta del archivo.
    ruta = carpeta / nombre_archivo

    # Generamos 200 valores entre a y b.
    valores_x = np.linspace(a, b, cantidad)

    # Abrimos el archivo CSV.
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:

        escritor = csv.writer(archivo)

        # Escribimos los encabezados.
        escritor.writerow(["x", "f(x)"])

        # Evaluamos la funcion en cada valor.
        for x in valores_x:

            y = funcion(x)

            # Guardamos el par (x, f(x)).
            escritor.writerow([x, y])

    print("Datos guardados en:", ruta)


def main():

    # Configuracion de los experimentos.
    tolerancia = 1e-6
    max_iteraciones = 100

    # Diccionario para guardar todos los experimentos.
    resultados_generales = {}

  
    print("LABORATORIO 2 - La raiz que se esconde")
  
    print("Tolerancia:", tolerancia)
    print("Maximo de iteraciones:", max_iteraciones)

    # Recorremos las seis funciones matematicas.
    for nombre, datos in funciones.items():

        print("FUNCION:", nombre)

        # Ejecutamos los seis metodos sobre la funcion.
        resultados = ejecutar_metodos(
            datos,
            tolerancia,
            max_iteraciones
        )

        # Guardamos los resultados para el resumen CSV.
        resultados_generales[nombre] = resultados

        # Mostramos los encabezados de la tabla.
        print(
            f"{'Metodo':<22}"
            f"{'Raiz':<20}"
            f"{'Iteraciones':<15}"
            f"{'Convergencia':<15}"
        )

        # Recorremos los resultados obtenidos.
        for metodo, resultado in resultados.items():

            raiz = resultado["raiz"]
            iteraciones = resultado["iteraciones"]
            convergencia = resultado["convergencia"]

            # Preparamos la raiz para mostrarla.
            if raiz is None or not np.isfinite(raiz):

                raiz_texto = "No encontrada"

            else:

                raiz_texto = f"{raiz:.8f}"

            # Mostramos el resultado del metodo.
            print(
                f"{metodo:<22}"
                f"{raiz_texto:<20}"
                f"{iteraciones:<15}"
                f"{str(convergencia):<15}"
            )

        # Guardamos los 200 puntos de la funcion.
        guardar_datos_fun(
            nombre,
            datos["funcion"],
            datos["a"],
            datos["b"]
        )

    # Guardamos el resumen de los 36 experimentos.
    guardar_resumen(resultados_generales)

    print("EXPERIMENTOS FINALIZADOS")
  

# Ejecutamos el programa.
if __name__ == "__main__":
    main()
