def monta_sistema_global(conectividade,K11_TORRE_ant,K11_TORRE_post,NNEV,NNEVT,NEFT): 
    #Importar os arquivos de malha
    import numpy as np
    from scipy.sparse import csc_matrix
    NNT =NNEV*NNEV*NEFT
    linha_global = np.array((NNT),dtype= int)   
    coluna_global = np.array((NNT), dtype= int )
    valores_post =np.array((NNT), dtype = np.longdouble)
    valores_ant =np.array((NNT), dtype = np.longdouble)

  
    

    contador  = 0
    for elemento in range(0,NEFT):
        
        for i_local in range(0,NNEV):
               
              for j_local in range(0,NNEV):
                  #Matriz global posterior

                     linha_global[contador] =int( conectividade[elemento][i_local]) 
                     coluna_global[contador] = int (conectividade[elemento][j_local]) 

                     valores_post[contador] =  (K11_TORRE_post[elemento][i_local][j_local] )
                     valores_ant[contador] =   (K11_TORRE_ant[elemento][i_local][j_local])

                     contador  = contador +1

    
    
    k11_global_post= csc_matrix((valores_post, (linha_global, coluna_global)), shape=(NNEVT, NNEVT))      
    k11_global_ant = csc_matrix ((valores_ant, (linha_global, coluna_global)), shape=(NNEVT, NNEVT) )      
                





                 
    return(k11_global_post,k11_global_ant)