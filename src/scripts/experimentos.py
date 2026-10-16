import csv
import numpy as np

from pathlib import Path
from metodos import biseccion, falsa_posicion, secante
from funciones import funcion_polinomica
from funciones import funcion_raiz_doble
from funciones import funcion_logaritmica

# Funcion para guardar los resultados en un archivo CSV
def guardar_resumen(resultados):

    carpeta_scripts = Path(__file__).resolve().parent
    carpeta_src = carpeta_scripts.parent
    carpeta_data = carpeta_src / "data"
    carpeta_data.mkdir(parents=True, exist_ok=True)
    ruta_csv = carpeta_data / "resumen_convergencia.csv"

    # Abrimos el archivo en modo escritura
    with open(ruta_csv, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        # Escribimos los encabezados del archivo
        escritor.writerow([
            "Funcion",
            "Metodo",
            "Raiz",
            "Iteraciones",
            "Error",
            "Convergencia"
        ])

        for metodo, resultado in resultados.items():
            if len(resultado["errores"]) > 0:
                error = resultado["errores"][-1]
            else:
                error = ""
            escritor.writerow([
                "Polinomica",
                metodo,
                resultado["raiz"],
                resultado["iteraciones"],
                error,
                resultado["convergencia"]
            ])

    print("\nArchivo CSV guardado correctamente:")
    print(ruta_csv)



# Funcion para generar un CSV con los puntos de una funcion
def guardar_datos_funcion(nombre, funcion, a, b, cantidad=200):

    carpeta_scripts = Path(__file__).resolve().parent
    carpeta_src = carpeta_scripts.parent
    carpeta_data = carpeta_src / "data"
    carpeta_data.mkdir(parents=True, exist_ok=True)
    ruta_csv = carpeta_data / (nombre + ".csv")
    valores_x = np.linspace(a, b, cantidad)

    # Abrimos el archivo CSV
    with open(ruta_csv, "w", newline="", encoding="utf-8") as archivo:
        # Creamos el escritor CSV
        escritor = csv.writer(archivo)
        escritor.writerow(["x", "f(x)"])
        # Recorremos todos los puntos generados
        for x in valores_x:
            y = funcion(x)
            escritor.writerow([x, y])
    # Mostramos un mensaje de confirmacion
    print("\nDatos de la funcion guardados:")
    print(ruta_csv)



# Funcion principal del programa
def main():

    # Definimos el intervalo inicial.
    a = 1
    b = 2
    tolerancia = 1e-6
    max_iteraciones = 100

    # Ejecutamos el metodo de biseccion
    resultado_biseccion = biseccion(
        funcion_polinomica,
        a,
        b,
        tolerancia,
        max_iteraciones
    )

    # Ejecutamos el metodo de falsa posicion
    resultado_falsa = falsa_posicion(
        funcion_polinomica,
        a,
        b,
        tolerancia,
        max_iteraciones
    )

    # Ejecutamos el metodo de secante
    resultado_secante = secante(
        funcion_polinomica,
        a,
        b,
        tolerancia,
        max_iteraciones
    )

    # Guardamos los resultados de los tres metodos
    resultados = {
        "Biseccion": resultado_biseccion,
        "Falsa posicion": resultado_falsa,
        "Secante": resultado_secante
    }

    # Mostramos la informacion
    print("==============================================")
    print("     LABORATORIO 2 - BUSQUEDA DE RAICES")
    print("==============================================")

    print("\nFuncion: f(x) = x^3 - x - 2")
    print("Intervalo inicial:", [a, b])
    print("Tolerancia:", tolerancia)
    print("Maximo de iteraciones:", max_iteraciones)

    print("\nCOMPARACION DE METODOS")
    print("-" * 75)

    print(
        f"{'Metodo':<18}"
        f"{'Raiz':<18}"
        f"{'Iteraciones':<18}"
        f"{'Convergencia':<15}"
    )

    print("-" * 75)

    # Recorremos cada metodo y su resultado
    for metodo, resultado in resultados.items():
        raiz = resultado["raiz"]
        iteraciones = resultado["iteraciones"]
        convergencia = resultado["convergencia"]

        if raiz is not None:
            raiz_texto = f"{raiz:.8f}"
        else:
            raiz_texto = "No encontrada"

        print(
            f"{metodo:<18}"
            f"{raiz_texto:<18}"
            f"{iteraciones:<18}"
            f"{str(convergencia):<15}"
        )

    # Guardamos los resultados en un archivo CSV
    guardar_resumen(resultados)
    # Generamos el CSV de la funcion polinomica
    guardar_datos_funcion(
        "polinomica",
        funcion_polinomica,
        a,
        b,
        200
    )

    # Generamos el CSV de la funcion con raiz doble
    guardar_datos_funcion(
        "raiz_doble",
        funcion_raiz_doble,
        1,
        3,
        200
    )

    # Generamos el CSV de la funcion logaritmica
    guardar_datos_funcion(
        "logaritmica",
        funcion_logaritmica,
        2,
        3,
        200
    )

    print("\nExperimento finalizado correctamente.")


# Ejecutamos el programa principal
if __name__ == "__main__":
    main()
