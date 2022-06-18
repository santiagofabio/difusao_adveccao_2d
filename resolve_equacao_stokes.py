def resolve_difusao (elemento,matriz_conectividade,cordenadas_x, cordenadas_y,alpha,NNEV,NNEP,k11_torre,k12_torre,k13_torre,k21_torre,k22_torre,k23_torre,k31_torre,k32_torre ):
                           
    import math 
    import numpy
    from calcula_termo_difusivo import calcula_termo_difusivo
    from avalia_funcao import avalia_funcao
   
    #Coordenadas elementos de velocidade
    elemento_coord_x = numpy.zeros(NNEV)
    elemento_coord_y = numpy.zeros(NNEV)


    


    for  i in range(0,NNEV):
        no = int(matriz_conectividade[elemento,i]) 
      
        
        elemento_coord_x[i]= float(cordenadas_x[no])
        elemento_coord_y[i]= float(cordenadas_y[no])



    
    matriz_difusivo_ksi,matriz_difusivo_eta = calcula_termo_difusivo( elemento_coord_x, elemento_coord_y,NNEV, NNEV, NNEV)
    k11_torre[elemento, : ,: ] = alpha*matriz_difusivo_ksi + alpha*matriz_difusivo_eta

    

    return(k11_torre)












    
   
   
   
   
   
   
   
  
