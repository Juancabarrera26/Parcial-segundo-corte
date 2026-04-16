# Punto 3 - Ambiguedad en if-then-else


En este punto se analiza una gramatica propuesta para resolver la ambiguedad del uso del else en estructuras condicionales.

La gramatica dada es:
```

prop -> if expr then prop
| prop_emparejada

prop_emparejada -> if expr then prop_emparejada else prop
| otras
```
---

La idea es determinar si la gramatica es ambigua y, en caso de serlo, realizar las modificaciones necesarias para eliminar la ambiguedad.

---

## Demostracion de ambiguedad

Se analiza la siguiente expresion:

if a then if b then x else y

Esta expresion puede interpretarse de dos formas diferentes:

### Interpretacion 1

El else se asocia al segundo if:

if a then (if b then x else y)

### Interpretacion 2

El else se asocia al primer if:

(if a then if b then x) else y

Esto implica que existen dos arboles de derivacion distintos para la misma cadena, por lo tanto la gramatica sigue siendo ambigua.

---

## Analisis

Aunque la gramatica intenta separar los casos usando la regla prop_emparejada, aun permite que el else se asocie de forma diferente dependiendo de la derivacion.

Por esta razon, no elimina completamente la ambiguedad del problema conocido como dangling else.

---

## Correccion de la gramatica

Para eliminar la ambiguedad, se separan claramente las proposiciones en dos tipos:

* Emparejadas
* No emparejadas

La nueva gramatica es:

prop -> emparejada
| no_emparejada

emparejada -> if expr then emparejada else emparejada
| otras

no_emparejada -> if expr then prop
| if expr then emparejada else no_emparejada

---

## Explicacion de la solucion

Con esta nueva definicion:

* Las expresiones emparejadas siempre tienen un else correspondiente
* Las expresiones no emparejadas representan los casos incompletos

Esto asegura que el else se asocie siempre con el if mas cercano, eliminando la ambiguedad.
