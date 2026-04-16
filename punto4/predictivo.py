pos = 0
tokens = []

def match(t):
    global pos
    if pos < len(tokens) and tokens[pos] == t:
        pos += 1
    else:
        raise Exception("Error")

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
    if tokens[pos].isdigit():
        match(tokens[pos])
    elif tokens[pos] == '(':
        match('(')
        E()
        match(')')
      
tokens = list("2+3")
E()
print("Cadena valida")
