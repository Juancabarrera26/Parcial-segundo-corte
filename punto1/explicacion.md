# Punto 1 - Gramatica para operaciones CRUD

## Descripcion

En este punto se diseño una gramatica para un lenguaje sencillo que permite realizar operaciones CRUD sobre una base de datos no relacional.

---

## Objetivo

Definir un conjunto de reglas que permita:

* Insertar registros
* Consultar informacion
* Modificar datos existentes
* Eliminar registros

---

## Diseño

Se definio un lenguaje propio con las siguientes instrucciones:

* INSERTAR
* CONSULTAR
* MODIFICAR
* BORRAR

Cada instruccion trabaja sobre una coleccion identificada por un nombre.

Los registros se representan como listas de campos, donde cada campo es una asignacion de tipo clave = valor.

---

## Gramatica 

* INSERTAR coleccion ( campos )
* CONSULTAR coleccion DONDE condicion
* MODIFICAR coleccion DONDE condicion ( campos )
* BORRAR coleccion DONDE condicion

---

## Ejemplos

INSERTAR usuarios ( nombre = "Juan"; edad = 20 )

CONSULTAR usuarios DONDE edad > 18

MODIFICAR usuarios DONDE nombre = "Juan" ( edad = 21 )

BORRAR usuarios DONDE edad < 18


