import csv
import numpy as np

from pathlib import Path
from metodos import biseccion, falsa_posicion, secante
from funciones import fun_polinomica
from funciones import fun_raiz_doble
from funciones import fun_logaritmica

# fun para guardar los resultados en un archivo CSV
def guardar_resumen(resultados):

    # Obtenemos la ubicacion del archivo actual
    carpeta_scripts = Path(__file__).resolve().parent

    # Obtenemos la carpeta src.
    carpeta_src = carpeta_scripts.parent

    # Definimos la carpeta donde guardaremos los CSV
    carpeta_data = carpeta_src / "data"

    # Creamos la carpeta si no existe
    carpeta_data.mkdir(parents=True, exist_ok=True)

    # Definimos la ruta del archivo
    ruta_csv = carpeta_data / "resumen_convergencia.csv"

    # Abrimos el archivo CSV en modo escritura
    with open(ruta_csv, "w", newline="", encoding="utf-8") as archivo:

        # Creamos el escritor de CSV
        escritor = csv.writer(archivo)

        # Escribimos los encabezados
        escritor.writerow([
            "Funcion",
            "Metodo",
            "Raiz",
            "Iteraciones",
            "Error_residual",
            "Convergencia"
        ])

        # Recorremos las seis funciones
        for nombre_funcion, resultados in resultados_generales.items():

            # Recorremos los metodos de cada funcion
            for nombre_metodo, resultado in resultados.items():

                # Obtenemos la raiz aproximada
                raiz = resultado["raiz"]

                # Obtenemos las iteraciones
                iteraciones = resultado["iteraciones"]

                # Obtenemos el estado de convergencia
                convergencia = resultado["convergencia"]

                # Obtenemos la funcion original
                funcion = funciones[nombre_funcion]["funcion"]

                # Calculamos el error residual final
                if raiz is not None:
                    error = abs(funcion(raiz))
                else:
                    error = ""

                # Escribimos los datos en el CSV
                escritor.writerow([
                    nombre_funcion,
                    nombre_metodo,
                    raiz if raiz is not None else "",
                    iteraciones,
                    error,
                    convergencia
                ])

    # Mostramos un mensaje de confirmacion
    print("\nResumen general guardado correctamente:")
    print(ruta_csv)


# Funcion para generar un CSV con los puntos de una funcion
def guardar_datos_fun(nombre, funcion, a, b, cantidad=200):

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



# Funcion principal del programa.
def main():

    # Definimos las condiciones del laboratorio.
    tolerancia = 1e-6
    max_iteraciones = 100

    print("==============================================")
    print("     LABORATORIO 2 - BUSQUEDA DE RAICES")
    print("==============================================")

    print("Tolerancia:", tolerancia)
    print("Maximo de iteraciones:", max_iteraciones)
    
    # Diccionario para guardar todos los experimentos.
    resultados_generales = {}

    # Recorremos todas las funciones configuradas.
    for nombre, datos in funciones.items():

        # Obtenemos el intervalo.
        a = datos["a"]
        b = datos["b"]

        # Ejecutamos los tres metodos.
        resultados = ejecutar_metodos(
            datos,
            tolerancia,
            max_iteraciones
        )
        
        # Guardamos los resultados de esta funcion.
        resultados_generales[nombre] = resultados

        # Mostramos el nombre de la funcion.
        print("\nFUNCION:", nombre)
        print("Intervalo:", [a, b])

        # Encabezado de la tabla.
        print("-" * 70)

        print(
            f"{'Metodo':<18}"
            f"{'Raiz':<18}"
            f"{'Iteraciones':<15}"
            f"{'Convergencia':<15}"
        )

        print("-" * 70)

        # Recorremos los resultados obtenidos.
        for metodo, resultado in resultados.items():

            raiz = resultado["raiz"]
            iteraciones = resultado["iteraciones"]
            convergencia = resultado["convergencia"]

            # Comprobamos si existe una raiz calculada.
            if raiz is not None:
                raiz_texto = f"{raiz:.8f}"
            else:
                raiz_texto = "No encontrada"

            # Mostramos la fila correspondiente.
            print(
                f"{metodo:<18}"
                f"{raiz_texto:<18}"
                f"{iteraciones:<15}"
                f"{str(convergencia):<15}"
            )

    # Guardamos los resultados en un archivo CSV
    guardar_resumen(resultados)
    # Generamos el CSV de la funcion polinomica
    guardar_datos_fun(
        "polinomica",
        fun_polinomica,
        a,
        b,
        200
    )

    # Generamos el CSV de la funcion con raiz doble
    guardar_datos_fun(
        "raiz_doble",
        fun_raiz_doble,
        1,
        3,
        200
    )

    # Generamos el CSV de la funcion logaritmica
    guardar_datos_fun(
        "logaritmica",
        fun_logaritmica,
        2,
        3,
        200
    )

    # Generamos el CSV de la funcion exponencial.
    guardar_datos_funcion(
        "exponencial",
        funcion_exponencial,
        0,
        1,
        200
    )

    # Generamos el CSV de la funcion trigonometrica.
    guardar_datos_funcion(
        "trigonometrica",
        funcion_trigonometrica,
        0,
        1,
        200
    )

    # Generamos el CSV de la funcion mixta.
    guardar_datos_funcion(
        "mixta",
        funcion_mixta,
        0.1,
        1,
        200
    )

    print("\nExperimento finalizado correctamente.")


# Ejecutamos el programa.
if __name__ == "__main__":
    main()
