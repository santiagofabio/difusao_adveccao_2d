def calcula_jacobinao(cordenadas_x,cordenadas_y,ksi, eta, NNE):
    from avalia_derivada_funcao_eta import avalia_derivada_funcao_eta
    from avalia_derivada_funcao_ksi import avalia_derivada_funcao_ksi

    y_dpsi_deta =0.0
    y_dpsi_dksi =0.0
    x_dpsi_deta =0.0
    x_dpsi_dksi =0.0

  
    for ie in range(0,NNE):
        #Calculos em Y  
        y_dpsi_deta = y_dpsi_deta+  cordenadas_y[ie]*avalia_derivada_funcao_eta(ie,ksi,eta)
        y_dpsi_dksi = y_dpsi_dksi +  cordenadas_y[ie]*avalia_derivada_funcao_ksi(ie,ksi,eta)
        #Calculos em X
        x_dpsi_deta = x_dpsi_deta +  cordenadas_x[ie]*avalia_derivada_funcao_eta(ie,ksi,eta)
        x_dpsi_dksi = x_dpsi_dksi +  cordenadas_x[ie]*avalia_derivada_funcao_ksi(ie,ksi,eta)
            
    
    jacobiano  = abs(y_dpsi_deta*x_dpsi_dksi- y_dpsi_dksi*x_dpsi_deta)
    return(jacobiano)


