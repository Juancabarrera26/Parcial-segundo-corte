def cyk(cadena):
    # reglas en forma simple
    reglas = [
        ('E', 'ET'),
        ('E', 'T'),
        ('T', 'TF'),
        ('T', 'F'),
        ('F', '(E)'),
        ('F', 'n')
    ]

    n = len(cadena)
    tabla = [[set() for _ in range(n)] for _ in range(n)]

    # inicializacion
    for i in range(n):
        if cadena[i].isdigit():
            tabla[i][i].add('F')

    # llenado
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                if 'F' in tabla[i][k] and 'F' in tabla[k + 1][j]:
                    tabla[i][j].add('T')

    return 'E' in tabla[0][n - 1]

print(cyk("23"))
