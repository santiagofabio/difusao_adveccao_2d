def imprime_matriz(matriz,nl, nc):

    for i in range (0,nl):
        for j in range(0, nc):
            print('{:.4f}  '.format(matriz[i][j]), end='')
        print()
    return(0)