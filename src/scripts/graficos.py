import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

# Funcion para graficar una funcion matematica
def graficar_funcion(nombre, fx, funcion, a, b, raiz):
    carpeta_scripts = Path(__file__).resolve().parent
    carpeta_src = carpeta_scripts.parent
    carpeta_assets = carpeta_src / "assets"
    carpeta_assets.mkdir(parents=True, exist_ok=True)
    # Generamos 200 puntos en el intervalo
    valores_x = np.linspace(a, b, 200)
    # Evaluamos la funcion en cada punto
    valores_y = []

    for x in valores_x:
        valores_y.append(funcion(x))

    # Creamos una nueva figura
    plt.figure(figsize=(8, 5))
    # Dibujamos la funcion
    plt.plot(valores_x, valores_y, label=nombre)
    # Dibujamos el eje horizontal y = 0
    plt.axhline(0, color="black", linewidth=0.8)

    # Marcamos la raiz encontrada
    if raiz is not None:
        plt.scatter(
            raiz,
            funcion(raiz),
            color="red",
            label=f"Raiz aproximada: {raiz:.6f}",
            zorder=5
        )

    # Agregamos el titulo
    plt.title("Grafico de " + nombre)
    # Etiquetamos los ejes
    plt.xlabel("x")
    plt.ylabel(f"f(x) = {fx}")
    # Mostramos la leyenda
    plt.legend()
    # Agregamos una cuadricula
    plt.grid(True)
    # Ajustamos la distribucion
    plt.tight_layout()

    # Definimos la ruta donde se guardara
    ruta_grafico = carpeta_assets / (nombre + ".png")

    # Guardamos la imagen
    plt.savefig(ruta_grafico, dpi=300)
    # Cerramos la figura para liberar memoria
    plt.close()
    # Mostramos un mensaje
    print("Grafico guardado en:", ruta_grafico)

def graficar_convergencia(nombre_funcion, resultados, funcion):
    # Definimos las carpetas de guardado
    carpeta_scripts = Path(__file__).resolve().parent
    carpeta_src = carpeta_scripts.parent
    carpeta_assets = carpeta_src / "assets"
    carpeta_assets.mkdir(parents=True, exist_ok=True)

    # Creamos la figura
    plt.figure(figsize=(8, 5))

    hay_datos = False

    for nombre_metodo, resultado in resultados.items():
        # Calculamos el mismo tipo de error para todos los metodos
        errores = np.array(
            [abs(funcion(x)) for x in resultado["historial"]],
            dtype=float
)
        iteraciones = np.arange(1, len(errores) + 1)

        # La escala logaritmica requiere errores positivos
        validos = np.isfinite(errores) & (errores > 0)

        if not np.any(validos):
            continue

        etiqueta = nombre_metodo

        if not resultado["convergencia"]:
            etiqueta += " (no convergio)"

        plt.plot(iteraciones[validos], errores[validos], marker="o", label=etiqueta)

        hay_datos = True

    # Configuramos la grafica
    plt.yscale("log")
    plt.xlabel("Iteracion")
    plt.ylabel("Error residual |f(x)|")
    plt.title(f"Convergencia - {nombre_funcion}")
    plt.grid(True, which="both", linestyle="--", alpha=0.5)

    if hay_datos:
        plt.legend()
    else:
        plt.text(
            0.5, 0.5,
            "No hay errores positivos para graficar",
            ha="center",
            va="center",
            transform=plt.gca().transAxes
        )

    plt.tight_layout()

    # Guardamos la imagen en assets
    nombre_archivo = f"convergencia_{nombre_funcion}.png"
    ruta_grafico = carpeta_assets / nombre_archivo

    plt.savefig(ruta_grafico, dpi=300)
    plt.close()

    print("Grafico guardado en:", ruta_grafico)


