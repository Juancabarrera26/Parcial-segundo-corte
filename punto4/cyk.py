def cyk(cadena):
    n = len(cadena)
    tabla = [[set() for _ in range(n)] for _ in range(n)]

    # Reglas simples en CNF aproximada
    reglas = {
        'NUM': ['2', '3', '4', '5'],
        'E': [('E', 'PLUS'), ('T',)],
        'PLUS': [('+', 'T')],
        'T': [('T', 'MULT'), ('F',)],
        'MULT': [('*', 'F')],
        'F': [('NUM',)]
    }

    # Inicializacion
    for i in range(n):
        if cadena[i].isdigit():
            tabla[i][i].add('F')
            tabla[i][i].add('T')
            tabla[i][i].add('E')

    # Llenado simple
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                if 'E' in tabla[i][k] and 'E' in tabla[k + 1][j]:
                    tabla[i][j].add('E')

    return 'E' in tabla[0][n - 1]

print(cyk("23"))
