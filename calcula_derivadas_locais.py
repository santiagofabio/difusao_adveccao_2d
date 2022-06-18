def calcula_derivadas_locais (cordenadas_x,cordenadas_y,ksi, eta, NNE):
 import numpy
 from avalia_derivada_funcao_eta import avalia_derivada_funcao_eta
 from avalia_derivada_funcao_ksi import avalia_derivada_funcao_ksi

 x_dpsi_dksi = 0.0
 x_dpsi_deta = 0.0
 y_dpsi_dksi = 0.0
 y_dpsi_deta = 0.0
 for  ie in range(0, NNE):
     x_dpsi_dksi =  x_dpsi_dksi + cordenadas_x[ie] *avalia_derivada_funcao_ksi(ie,ksi,eta)
     x_dpsi_deta = x_dpsi_deta +  cordenadas_x[ie]*avalia_derivada_funcao_eta(ie,ksi,eta)
     y_dpsi_dksi = y_dpsi_dksi + cordenadas_y[ie]*avalia_derivada_funcao_ksi(ie,ksi,eta)
     y_dpsi_deta = y_dpsi_deta +  cordenadas_y[ie]*avalia_derivada_funcao_eta(ie,ksi,eta)
     
 return(x_dpsi_dksi,x_dpsi_deta,y_dpsi_dksi,y_dpsi_deta)