def graficar_iteraciones(resultados_por_funcion):
    # Definir las carpetas de guardado
    carpeta_scripts = Path(__file__).resolve().parent
    carpeta_src = carpeta_scripts.parent
    carpeta_assets = carpeta_src / "assets"
    carpeta_assets.mkdir(parents=True, exist_ok=True)

    # Obtener todas las funciones y metodos
    funciones = list(resultados_por_funcion.keys())

    metodos = []
    for resultados in resultados_por_funcion.values():
        for nombre_metodo in resultados.keys():
            if nombre_metodo not in metodos:
                metodos.append(nombre_metodo)

    # Configurar las barras
    x = np.arange(len(funciones))
    ancho = 0.8 / len(metodos)

    plt.figure(figsize=(14, 7))

    # Dibujar una barra por metodo para cada funcion
    for i, metodo in enumerate(metodos):
        valores = []

        for funcion in funciones:
            resultado = resultados_por_funcion[funcion].get(metodo)

            if resultado is not None and resultado["convergencia"]:
                valores.append(resultado["iteraciones"])
            else:
                valores.append(np.nan)

        desplazamiento = (i - (len(metodos) - 1) / 2) * ancho

        barras = plt.bar(
            x + desplazamiento,
            valores,
            ancho,
            label=metodo
        )

        # Mostrar el numero de iteraciones sobre cada barra
        for barra, valor in zip(barras, valores):
            if np.isfinite(valor):
                plt.text(
                    barra.get_x() + barra.get_width() / 2,
                    barra.get_height(),
                    str(int(valor)),
                    ha="center",
                    va="bottom",
                    fontsize=8
                )

    # Configurar el grafico
    plt.title("Comparacion de iteraciones por funcion y metodo")
    plt.xlabel("Funcion")
    plt.ylabel("Numero de iteraciones")
    plt.xticks(x, funciones, rotation=20, ha="right")
    plt.legend(title="Metodo numerico")
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()

    # Guardar la imagen
    ruta_grafico = carpeta_assets / "resumen_iteraciones.png"
    plt.savefig(ruta_grafico, dpi=300)
    plt.close()

    print("Grafico guardado en:", ruta_grafico)



