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



# Programa de prueba
if __name__ == "__main__":

    from funciones import funcion_polinomica
    from funciones import funcion_raiz_doble
    from funciones import funcion_logaritmica
    from funciones import funcion_exponencial
    from funciones import funcion_trigonometrica
    from funciones import funcion_mixta
    from metodos import biseccion

    # Calculamos la raiz con biseccion -------------------------------------------------------------------
    resultado_polinomica = biseccion(funcion_polinomica, 1, 2, 1e-6, 100)
    # Generamos el grafico
    graficar_funcion("polinomica", "x^3 - x - 2", funcion_polinomica, 1, 2, resultado_polinomica["raiz"])


    # Utilizamos la raiz exacta conocida -------------------------------------------------------------------
    graficar_funcion("raiz_doble", "(x - 2)^2", funcion_raiz_doble, 1, 3, 2)


    # Calculamos la raiz con biseccion -------------------------------------------------------------------
    resultado_logaritmica = biseccion(funcion_logaritmica, 2, 3, 1e-6, 100)
    # Generamos el grafico
    graficar_funcion("logaritmica", "ln(x) + x - 4", funcion_logaritmica, 2, 3, resultado_logaritmica["raiz"])


    # Calculamos la raiz con biseccion -------------------------------------------------------------------
    resultado_exponencial = biseccion(funcion_exponencial, 0, 1, 1e-6, 100)
    # Generamos el grafico
    graficar_funcion("exponencial", "e^(-x) - x",funcion_exponencial, -1, 2, resultado_exponencial["raiz"])


    # Calculamos la raiz con biseccion -------------------------------------------------------------------
    resultado_trigonometrica = biseccion(funcion_trigonometrica, 0, 1, 1e-6, 100)
    # Generamos el grafico
    graficar_funcion("trigonometrica", "cos(x) - x", funcion_trigonometrica, -1, 2, resultado_trigonometrica["raiz"])


    # Calculamos la raiz con biseccion -------------------------------------------------------------------
    resultado_mixta = biseccion(funcion_mixta, 0.1, 1, 1e-6, 100)
    # Generamos el grafico
    graficar_funcion("mixta", "√x - cos(x)", funcion_mixta, -1, 2, resultado_mixta["raiz"])
