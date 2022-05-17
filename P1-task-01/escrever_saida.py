from ler_arquivo import ler_arquivo


def escrever_saida(arq_saida, arq_entrada, x, met_iter, num_iter, historico, tem_erro, calculou_det, erro):
    with open(arq_saida, 'w') as saida:
        saida.write("DADOS de ENTRADA:\n")
        n, icod, idet, A, B, tolm = ler_arquivo(arq_entrada)
        saida.write(f"N = {n}\n")
        saida.write(f"ICOD = {icod}\n")
        saida.write(f"IDET = {idet}\n")
        saida.write(f"TOLm = {tolm}\n")

        saida.write("DADOS DE SAÍDA:\n")
        if not tem_erro:
            saida.write(f"Solução do sistema X: {x}\n")
            if met_iter:
                saida.write(f"Número de iterações: {num_iter}\n")
                saida.write(f"Histórico de erros: {historico}\n")
        if calculou_det:
            saida.write(f"Erros de uso (determinante): Não foi possível calcular o determinante.\n")
        saida.write(f"Erros de uso: {erro}\n")
    saida.close()
