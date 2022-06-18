def calcula_termo_advectivo(cordenadas_x1, cordenadas_y1,vx,vy,NNE):
  import numpy
  from avalia_derivada_funcao_eta import avalia_derivada_funcao_eta
  from avalia_derivada_funcao_ksi import avalia_derivada_funcao_ksi
  from calcula_jacobinao import calcula_jacobinao
  from avalia_funcao import avalia_funcao
  
  raizes = numpy.zeros(5)
  pesos = numpy.zeros(5)
  matriz_adveccao_ksi = numpy.zeros((NNE,NNE))
  matriz_adveccao_eta = numpy.zeros((NNE,NNE))
  matriz_adveccao = numpy.zeros((NNE,NNE))
  
  #
  ax = 0.0
  bx = 1.0
  ay= 0.0
  

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


  for i in range(0,NNE):
        for j in range(0,NNE):
              
              #Inicio integração Gaussiana 
                h1= (bx-ax)*0.5
                h2 =(bx+ax)*0.5
                somatorio_integral_adveccao_fksi =0.0
                somatorio_integral_adveccao_feta =0.0


                for ig in range(0,npg):
                    integral_adveccao_funcao_ksi =0.0
                    integral_adveccao_funcao_eta =0.0

                    ksi =h1*raizes[ig]+h2
                    by = 1-ksi
                    k1 =(by-ay)*0.5
                    k2 = (by+ay)*0.5
                    for jg in range(0,npg):
                        eta =k1*raizes[jg]+k2
                       # Estamos calculando a integral de df_ksi
                        
                        jacobiano  = calcula_jacobinao(cordenadas_x1,cordenadas_y1,ksi, eta, NNE)
                        inv_jacobiano = float(1.0/jacobiano)
                        valor_adveccao_funcao_ksi = avalia_funcao(i,ksi,eta)*avalia_derivada_funcao_ksi(j,ksi,eta)*inv_jacobiano*jacobiano
                        integral_adveccao_funcao_ksi = integral_adveccao_funcao_ksi + pesos[jg]*valor_adveccao_funcao_ksi
                        
                        # Estamos calculando a integral de df_eta
                        valor_adveccao_funcao_eta = avalia_funcao(i,ksi,eta)*avalia_derivada_funcao_eta(j,ksi,eta)*inv_jacobiano*jacobiano
                        integral_adveccao_funcao_eta = integral_adveccao_funcao_eta + pesos[jg]*valor_adveccao_funcao_eta


                     # Estamos calculando a integral de df_ksi   
                    somatorio_integral_adveccao_fksi = somatorio_integral_adveccao_fksi +pesos[ig]*k1*integral_adveccao_funcao_ksi
                    somatorio_integral_adveccao_feta = somatorio_integral_adveccao_feta +pesos[ig]*k1*integral_adveccao_funcao_eta
                # Estamos calculando a integral de df_ksi
                somatorio_integral_adveccao_fksi = h1*somatorio_integral_adveccao_fksi 
                somatorio_integral_adveccao_feta = h1*somatorio_integral_adveccao_feta
                
                #Alocando em ksi
                matriz_adveccao_ksi[i][j] =vx*somatorio_integral_adveccao_fksi
               
                #Alocando em keta
                matriz_adveccao_eta[i][j] = vy*somatorio_integral_adveccao_feta
             


     
   
  
  return(matriz_adveccao_ksi, matriz_adveccao_eta )





  







