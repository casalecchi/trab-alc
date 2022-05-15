from ler_arquivo_3 import ler_arquivo


def escrever_saida(arq_saida, arq_entrada, y, tem_erro=False):
    with open(arq_saida, 'w') as saida:
        saida.write("DADOS de ENTRADA:\n")
        icod, n, pontos, x_estimar = ler_arquivo(arq_entrada)
        saida.write(f"ICOD = {icod}\n")
        saida.write(f"N = {n}\n")
        saida.write(f"PONTOS = {pontos}\n")
        saida.write(f"X = {x_estimar}\n")

        saida.write("DADOS DE SAÍDA:\n")
        if tem_erro:
            saida.write(f"Não foi possível estimar um valor para y.\n")
            saida.write(f"Erros de uso: {y}")
        else:
            saida.write(f"Valor estimado de y: {y}\n")
            saida.write(f"Erros de uso: Sem erro")
    saida.close()
