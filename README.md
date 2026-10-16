# Laboratorio 2: La raíz que se esconde

### Integrantes
Felipe Araya Díaz, Mariana Morales Muñoz

### Asignatura
Computación Numérica 

## Descripción

Implementación y comparación de seis métodos numéricos para encontrar raíces de funciones:

- Bisección
- Falsa posición
- Secante
- Punto fijo
- Newton-Raphson
- Newton-Raphson mejorado

Se utilizan seis funciones matemáticas, una tolerancia de `1e-6` y un máximo de 100 iteraciones.

## Requisitos

- Python 3
- NumPy
- Matplotlib
- Pandas

## Instalación

Crear y activar el entorno virtual en Windows:

    python -m venv .venv
    .\.venv\Scripts\Activate.ps1

Instalar las dependencias:

    pip install -r requirements.txt

## Ejecución

Ejecutar desde la carpeta principal del proyecto.

Generar los resultados y archivos CSV:

    python src/scripts/experimentos.py

Generar los gráficos:

    python src/scripts/graficos.py

## Estructura del proyecto

- `src/scripts/funciones.py`: funciones matemáticas y derivadas.
- `src/scripts/metodos.py`: implementación de los seis métodos.
- `src/scripts/experimentos.py`: ejecución de experimentos y generación de CSV.
- `src/scripts/graficos.py`: generación de gráficos.
- `src/data/`: archivos CSV.
- `src/assets/`: gráficos PNG.
- `informe.md`: análisis y conclusiones del laboratorio.
- `requirements.txt`: dependencias del proyecto.

## Resultados

El proyecto genera siete archivos CSV: seis con los datos de las funciones y uno con el resumen de los 36 experimentos.

También genera gráficos de las funciones, gráficos de convergencia en escala logarítmica y un resumen de iteraciones.

El análisis de los resultados se encuentra en `informe.md`.
