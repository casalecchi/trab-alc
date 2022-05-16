import sys
from escrever_saida import escrever_saida
from ler_arquivo import ler_arquivo
from routines import decomposicao_lu, decomposicao_cholesky, iterativo_jacobi, iterativo_gauss_seidel


n, icod, idet, A, B, tol = ler_arquivo(sys.argv[1])
calculou_det = True if idet > 0 else False
if icod == 1:
    x = decomposicao_lu(A, B, n)
    tem_erro = True if type(x) == str else False
    erro = x if tem_erro else "Sem erro"
    escrever_saida("saida.txt", sys.argv[1], x, False, 0, [], tem_erro, calculou_det, erro)

elif icod == 2:
    x = decomposicao_cholesky(A, B, n)
    tem_erro = True if type(x) == str else False
    erro = x if tem_erro else "Sem erro"
    escrever_saida("saida.txt", sys.argv[1], x, False, 0, [], tem_erro, calculou_det, erro)

elif icod == 3:
    x, historico, num_iter = iterativo_jacobi(A, B, n, tol)
    tem_erro = True if type(num_iter) == str else False
    erro = num_iter if tem_erro else "Sem erro"
    escrever_saida("saida.txt", sys.argv[1], x, True, num_iter, historico, tem_erro, calculou_det, erro)

elif icod == 4:
    x, historico, num_iter = iterativo_gauss_seidel(A, B, n, tol)
    tem_erro = True if type(num_iter) == str else False
    erro = num_iter if tem_erro else "Sem erro"
    escrever_saida("saida.txt", sys.argv[1], x, True, num_iter, historico, tem_erro, calculou_det, erro)

else:
    print("ICOD inválido.")
