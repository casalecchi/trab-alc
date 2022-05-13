# import numpy as np

# N = input("Ordem N do sistema de equações: ")
# ICOD = input("ICOD: ")
# IDET = input("IDET (0 calcula o determinante, maior que 0 não calcula): ")
A = [[3, -1, -1], [-1, 3, -1], [-1, -1, 3]]
# A = [[1, 0.2, 0.4], [0.2, 1, 0.5], [0.4, 0.5, 1]]
# A = [[1, 2, 2], [4, 4, 2], [4, 6, 4]]
# B = [3, 6, 10]
# B = [0.6, -0.3, -0.6]
B = [1, 2, 1]
# TOLm = input("Tolerância máxima: ")


def decomposicao_lu(matriz, b):
    # ICOD == 1
    for k in range(len(matriz)):
        for i in range(k + 1, len(matriz)):
            matriz[i][k] = matriz[i][k] / matriz[k][k]
        for j in range(k + 1, len(matriz)):
            for i in range(k + 1, len(matriz)):
                matriz[i][j] = matriz[i][j] - matriz[i][k] * matriz[k][j]

    # Modificamos o vetor B para se transformar em Y

    for i in range(1, len(matriz)):
        for j in range(i):
            b[i] -= (matriz[i][j] * b[j])

    # Modificar o vetor B para se transforar em X

    b[len(matriz) - 1] = b[len(matriz) - 1] / matriz[len(matriz) - 1][len(matriz) - 1]

    for i in range(len(matriz) - 2, -1, -1):
        for j in range(i + 1, len(matriz)):
            b[i] -= (matriz[i][j] * b[j])
        b[i] = b[i] / matriz[i][i]

    return b


def decomposicao_cholesky(matriz, b):
    # ICOD == 2
    # Matriz A precisa ser uma matriz simétrica positiva definida
    n = len(matriz)
    for i in range(n):
        for k in range(i):
            matriz[i][i] -= (matriz[i][k] ** 2)
        matriz[i][i] = matriz[i][i] ** (1/2)
        for j in range(i + 1, n):
            matriz[j][i] = matriz[i][j]
            for k in range(i):
                matriz[j][i] -= (matriz[i][k] * matriz[j][k])
            matriz[j][i] = matriz[j][i] / matriz[i][i]

    # Modificamos o vetor B para se transformar em Y
    b[0] = b[0] / matriz[0][0]

    for i in range(1, len(matriz)):
        for j in range(i):
            b[i] -= (matriz[i][j] * b[j])
        b[i] = b[i] / matriz[i][i]

    # Modificar o vetor B para se transforar em X

    b[len(matriz) - 1] = b[len(matriz) - 1] / matriz[len(matriz) - 1][len(matriz) - 1]

    for i in range(len(matriz) - 2, -1, -1):
        for j in range(i + 1, len(matriz)):
            b[i] -= (matriz[j][i] * b[j])  # Apenas modificamos o i com o j para pegar o elemento certo da matriz
        b[i] = b[i] / matriz[i][i]

    return b


def iterativo_jacobi(matriz, b, n, tol):
    # ICOD == 3
    # Matriz A deve ser diagonal dominante
    x0 = [1 for _ in range(n)]
    x1 = [0 for _ in range(n)]

    historico = []  # Lista que guardará o histórico dos erros

    while True:
        for i in range(n):
            x1[i] = b[i] / matriz[i][i]
            for j in range(n):
                if j == i:
                    continue
                x1[i] -= (matriz[i][j] * x0[j]) / matriz[i][i]

        erro = residuo(x0, x1, n)
        historico.append(erro)

        if erro < tol:
            break

        # Copia os elementos de x1 para x0
        x0 = x1[::1]

    return x1, x0, historico


def iterativo_gauss_seidel(matriz, b, n, tol):
    # ICOD == 4
    # Vale a mesma condição de convergência que Jacobi
    x0 = [1 for _ in range(n)]
    x1 = [0 for _ in range(n)]
    historico = []  # Lista que guardará o histórico dos erros

    while True:
        for i in range(n):
            x1[i] = b[i] / matriz[i][i]
            for j in range(i):
                x1[i] -= (matriz[i][j] * x1[j]) / matriz[i][i]
            for j in range(i + 1, n):
                x1[i] -= (matriz[i][j] * x0[j]) / matriz[i][i]

        erro = residuo(x0, x1, n)
        historico.append(erro)

        if erro < tol:
            return x0, x1, historico

        x0 = x1[::1]


def residuo(x0, x1, n):
    d = [0 for _ in range(n)]  # vetor auxiliar
    numerador = 0
    for i in range(n):
        d[i] = (x1[i] - x0[i]) ** 2
        numerador += d[i]
    numerador = numerador ** (1/2)

    denominador = 0
    for index, j in enumerate(x1):
        d[index] = j ** 2
        denominador += d[index]
    denominador = denominador ** (1/2)

    return numerador / denominador


print(iterativo_gauss_seidel(A, B, 3, 0.001))
