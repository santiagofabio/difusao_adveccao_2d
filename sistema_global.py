def monta_sub_matrizes_global(conectividade,k11_torre,k12_torre,k13_torre,k21_torre,k22_torre,k23_torre,k31_torre,k32_torre,NNEV,NNEP,NNEVT,NNEPT,NEFT):
    # Importar os arquivos de malha
    import numpy as np
    from scipy import sparse

    BCDNH =np.loadtxt('BCDNH.txt')
    BCDH =np.loadtxt('BCDH.txt')
    NV =3 

    #Linha 1  Matriz Global
    k11_global = np.zeros((NNEVT,NNEVT),  dtype=float)
    k12_global = np.zeros((NNEVT,NNEVT),  dtype=float)
    k13_global = np.zeros((NNEVT,NNEPT),  dtype=float)

    k21_global = np.zeros((NNEVT,NNEVT),  dtype=float)
    k22_global = np.zeros((NNEVT,NNEVT),  dtype=float)
    k23_global = np.zeros((NNEVT,NNEPT),  dtype=float)


    k31_global = np.zeros((NNEPT,NNEVT))
    k32_global = np.zeros((NNEPT,NNEVT))  

      
    for elemento in range(0,NEFT):
       # Preenchendo K11_Global
        for i_local in range(0,NNEV):
              for j_local in range(0,NNEV):
                 valor = k11_torre[elemento][i_local][j_local]
                 linha =int( conectividade[elemento][i_local]) -1
                 coluna = int (conectividade[elemento][j_local]) -1
                 k11_global[linha,coluna] = valor 
                


      # Preenchendo K12_Global
        for i_local in range(0,NNEV):
             for j_local in range(0,NNEV):

                  linha =int(conectividade[elemento][i_local]-1)
                  coluna= int( conectividade[elemento][j_local] -1)
                  valor = float(k12_torre[elemento][i_local][j_local])
                  k12_global[linha,coluna] = valor 
                  

              
                  linha = int (conectividade[elemento][i_local]-1)
                  coluna = int (conectividade[elemento][j_local] -1)
                  valor = float(k21_torre[elemento][i_local][j_local])
                  k21_global[linha,coluna] = valor 
                  

 
         
        for i_local in range(0,NNEV):
               for j_local in range(NNEP):
                  linha = int(conectividade[elemento][i_local] -1)
                  coluna = int (conectividade[elemento][j_local] -1)
                  valor = float(k13_torre[elemento][i_local][j_local])
                  k13_global[linha][coluna] =valor
                  

                  linha = int(conectividade[elemento][j_local]-1)
                  coluna = int(conectividade[elemento][i_local] -1)
                  valor = float(k31_torre[elemento][j_local][i_local])
                  k31_global[linha][coluna] =valor
                 
                  
        
        #k22_global
        for i_local in range(0,NNEV):
             for j_local in range(0,NNEV):
              linha = int(conectividade[elemento][i_local]-1)
              coluna = int(conectividade[elemento][j_local] -1)
              valor = float(k22_torre[elemento][i_local][j_local])
              k22_global[linha][coluna] = valor
              

        #K23  e K32  
        for i_local in range(0,NNEV):
               for j_local in range(0,NNEP):
                  linha = int(conectividade[elemento][i_local]-1)
                  coluna =int (conectividade[elemento][j_local] -1)
                  valor = float( k23_torre[elemento][i_local][j_local])
                  k23_global[linha][coluna] =valor
                 

                  linha =int ( conectividade[elemento][j_local]-1)
                  coluna = int(conectividade[elemento][i_local] -1)
                  k32_global[linha][coluna]=float(k32_torre[elemento][j_local][i_local])

   

   
                   
    return(k11_global,k12_global)