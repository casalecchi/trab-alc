def decomposicao_lu(matriz, b, n):
    # ICOD == 1

    # Modificação da matriz A em LU, sem pivotamento
    for k in range(n):
        for i in range(k + 1, n):
            if matriz[k][k] == 0:
                return "Execução parada. Pivô nulo detectado, decomposição não é possível."
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


def decomposicao_cholesky(matriz, b, n):
    # ICOD == 2

    # Matriz A precisa ser uma matriz simétrica positiva definida
    if not simetrica(matriz):
        return "Execução parada. Matriz deve ser simétrica positiva definida"

    for i in range(n):
        for k in range(i):
            matriz[i][i] -= (matriz[i][k] ** 2)

        if matriz[i][i] <= 0:
            return "Execução parada. Matriz deve ser simétrica positiva definida"

        matriz[i][i] = matriz[i][i] ** (1/2)

        for j in range(i + 1, n):
            matriz[j][i] = matriz[i][j]
            for k in range(i):
                matriz[j][i] -= (matriz[i][k] * matriz[j][k])
            matriz[j][i] = matriz[j][i] / matriz[i][i]

    # Modificamos o vetor B para se transformar em Y
    b[0] = b[0] / matriz[0][0]

    for i in range(1, n):
        for j in range(i):
            b[i] -= (matriz[i][j] * b[j])
        b[i] = b[i] / matriz[i][i]

    # Modificar o vetor B para se transforar em X
    b[n - 1] = b[n - 1] / matriz[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            b[i] -= (matriz[j][i] * b[j])
        b[i] = b[i] / matriz[i][i]

    return b


def iterativo_jacobi(matriz, b, n, tol):
    # ICOD == 3

    # Matriz A deve ser diagonal dominante
    if not diagonal_dominante(matriz):
        return 0, 0, "Execução parada. Matriz deve ser diagonal dominante."

    # Inicializar x0 e x1
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
            num_iter = len(historico)
            return x1, historico, num_iter

        # Copia os elementos de x1 para x0
        x0 = x1[:]


def iterativo_gauss_seidel(matriz, b, n, tol):
    # ICOD == 4

    # Vale a mesma condição de convergência que Jacobi
    if not diagonal_dominante(matriz):
        return 0, 0, "Execução parada. Matriz deve ser diagonal dominante."

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
            num_iter = len(historico)
            return x1, historico, num_iter

        x0 = x1[:]


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


def simetrica(matriz):
    n = len(matriz)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if matriz[i][j] != matriz[j][i]:
                # Não é simétrica
                return False
    return True


def diagonal_dominante(matriz):
    n = len(matriz)
    for i in range(n):
        soma_linha = 0
        soma_coluna = 0
        for j in range(n):
            if i == j:
                continue
            soma_linha += abs(matriz[i][j])
            soma_coluna += abs(matriz[j][i])
        if abs(matriz[i][i]) < soma_coluna or abs(matriz[i][i]) < soma_coluna:
            return False
    return True
