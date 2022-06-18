def avalia_dfy (indice, ksi, eta,cordenadas_x, NNE):

    import numpy
    from avalia_derivada_funcao_eta import avalia_derivada_funcao_eta
    from avalia_derivada_funcao_ksi import avalia_derivada_funcao_ksi

    derivada_psi_eta =numpy.zeros((NNE))
    derivada_psi_ksi =numpy.zeros((NNE))


 

    dfx = -avalia_derivada_funcao_ksi(indice,ksi,eta)*derivada_psi_eta + avalia_derivada_funcao_eta(indice,ksi,eta)*derivada_psi_ksi
    return(dfx)
