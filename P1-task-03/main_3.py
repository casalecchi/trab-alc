import sys
from ler_arquivo_3 import ler_arquivo
from escrever_saida_3 import escrever_saida
from routines_3 import regressao, interpolacao

icod, n, pontos, x_estimar = ler_arquivo(sys.argv[1])
if icod == 1:
    y = interpolacao(pontos, n, x_estimar)
    tem_erro = True if type(y) == str else False
    escrever_saida("saida.txt", sys.argv[1], y, tem_erro)
elif icod == 2:
    y = regressao(pontos, n, x_estimar)
    tem_erro = True if type(y) == str else False
    escrever_saida("saida.txt", sys.argv[1], y, tem_erro)
else:
    print("ICOD inválido.")
