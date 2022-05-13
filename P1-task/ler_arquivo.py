import sys
import os


def ler_arquivo(file):
    with open(file, 'r') as f:
        N = int(f.readline())
        ICOD = int(f.readline())
        IDET = int(f.readline())
        A = list(eval(f.readline()))
        B = eval(f.readline())
        TOLm = float(f.readline())

    f.close()
    return N, ICOD, IDET, A, B, TOLm


print(ler_arquivo(sys.argv[1]))
