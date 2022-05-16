from ler_arquivo_2 import ler_arquivo


def escrever_saida(arq_saida, arq_entrada, autovalores, autovetores, determinante, num_iter, calculou_det=False, tem_erro=False, erro="Sem erro"):
    with open(arq_saida, 'w') as saida:
        saida.write("DADOS de ENTRADA:\n")
        n, icod, idet, _, tolm = ler_arquivo(arq_entrada)
        saida.write(f"ICOD = {icod}\n")
        saida.write(f"N = {n}\n")
        saida.write(f"IDET = {idet}\n")
        saida.write(f"TOLm = {tolm}\n")

        saida.write("DADOS DE SAÍDA:\n")
        if not tem_erro:
            for index, autovetor in enumerate(autovetores):
                try:
                    saida.write(f"Autovalor(es) da matriz A: {autovalores[index]} -> ")
                except TypeError:
                    saida.write(f"Autovalor(es) da matriz A: {autovalores} -> ")
                saida.write(f"Autovetor(es) associado: {autovetor}\n")
            saida.write(f"Número de iterações: {num_iter}\n")
        else:
            determinante = "Não foi possível calcular."
        if calculou_det and type(determinante) == str:
            saida.write(f"Erros de uso (determinante): Não foi possível calcular o determinante.\n")
        elif calculou_det:
            saida.write(f"Determinante da matriz A: {determinante}\n")
        saida.write(f"Erros de uso: {erro}\n")
    saida.close()
