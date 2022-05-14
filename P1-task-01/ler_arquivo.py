import sys
import os


def ler_arquivo(file):
    with open(file, 'r') as f:
        N = int(f.readline())
        ICOD = int(f.readline())
        IDET = int(f.readline())
        A = []
        for l in f.readlines():
            line = l.split()
            if len(line) == 1:
                TOLm = float(line[0])
                break
            for i in range(N):
                line[i] = float(line[i])
            A.append(line)
        B = A.pop(-1)

    f.close()
    return N, ICOD, IDET, A, B, TOLm


print(ler_arquivo(sys.argv[1]))
