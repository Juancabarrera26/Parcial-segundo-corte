pos = 0
tokens = []

def match(t):
    global pos
    if pos < len(tokens) and tokens[pos] == t:
        pos += 1
    else:
        raise Exception("Error de sintaxis")

def E():
    T()
    if pos < len(tokens) and tokens[pos] == '+':
        match('+')
        E()

def T():
    F()
    if pos < len(tokens) and tokens[pos] == '*':
        match('*')
        T()

def F():
    global pos
    if pos < len(tokens) and tokens[pos].isdigit():
        match(tokens[pos])
    elif pos < len(tokens) and tokens[pos] == '(':
        match('(')
        E()
        match(')')
    else:
        raise Exception("Error en F")

tokens = list("2+3")
E()

if pos == len(tokens):
    print("Cadena valida")
else:
    print("Error")