# Programa de prueba
if __name__ == "__main__":

    from funciones import fun_polinomica
    from funciones import fun_raiz_doble
    from funciones import fun_logaritmica
    from funciones import fun_exponencial
    from funciones import fun_trigonometrica
    from funciones import fun_mixta

    from funciones import derivada_polinomica
    from funciones import derivada_raiz_doble
    from funciones import derivada_logaritmica
    from funciones import derivada_exponencial
    from funciones import derivada_trigonometrica
    from funciones import derivada_mixta

    from funciones import segunda_derivada_polinomica
    from funciones import g_polinomica
    from funciones import segunda_derivada_raiz_doble
    from funciones import g_raiz_doble
    from funciones import segunda_derivada_logaritmica
    from funciones import g_logaritmica
    from funciones import segunda_derivada_exponencial
    from funciones import g_exponencial
    from funciones import segunda_derivada_trigonometrica
    from funciones import g_trigonometrica
    from funciones import segunda_derivada_mixta
    from funciones import g_mixta

    from metodos import biseccion
    from metodos import falsa_posicion
    from metodos import punto_fijo
    from metodos import secante
    from metodos import newton_raphson
    from metodos import newton_raphson_mejorado
    
    from experimentos import funciones


    # Calculamos la raiz con biseccion -------------------------------------------------------------------
    resultado_polinomica = biseccion(fun_polinomica, 1, 2, 1e-6, 100)
    # Generamos el grafico
    graficar_funcion("polinomica", "x^3 - x - 2", fun_polinomica, 1, 2, resultado_polinomica["raiz"])

    # Utilizamos la raiz exacta conocida -------------------------------------------------------------------
    graficar_funcion("raiz_doble", "(x - 2)^2", fun_raiz_doble, 1, 3, 2)

    # Calculamos la raiz con biseccion -------------------------------------------------------------------
    resultado_logaritmica = biseccion(fun_logaritmica, 2, 3, 1e-6, 100)
    # Generamos el grafico
    graficar_funcion("logaritmica", "ln(x) + x - 4", fun_logaritmica, 2, 3, resultado_logaritmica["raiz"])

    # Calculamos la raiz con biseccion -------------------------------------------------------------------
    resultado_exponencial = biseccion(fun_exponencial, 0, 1, 1e-6, 100)
    # Generamos el grafico
    graficar_funcion("exponencial", "e^(-x) - x",fun_exponencial, 0, 1, resultado_exponencial["raiz"])

    # Calculamos la raiz con biseccion -------------------------------------------------------------------
    resultado_trigonometrica = biseccion(fun_trigonometrica, 0, 1, 1e-6, 100)
    # Generamos el grafico
    graficar_funcion("trigonometrica", "cos(x) - x", fun_trigonometrica, 0, 1, resultado_trigonometrica["raiz"])

    # Calculamos la raiz con biseccion -------------------------------------------------------------------
    resultado_mixta = biseccion(fun_mixta, 0.1, 1, 1e-6, 100)
    # Generamos el grafico
    graficar_funcion("mixta", "√x - cos(x)", fun_mixta, 0.1, 1, resultado_mixta["raiz"])


    resultados_por_funcion = {
        "Polinomica": {
            "Biseccion": biseccion(fun_polinomica, 1, 2, 1e-6, 100),
            "Falsa posicion": falsa_posicion(fun_polinomica, 1, 2, 1e-6, 100),
            "Punto fijo": punto_fijo(g_polinomica, 1.5, 1e-6, 100),
            "Secante": secante(fun_polinomica, 1.5, 2, 1e-6, 100),
            "Newton-Raphson": newton_raphson(fun_polinomica, derivada_polinomica, 1.5, 1e-6, 100),
            "Newton-Raphson mejorado": newton_raphson_mejorado(fun_polinomica, derivada_polinomica, segunda_derivada_polinomica, 1.5, 1e-6, 100)
        },

        "Raiz doble": {
            "Biseccion": biseccion(fun_raiz_doble, 1, 3, 1e-6, 100),
            "Falsa posicion": falsa_posicion(fun_raiz_doble, 1, 3, 1e-6, 100),
            "Punto fijo": punto_fijo(g_raiz_doble, 1.2, 1e-6, 100),
            "Secante": secante(fun_raiz_doble, 1.2, 3, 1e-6, 100),
            "Newton-Raphson": newton_raphson(fun_raiz_doble, derivada_raiz_doble, 1.2, 1e-6, 100),
            "Newton-Raphson mejorado": newton_raphson_mejorado(fun_raiz_doble, derivada_raiz_doble, segunda_derivada_raiz_doble, 1.2, 1e-6, 100)
        },
        
        "Logaritmica": {
            "Biseccion": biseccion(fun_logaritmica, 2, 3, 1e-6, 100),
            "Falsa posicion": falsa_posicion(fun_logaritmica, 2, 3, 1e-6, 100),
            "Punto fijo": punto_fijo(g_logaritmica, 2.5, 1e-6, 100),
            "Secante": secante(fun_logaritmica, 2.5, 3, 1e-6, 100),
            "Newton-Raphson": newton_raphson(fun_logaritmica, derivada_logaritmica, 2.5, 1e-6, 100),
            "Newton-Raphson mejorado": newton_raphson_mejorado(fun_logaritmica, derivada_logaritmica, segunda_derivada_logaritmica, 2.5, 1e-6, 100)
        },
        
        "Exponencial": {
            "Biseccion": biseccion(fun_exponencial, 0, 1, 1e-6, 100),
            "Falsa posicion": falsa_posicion(fun_exponencial, 0, 1, 1e-6, 100),
            "Punto fijo": punto_fijo(g_exponencial, 0.5, 1e-6, 100),
            "Secante": secante(fun_exponencial, 0.5, 1, 1e-6, 100),
            "Newton-Raphson": newton_raphson(fun_exponencial, derivada_exponencial, 0.5, 1e-6, 100),
            "Newton-Raphson mejorado": newton_raphson_mejorado(fun_exponencial, derivada_exponencial, segunda_derivada_exponencial, 0.5, 1e-6, 100)
        },

        "Trigonometrica": {
            "Biseccion": biseccion(fun_trigonometrica, 0, 1, 1e-6, 100),
            "Falsa posicion": falsa_posicion(fun_trigonometrica, 0, 1, 1e-6, 100),
            "Punto fijo": punto_fijo(g_trigonometrica, 0.5, 1e-6, 100),
            "Secante": secante(fun_trigonometrica, 0.5, 1, 1e-6, 100),
            "Newton-Raphson": newton_raphson(fun_trigonometrica, derivada_trigonometrica, 0.5, 1e-6, 100),
            "Newton-Raphson mejorado": newton_raphson_mejorado(fun_trigonometrica, derivada_trigonometrica, segunda_derivada_trigonometrica, 0.5, 1e-6, 100)
        },

        "Mixta": {
            "Biseccion": biseccion(fun_mixta, 0.1, 1, 1e-6, 100),
            "Falsa posicion": falsa_posicion(fun_mixta, 0.1, 1, 1e-6, 100),
            "Punto fijo": punto_fijo(g_mixta, 0.5, 1e-6, 100),
            "Secante": secante(fun_mixta, 0.5, 1, 1e-6, 100),
            "Newton-Raphson": newton_raphson(fun_mixta, derivada_mixta, 0.5, 1e-6, 100),
            "Newton-Raphson mejorado": newton_raphson_mejorado(fun_mixta, derivada_mixta, segunda_derivada_mixta, 0.5, 1e-6, 100)
        }    
    }

    for nombre, resultados in resultados_por_funcion.items():
        if resultados:
            graficar_convergencia(nombre, resultados, funciones[nombre]["funcion"]
            )

    graficar_iteraciones(resultados_por_funcion)
