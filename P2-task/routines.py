'''Retornar:
    - Autovalores e autovetores da matriz A
    - Possíveis erros de uso
    - Determinante quando solicitado
    - Número de iterações para convergência'''
import math


def metodo_potencia(matriz, n, tol):
    # ICOD == 1
    # x0 tem que ser solução do problema AX=lambdaX
    x0 = [1 for _ in range(n)]
    lambda0 = 1

    historico = []

    while True:
        # inicializar x1, ou Y (no slide)
        x1 = [0 for _ in range(n)]

        # Fazer a multiplicação Y = A.X0
        for i in range(n):
            for j in range(n):
                x1[i] += matriz[i][j] * x0[j]

        # Normalizar x1
        lambda1 = max(x1)
        for i in range(n):
            x1[i] = x1[i] / lambda1

        erro = residuo(lambda0, lambda1)
        historico.append(erro)

        if erro < tol:
            return x1, lambda1, historico

        x0 = x1[:]
        lambda0 = lambda1


def metodo_jacobi(matriz, n, tol):
    # ICOD == 2
    # Matriz A deve ser simétrica
    if not simetrica(matriz):
        return "Execução parada. Matriz deve ser simétrica."

    while True:
        # Achar o maior elemento de A, fora da diagonal principal
        maior = 0
        pos_maior = [0, 0]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if maior < abs(matriz[i][j]):
                    maior = abs(matriz[i][j])
                    pos_maior = [i, j]

        # Achar valor de phi
        if matriz[pos_maior[0]][pos_maior[0]] == matriz[pos_maior[1]][pos_maior[0]]:
            phi = math.pi / 4
        else:
            arctg_num = (2 * matriz[pos_maior[0]][pos_maior[1]])
            arctg_deno = matriz[pos_maior[0]][pos_maior[0]] - matriz[pos_maior[1]][pos_maior[1]]
            phi = (1 / 2) * math.atan(arctg_num / arctg_deno)

        # Seno e cosseno de phi
        sen = math.sin(phi)
        cos = math.cos(phi)

        #matriz[pos_maior[0]][pos_maior[0]] =
        #matriz[pos_maior[0]][pos_maior[1]] =
        #matriz[pos_maior[1]][pos_maior[0]] =
        #matriz[pos_maior[1]][pos_maior[1]] =


def residuo(lambda0, lambda1):
    return abs(lambda1 - lambda0) / abs(lambda1)


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


A = [[1, 0.2, 0], [0.2, 1, 0.5], [0, 0.5, 1]]
# print(metodo_potencia(A, 3, 0.0001))
print(metodo_jacobi(A, 3, 0.01))
