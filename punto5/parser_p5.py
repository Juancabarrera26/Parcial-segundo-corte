def tokenize(cadena):
    tokens = []
    partes = cadena.replace("(", " ( ").replace(")", " ) ").split()

    for p in partes:
        if p == "if":
            tokens.append("if")
        elif p == "then":
            tokens.append("then")
        elif p == "else":
            tokens.append("else")
        elif p == "=":
            tokens.append("=")
        elif p.isdigit():
            tokens.append("NUM")
        else:
            tokens.append("ID")

    return tokens


# Variables globales
tokens = []
pos = 0


# Algoritmo de emparejamiento
def match(t):
    global pos
    if pos < len(tokens) and tokens[pos] == t:
        pos += 1
    else:
        raise Exception("Error de sintaxis en posicion " + str(pos))


# Reglas del parser

def programa():
    sentencia()
    while pos < len(tokens):
        sentencia()


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
    elif tokens[pos] == "NUM":
        match("NUM")
    else:
        raise Exception("Error en expresion")


# Funcion principal para probar
def ejecutar(cadena):
    global tokens, pos
    tokens = tokenize(cadena)
    pos = 0

    try:
        programa()
        if pos == len(tokens):
            print("Cadena valida")
        else:
            print("Error: tokens sobrantes")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    print("Ejemplo 1:")
    ejecutar("x = 5")

    print("Ejemplo 2:")
    ejecutar("if x then y = 5 else y = 10")

    print("Ejemplo 3:")
    ejecutar("if x then if y then z = 1 else z = 2")
