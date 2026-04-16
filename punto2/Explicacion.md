# Punto 2 

En este punto se implemento la gramatica definida en el punto 1 utilizando ANTLR4, haciendo uso del entorno de desarrollo IntelliJ IDEA.

ANTLR permite generar automaticamente analizadores sintacticos a partir de una gramatica, lo que facilita validar si una entrada pertenece al lenguaje definido.

---

## Entorno de trabajo

La implementacion se realizo utilizando:

* IntelliJ IDEA
* Plugin de ANTLR v4

Esto permitio generar y probar el parser directamente desde el entorno.

---

## Implementacion

Se definio un archivo de gramatica llamado CRUD.g4, el cual contiene las reglas del lenguaje CRUD propuesto.

Las instrucciones soportadas son:

* INSERTAR
* CONSULTAR
* MODIFICAR
* BORRAR

Cada una mantiene la estructura definida en el punto 1.

---

## Gramatica implementada

```antlr id="7gqzt0"
grammar CRUD;

programa: instruccion+ ;

instruccion
    : insertar
    | consultar
    | modificar
    | borrar
    ;

insertar: 'INSERTAR' ID '(' campos ')' ;

consultar: 'CONSULTAR' ID condicion ;

modificar: 'MODIFICAR' ID condicion '(' campos ')' ;

borrar: 'BORRAR' ID condicion ;

campos: campo (';' campo)* ;

campo: ID '=' valor ;

condicion: 'DONDE' ID op valor ;

op: '=' | '!=' | '<' | '>' ;

valor: NUM | STRING ;

ID: [a-zA-Z]+ ;
NUM: [0-9]+ ;
STRING: '"' (~["])* '"' ;

WS: [ \t\n\r]+ -> skip ;
```

---

## Pruebas realizadas

Las pruebas se ejecutaron utilizando la herramienta de ANTLR integrada en IntelliJ, la cual permite visualizar el arbol sintactico generado.

### Prueba 1

Entrada:
```

INSERTAR usuarios ( nombre = "Juan Camilo"; edad = 20 )
```
Resultado:
```
La instruccion es reconocida correctamente y se genera el arbol sintactico sin errores.
```
---

### Prueba 2

Entrada:
```
CONSULTAR usuarios DONDE edad > 18
```
Resultado:
```
La condicion es procesada correctamente.
```
---

### Prueba 3

Entrada:
```
MODIFICAR usuarios DONDE nombre = "Juan Camilo" ( edad = 21 )
```
Resultado:
``` 
Se reconoce la estructura completa de la instruccion.
```
---

### Prueba 4

Entrada:
```
BORRAR usuarios DONDE edad < 18
```
Resultado:
```
La instruccion es valida y no presenta errores sintacticos.
```
---

## Ejecucion en IntelliJ

Para ejecutar la gramatica en IntelliJ se siguieron los siguientes pasos:

1. Crear un proyecto en IntelliJ
2. Instalar el plugin de ANTLR v4
3. Agregar el archivo CRUD.g4
4. Click derecho sobre la regla programa
5. Seleccionar la opcion de prueba (Test Rule)
6. Ingresar una cadena de entrada

Esto permitio visualizar el arbol sintactico generado por el parser.
