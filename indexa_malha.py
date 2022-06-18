def indexa_malha(matriz,BCDNH,BCDH):
    NTL, NTC = matriz.shape
    NNCDNH = len(BCDNH)
    NNCDH =len(BCDH)


    for linha in range(0,NTL):
        for coluna in range(0, NTC):
            matriz[linha][coluna] = matriz[linha][coluna]-1
           


    for i in range(0,NNCDNH):
        BCDNH[i] =BCDNH[i] -1

    
    for i in range(0,NNCDH):
        BCDH[i] =BCDH[i] -1

    return(matriz,BCDNH, BCDH)    


