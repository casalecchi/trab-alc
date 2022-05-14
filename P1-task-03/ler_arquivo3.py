import sys


def ler_arquivo3(file):
    with open(file, 'r') as f:
        ICOD = int(f.readline())
        N = int(f.readline())
        coordenadas = []
        for line in f.readlines():
            coordenada = line.split()
            if len(coordenada) < 2:
                x_estimar = float(line)
                break
            coordenada = [float(coordenada[0]), float(coordenada[1])]
            coordenadas.append(coordenada)


        return ICOD, N, coordenadas, x_estimar


print(ler_arquivo3(sys.argv[1]))