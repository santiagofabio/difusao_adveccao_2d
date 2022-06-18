def calcula_termo_decaimento (cordenadas_x1,cordenadas_y1,NNE):
    import numpy
    from avalia_funcao import avalia_funcao
    from calcula_jacobinao import  calcula_jacobinao
    from  avalia_derivada_funcao_eta import avalia_derivada_funcao_eta
    from  avalia_derivada_funcao_ksi import avalia_derivada_funcao_ksi
    
    raizes = numpy.zeros(5)
    pesos = numpy.zeros(5)
    matriz_decaimento = numpy.zeros((NNE,NNE))
    npg =5
    #raizes do método de Gauss
    raizes[0]=0.9061798459
    raizes[1]=0.5384693101
    raizes[2]=0.0
    raizes[3]= -0.5384693101
    raizes[4]= -0.9061798459
    

    #pesos método de Gausss

    pesos[0]=0.2369268850 
    pesos[1]=0.4786286705
    pesos[2]=0.5688888889
    pesos[3]=0.4786286705
    pesos[4]=0.2369268850

    ax =0.0
    bx= 1.0
    ay = 0.0

    

    for i in range(0,NNE):
        for j in range(0,NNE):

              #Inicio integração Gaussiana 
                h1= (bx-ax)*0.5
                h2 =(bx+ax)*0.5
                somatorio_integral =0.0
               
               
                
                for ig in range(0,npg):
                    integral_x =0.0
                    ksi =h1*raizes[ig]+h2
                    by =  1.0 -ksi
                   
                    k1 =(by-ay)*0.5
                    k2 = (by+ay)*0.5

                    

                   
                    for jg in range(0,npg):
                        eta =k1*raizes[jg]+k2
                        jacobiano  = calcula_jacobinao(cordenadas_x1,cordenadas_y1,ksi, eta, NNE)
                        valor_funcao = avalia_funcao(i,ksi,eta)*avalia_funcao(j,ksi,eta)*jacobiano
                        #valor_funcao =ksi*eta
                        integral_x = integral_x + pesos[jg]*valor_funcao


                    somatorio_integral = somatorio_integral +pesos[ig]*k1*integral_x
                somatorio_integral = h1*somatorio_integral 
                
                matriz_decaimento[i][j] = somatorio_integral      

            
    return(matriz_decaimento) 