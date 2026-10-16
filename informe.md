### Estudiantes: Felipe Araya Díaz y Mariana Morales Muñoz
# Informe Lab 2: Comparación de métodos de búsqueda de raíces


Tras haber completado la experimentación y observar los resultados, hacemos el siguiente análisis, respondiendo las preguntas proporcionadas:

### 1. ¿Qué método convergió en menos iteraciones en cada función? ¿Por qué?
En caso de "empate", se eligió el método con menor error residual.

| Función        | Método                  | Iteraciones |
| -------------- | ----------------------- | ----------- |
| Polinomica     | Newton-Raphson mejorado | 2           |
| Raíz Doble     | Newton-Raphson mejorado | 1           |
| Logarítmica    | Newton-Raphson          | 3           |
| Exponencial    | Newton-Raphson          | 2           |
| Trigonométrica | Newton-Raphson          | 3           |
| Mixta          | Newton-Raphson mejorado | 2           |

El factor principal que influye en la convergencia de Newton-Raphson es el valor de x_0, se eligieron valores que se encontraban en el intervalos usados al rededor de la raiz; eso junto con que el método y su version mejorada tienen una velocidad cuadrática, hicieron que la convergencia sea relativamente rápida y los métodos predominaran en cuanto a velocidad.

### 2. ¿Qué orden de convergencia tiene cada método y cómo se refleja en el gráfico |error| vs iteración?
Observando los gráficos de error vs. iteración:
| Método                  | Velocidad               | Observación                                  |
| ----------------------- | ----------------------- | -------------------------------------------- |
| Biseccion               | Lineal (O(h))           | El error disminuye de forma constante        |
| Falsa posicion          | Lineal (O(h))           | El error disminuye de forma constante        |
| Punto fijo              | Lineal (O(h))           | El error disminuye de forma constante        |
| Secante                 | Superlineal (orden ≈ 1.618) | El error disminuye en forma de parábola |
| Newton-Raphson          | Cuadrática (O(h^2))     | El error disminuye en forma de parábola      |
| Newton-Raphson mejorado | Cuadrática (O(h^2))     | El error disminuye en forma de parábola      |

El comportamiento de las curvas son compatibles con las propiedades teóricas de los métodos, aunque los gráficos por sí solos no permiten determinar exactamente el orden de convergencia.

### 3. ¿Qué métodos requieren un intervalo con cambio de signo y cuáles no?

| Método                  | Requiere cambio de signo |
| ----------------------- | ------------------------ |
| Biseccion               | Si                       |
| Falsa posicion          | Si                       |
| Punto fijo              | No                       |
| Secante                 | No                       |
| Newton-Raphson          | No                       |
| Newton-Raphson mejorado | No                       |


### 4. En la función que toca el eje x (raíz doble): ¿qué métodos fallan o no aplican y cuál se comporta mejor? ¿Por qué?
Los métodos que fallan inmediatamente son el de la bisección y falsa posición, ya que estos requieren obligatoriamente de un cambio de signo en el intervalo, condición que no se cumple para la función de raíz doble.
El método que mejor funciona es Newton-Raphson mejorado. Esto se debe a que incorpora información de la segunda derivada, lo que permite tratar de forma más eficiente las raíces múltiples.
n nuestros experimentos, Newton-Raphson mejorado encontró la raíz x=2 en 1 iteración, mientras que Newton-Raphson tradicional necesitó 10 y secante 19.


### 5. ¿Cómo influyen el intervalo inicial y la estimación inicial en la cantidad de iteraciones y en si el método converge?
Influyen directamente en lo rapido que se encuentra la raíz y en algunos, la posibilidad de que converjan.

| Método                        | Análisis             |
| ----------------------------- | -------------------- |
| Biseccion & Falsa posición    | Necesitan un intervalo donde exista un cambio de signo y el tamaño del intervalo influye en la cantidad de iteraciones. |
| Punto fijo                    | Depende de que g(x) converga y el valor inicial influye en la cantidad de iteraciones. |
| Secante                       | La convergencia es sensible a los valores iniciales. |
| Newton-Raphson & N-R mejorado | Un valor inicial cercano a la raíz suele favorecer la convergencia, mientras que uno alejado puede provocar divergencia o problemas si la derivada se anula o es muy pequeña. |

### 6. ¿Qué método recomiendan según el tipo de función, considerando el compromiso entre velocidad y robustez?
En general, para todas las funciones, Newton-Raphson y la versrión mejorada ofrecen la mejor velocidad en comparación con los otros métodos, aunque tienen la gran desventaja de requerir las derivadas de la función a procesar; por lo que la falsa posición termian siendo una muy buena segunda opción.


## Conclusión
#### ¿Qué ocurrió en la raíz doble y qué dice eso sobre «tener raíz» frente a «cambiar de signo»?
Que los métodos cerrados no hayan funcionado en la función de raíz doble demuestra que, conceptualmente, buscar la existencia de una raíz mediante un cambio de signo es útil, pero no es una condición necesaria para que exista una raíz.
En nuestro caso, (f(x)=(x-2)^2) tiene una raíz en (x=2), donde la gráfica toca el eje horizontal sin cruzarlo. Por eso, bisección y falsa posición no pudieron aplicarse con el intervalo seleccionado, mientras que Newton-Raphson mejorado encontró la raíz en una iteración.

#### ¿Cómo cambió el número de iteraciones al mover el intervalo o la estimación inicial?
El intervalo y las estimaciones iniciales pueden influir en la cantidad de iteraciones necesarias para alcanzar la convergencia. En general, elegir un intervalo más pequeño puede reducir las iteraciones necesarias en bisección, mientras que en falsa posición también influye el comportamiento de la función.
En métodos como Newton-Raphson y secante, las estimaciones iniciales influyen en la velocidad y en la posibilidad de convergencia.
Para cuantificar estos cambios sería necesario realizar experimentos adicionales, modificando únicamente los valores iniciales y comparando las iteraciones obtenidas.