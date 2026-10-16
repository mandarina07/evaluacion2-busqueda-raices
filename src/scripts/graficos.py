import numpy as np
import matplotlib.pyplot as plt

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


def graficar_convergencia(nombre_funcion, resultados):
    # Definimos las carpetas de guardado
    carpeta_scripts = Path(__file__).resolve().parent
    carpeta_src = carpeta_scripts.parent
    carpeta_assets = carpeta_src / "assets"
    carpeta_assets.mkdir(parents=True, exist_ok=True)

    # Creamos la figura
    plt.figure(figsize=(8, 5))

    hay_datos = False

    for nombre_metodo, resultado in resultados.items():
        errores = np.array(resultado["errores"], dtype=float)

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
    plt.ylabel("Error absoluto")
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

    from metodos import biseccion
    from metodos import falsa_posicion
    from metodos import punto_fijo
    from metodos import secante
    from metodos import newton_raphson
    from metodos import newton_raphson_mejorado


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
    graficar_funcion("mixta", "√x - cos(x)", fun_mixta, 0, 1, resultado_mixta["raiz"])


    resultados_por_funcion = {
        "Polinomica": {
            "Biseccion": biseccion(fun_polinomica, 1, 2),
            "Falsa posicion": falsa_posicion(fun_polinomica, 1, 2),
            "Punto fijo": punto_fijo("", 2),
            "Secante": secante(fun_polinomica, 1, 2),
            "Newton-Raphson": newton_raphson(fun_polinomica, derivada_polinomica, 2),
            "Newton-Raphson mejorado": newton_raphson_mejorado(fun_polinomica, derivada_polinomica, "", 2)
        },

        "Raiz doble": {
            "Biseccion": biseccion(fun_raiz_doble, 1, 2),
            "Falsa posicion": falsa_posicion(fun_raiz_doble, 1, 2),
            "Punto fijo": punto_fijo("", 1.2),
            "Secante": secante(fun_raiz_doble, 1, 2),
            "Newton-Raphson": newton_raphson(fun_raiz_doble, derivada_raiz_doble, 1.2),
            "Newton-Raphson mejorado": newton_raphson_mejorado(fun_raiz_doble, derivada_raiz_doble, "", 1.2)
        },

        "Logaritmica": {
            "Biseccion": biseccion(fun_logaritmica, 2, 3),
            "Falsa posicion": falsa_posicion(fun_logaritmica, 2, 3),
            "Punto fijo": punto_fijo("", 3),
            "Secante": secante(fun_logaritmica, 2, 3),
            "Newton-Raphson": newton_raphson(fun_logaritmica, derivada_logaritmica, 3),
            "Newton-Raphson mejorado": newton_raphson_mejorado(fun_logaritmica, derivada_logaritmica, "", 3)
        },

        "Exponencial": {
            "Biseccion": biseccion(fun_exponencial, 0, 1),
            "Falsa posicion": falsa_posicion(fun_exponencial,  0, 1),
            "Punto fijo": punto_fijo("", 0),
            "Secante": secante(fun_exponencial,  0, 1),
            "Newton-Raphson": newton_raphson(fun_exponencial, derivada_exponencial, 0),
            "Newton-Raphson mejorado": newton_raphson_mejorado(fun_exponencial, derivada_exponencial, "", 0)
        },

        "Trigonometrica": {
            "Biseccion": biseccion(fun_trigonometrica, 0, 1),
            "Falsa posicion": falsa_posicion(fun_trigonometrica,  0, 1),
            "Punto fijo": punto_fijo("", 1),
            "Secante": secante(fun_trigonometrica,  0, 1),
            "Newton-Raphson": newton_raphson(fun_trigonometrica, derivada_trigonometrica, 1),
            "Newton-Raphson mejorado": newton_raphson_mejorado(fun_trigonometrica, derivada_trigonometrica, "", 1)
        },

        "Mixta": {
            "Biseccion": biseccion(fun_mixta, 0.1, 1),
            "Falsa posicion": falsa_posicion(fun_mixta,  0.1, 1),
            "Punto fijo": punto_fijo("", 0.5),
            "Secante": secante(fun_mixta,  0.1, 1),
            "Newton-Raphson": newton_raphson(fun_mixta, derivada_mixta, 0.5),
            "Newton-Raphson mejorado": newton_raphson_mejorado(fun_mixta, derivada_mixta, "", 0.5)
        }
    }

    for nombre, resultados in resultados_por_funcion.items():
        if resultados:
            graficar_convergencia(nombre, resultados)
