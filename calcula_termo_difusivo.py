def calcula_termo_difusivo(cordenadas_x,cordenadas_y,NNE):
  import numpy
  from avalia_derivada_funcao_eta import avalia_derivada_funcao_eta
  from avalia_derivada_funcao_ksi import avalia_derivada_funcao_ksi
  from calcula_derivadas_locais import calcula_derivadas_locais
  from  calcula_jacobinao import calcula_jacobinao
  
   
  raizes = numpy.zeros(5)
  pesos = numpy.zeros(5)
  matriz_difusao_ksi = numpy.zeros((NNE,NNE))
  matriz_difusao_eta = numpy.zeros((NNE,NNE))


  npg =5

  #raizes do método de Gauss
  raizes[0]= 0.9061798459
  raizes[1]= 0.5384693101
  raizes[2]=0.0
  raizes[3]= -0.5384693101
  raizes[4]= -0.9061798459
    

    #pesos método de Gausss

  pesos[0]=0.2369268850 
  pesos[1]=0.4786286705
  pesos[2]=0.5688888889
  pesos[3]=0.4786286705
  pesos[4]=0.2369268850 



 
  # Intervalo de integraçao
  ax = 0.0
  bx = 1.0
  ay = 0.0
  


  for i in range(0,NNE):
        for j in range(i,NNE):
              
              #Inicio integração Gaussiana 
                h1= (bx-ax)*0.5
                h2 =(bx+ax)*0.5
                somatorio_integral_derivada_fksi =0.0
                somatorio_integral_derivada_feta =0.0
               
                for ig in range(0,npg):
                    integral_derivada_funcao_ksi =0.0
                    integral_derivada_funcao_eta =0.0
                    
                    ksi =h1*raizes[ig]+ h2
                    by = 1-ksi
                    k1 =(by-ay)*0.5
                    k2 = (by+ay)*0.5
                    
                      
                             
                    
                    
                    for jg in range(0,npg):
                            eta =k1*raizes[jg]+k2  
                                      
                             
                            [x_dpsi_dksi,x_dpsi_deta,y_dpsi_dksi,y_dpsi_deta ] = calcula_derivadas_locais(cordenadas_x,cordenadas_y,ksi, eta, NNE)
                            jacobiano  = abs(y_dpsi_deta*x_dpsi_dksi- y_dpsi_dksi*x_dpsi_deta)
                            inv_jacobiano = 1.0/jacobiano

                            
                        
                            #Estamos calculando a integral de df_ksi
                            dfdx_i =avalia_derivada_funcao_ksi(i,ksi,eta)*y_dpsi_deta   -avalia_derivada_funcao_eta(i,ksi,eta)*y_dpsi_dksi
                            dfdx_j =avalia_derivada_funcao_ksi(j,ksi,eta)*y_dpsi_deta -avalia_derivada_funcao_eta(j,ksi,eta)*y_dpsi_dksi
                            
                            valor_derivada_funcao_ksi = (dfdx_i* dfdx_j)*inv_jacobiano
                            integral_derivada_funcao_ksi = integral_derivada_funcao_ksi + pesos[jg]*valor_derivada_funcao_ksi
                        
                           # Estamos calculando a integral de df_eta
                            dfdy_i =-avalia_derivada_funcao_ksi(i,ksi,eta)*x_dpsi_deta +avalia_derivada_funcao_eta(i,ksi,eta)*x_dpsi_dksi
                            dfdy_j =-avalia_derivada_funcao_ksi(j,ksi,eta)*x_dpsi_deta +avalia_derivada_funcao_eta(j,ksi,eta)*x_dpsi_dksi
                            valor_derivada_funcao_eta =dfdy_i*dfdy_j*inv_jacobiano 
                            integral_derivada_funcao_eta = integral_derivada_funcao_eta + pesos[jg]*valor_derivada_funcao_eta


                     # Estamos calculando a integral de df_ksi   
                    somatorio_integral_derivada_fksi = somatorio_integral_derivada_fksi +pesos[ig]*k1*integral_derivada_funcao_ksi
                    somatorio_integral_derivada_feta = somatorio_integral_derivada_feta +pesos[ig]*k1*integral_derivada_funcao_eta
                # Estamos calculando a integral de df_ksi
                somatorio_integral_derivada_fksi = h1*somatorio_integral_derivada_fksi 
                somatorio_integral_derivada_feta = h1*somatorio_integral_derivada_feta
                
                #Alocando em ksi
                matriz_difusao_ksi[i][j] =somatorio_integral_derivada_fksi
                matriz_difusao_ksi[j][i] =matriz_difusao_ksi[i][j]
                #Alocando em keta
                matriz_difusao_eta[i][j] =somatorio_integral_derivada_feta
                matriz_difusao_eta[j][i] =matriz_difusao_eta[i][j]


                
   
  return(matriz_difusao_ksi, matriz_difusao_eta )





  







