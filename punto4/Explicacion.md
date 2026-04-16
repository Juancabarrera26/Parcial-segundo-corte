# Punto 4

En este punto se implemento un parser basado en el algoritmo CYK para evaluar expresiones de una calculadora simple.
Adicionalmente, se comparo su rendimiento con un parser de tipo predictivo.

---

## Objetivo

* Implementar el algoritmo CYK
* Aplicarlo a expresiones aritmeticas
* Comparar su rendimiento con otro tipo de parser

---

## Gramatica utilizada

Se utilizo una gramatica sencilla para expresiones aritmeticas:

E -> E + T | T
T -> T * F | F
F -> ( E ) | num

Esta gramatica permite operaciones basicas como suma, multiplicacion y uso de parentesis.

---

## Implementacion del algoritmo CYK

El algoritmo CYK utiliza programacion dinamica para verificar si una cadena pertenece a un lenguaje definido por una gramatica.

Se construye una tabla donde cada celda representa subconjuntos de la cadena evaluada.

---

## Codigo implementado en py

```python id="cyk_code"
def cyk(cadena, reglas):
    n = len(cadena)
    tabla = [[set() for _ in range(n)] for _ in range(n)]

    # Inicializacion
    for i in range(n):
        for izq, der in reglas:
            if cadena[i] in der:
                tabla[i][i].add(izq)

    # Llenado de la tabla
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                for izq, der in reglas:
                    if len(der) == 2:
                        if der[0] in tabla[i][k] and der[1] in tabla[k + 1][j]:
                            tabla[i][j].add(izq)

    return 'E' in tabla[0][n - 1]
```

---

## Pruebas realizadas

Se probaron expresiones simples como:

* 2 + 3
* 2 * 3
* ( 2 + 3 ) * 4

Resultados:

* Las expresiones validas fueron reconocidas correctamente
* El algoritmo funciona correctamente para cadenas cortas

---

## Parser predictivo

Se implemento un parser descendente simple para la misma gramatica, utilizando funciones recursivas.

Este parser analiza la cadena de izquierda a derecha sin necesidad de construir una tabla.

---

## Comparacion de rendimiento

Se evaluaron ambos parsers teniendo en cuenta el tiempo y la complejidad.

| Aspecto                     | CYK          | Predictivo    |
| --------------------------- | ------------ | ------------- |
| Complejidad                 | Alta (cubic) | Baja (lineal) |
| Tiempo de ejecucion         | Mayor        | Menor         |
| Uso de memoria              | Alto         | Bajo          |
| Facilidad de implementacion | Media        | Alta          |

---

## Analisis

El algoritmo CYK es mas general y puede trabajar con una mayor variedad de gramaticas, pero su costo computacional es alto.

El parser predictivo es mas eficiente y rapido, por lo que es mas adecuado en aplicaciones reales.

