import sys
from ler_arquivo_2 import ler_arquivo
from escrever_saida_2 import escrever_saida
from routines_2 import metodo_potencia, metodo_jacobi, determinante_jacobi


def preparo_jacobi(matriz, n, tol, idet):
    m_lambda, m_x, num_iter = metodo_jacobi(matriz, n, tol)
    if type(num_iter) == str:
        return 0, 0, 0, num_iter
    autovalores = []
    autovetores = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                autovalores.append(round(m_lambda[i][j], 4))
            autovetores[j].append(round(m_x[i][j], 4))

    determinante = False
    if idet > 0:
        determinante = determinante_jacobi(m_lambda, n)

    return autovalores, autovetores, determinante, num_iter


n, icod, idet, matriz, tol = ler_arquivo(sys.argv[1])
calculou_det = True if idet > 0 else False
if icod == 1:
    x1, lambda1, num_iter = metodo_potencia(matriz, n, tol)
    tem_erro = False
    erro = "Sem erro"
    if type(num_iter) == str:
        tem_erro = True
        erro = num_iter
    det = "Não é possível calulcar o determinante."
    escrever_saida("saida.txt", sys.argv[1], lambda1, [x1], det, num_iter, calculou_det, tem_erro, erro)
elif icod == 2:
    autovalores, autovetores, determinante, num_iter = preparo_jacobi(matriz, n, tol, idet)
    tem_erro = False
    erro = "Sem erro"
    if type(num_iter) == str:
        tem_erro = True
        erro = num_iter
    escrever_saida("saida.txt", sys.argv[1], autovalores, autovetores, determinante,
                   num_iter, calculou_det, tem_erro, erro)
else:
    print("ICOD inválido.")
