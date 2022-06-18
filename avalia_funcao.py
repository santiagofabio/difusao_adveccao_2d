def avalia_funcao (indice, ksi, eta):
 if  indice ==0 :
     funcoes_0 = 2*(1-ksi-eta)*(1-ksi-eta-0.5)
     return(funcoes_0)

 if indice == 1:
     funcoes_1 = 2*(ksi)*(ksi-0.5)
     return(funcoes_1)

 if indice == 2:
     funcoes_2 =2*eta*(eta-0.5)
     return(funcoes_2)

 if indice ==3:
    funcoes_3 = 4*(1-ksi-eta)*ksi
    return (funcoes_3)

 if indice ==4:
      funcoes_4 = 4*ksi*eta
      return(funcoes_4)

 if indice ==5:
     funcoes_5 =4*eta*(1-ksi-eta)
     return(funcoes_5)

