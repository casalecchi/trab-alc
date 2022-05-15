def interpolacao(pontos, n, x_estimar):
    # ICOD == 1
    fx = 0
    x = []
    y = []
    for ponto in pontos:
        x.append(ponto[0])
        y.append(ponto[1])

    for i in range(n):
        termo = y[i]
        for j in range(n):
            if i == j:
                continue
            termo *= (x_estimar - x[j]) / (x[i] - x[j])
        fx += termo
    return fx


def regressao(pontos, n, x):
    # ICOD == 2
    # y = b0 + b1x
    A = [[n, 0], [0, 0]]
    C = [0, 0]
    for i in range(n):
        A[0][1] += pontos[i][0]
        A[1][0] += pontos[i][0]
        A[1][1] += (pontos[i][0]) ** 2
        C[0] += pontos[i][1]
        C[1] += pontos[i][0] * pontos[i][1]

    B = decomposicao_lu(A, C, 2)
    if type(B) == str:
        return B

    return B[0] + x * B[1]


def decomposicao_lu(matriz, b, n):
    # ICOD == 1
    # Modificação da matriz A em LU, sem pivotamento
    for k in range(n):
        for i in range(k + 1, n):
            if matriz[k][k] == 0:
                return "Execução parada. Pivô nulo detectado."
            matriz[i][k] = matriz[i][k] / matriz[k][k]
        for j in range(k + 1, n):
            for i in range(k + 1, n):
                matriz[i][j] -= (matriz[i][k] * matriz[k][j])

    # Modificamos o vetor B para se transformar em Y

    for i in range(1, n):
        for j in range(i):
            b[i] -= (matriz[i][j] * b[j])

    # Modificar o vetor B para se transforar em X

    b[n - 1] = b[n - 1] / matriz[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            b[i] -= (matriz[i][j] * b[j])
        b[i] = b[i] / matriz[i][i]

    return b


print(regressao([[1.0, 2.0], [2.5, 3.5], [4.0, 8.0]], 3, 3.25))

