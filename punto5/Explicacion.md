# Punto 5 

En este punto se diseño e implemento un parser descendente recursivo que incluye un algoritmo de emparejamiento de tokens.

El parser permite reconocer instrucciones de asignacion y estructuras condicionales.

---

## Objetivo

* Diseñar un algoritmo de emparejamiento
* Implementar un parser descendente recursivo
* Definir una gramatica con asignaciones y condicionales

---

## Gramatica utilizada

Se definio la siguiente gramatica sencilla:
```

programa -> sentencia lista

lista -> sentencia lista
| ε

sentencia -> asignacion
| condicional

asignacion -> ID = expr

condicional -> if expr then sentencia else sentencia

expr -> ID
| NUM
```
---

## Algoritmo de emparejamiento

El algoritmo de emparejamiento se encarga de verificar que el token actual coincida con el esperado.

Si coincide, avanza en la entrada.
Si no coincide, se genera un error.

---

## Implementacion del parser

El parser fue implementado en Python utilizando funciones recursivas.

Cada funcion representa una regla de la gramatica.

```python id="parser_p5"
tokens = []
pos = 0

def match(t):
    global pos
    if pos < len(tokens) and tokens[pos] == t:
        pos += 1
    else:
        raise Exception("Error de sintaxis")

def programa():
    sentencia()
    lista()

def lista():
    if pos < len(tokens):
        sentencia()
        lista()

def sentencia():
    if tokens[pos] == "if":
        condicional()
    else:
        asignacion()

def asignacion():
    match("ID")
    match("=")
    expr()

def condicional():
    match("if")
    expr()
    match("then")
    sentencia()
    match("else")
    sentencia()

def expr():
    if tokens[pos] == "ID":
        match("ID")
    else:
        match("NUM")
```

---

## Tokens utilizados:

["if", "ID", "then", "ID", "=", "NUM", "else", "ID", "=", "NUM"]

Resultado:

La cadena es reconocida correctamente sin errores de sintaxis.

---

## Ejecucion y pruebas

Para ejecutar el parser, se debe utilizar el archivo `parser_p5.py`.

---

### Pasos para ejecutar

1. Abrir una terminal en la carpeta del proyecto
2. Ejecutar el siguiente comando:

```bash
python parser_p5.py
```

---

### Ejemplos de prueba

El archivo ya incluye algunos ejemplos que se ejecutan automaticamente:

#### Ejemplo 1

Entrada:
```
x = 5
```
Resultado esperado:
```
Cadena valida
```
---

#### Ejemplo 2

Entrada:
```
if x then y = 5 else y = 10
``` 
Resultado esperado:

Cadena valida

---

#### Ejemplo 3

Entrada:
```
if x then if y then z = 1 else z = 2
```
Resultado esperado:
```
Cadena valida
```
---

### Pruebas adicionales

Tambien se pueden probar nuevas entradas modificando la funcion ejecutar en el archivo:

```python
ejecutar("if x then y = 5 else y = 10")
```

Ejemplo de error:

Entrada:
```
if x then y = else 10
```
Resultado esperado:
```
Error de sintaxis
```
---

## Punto de vista

* El parser utiliza un enfoque simple basado en recursion
* El algoritmo de emparejamiento permite validar la estructura paso a paso
* La implementacion es suficiente para gramaticas pequeñas
