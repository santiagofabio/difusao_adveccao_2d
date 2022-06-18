def avalia_funcao_ordem_um(indice, ksi, eta):

  if indice == 0:
     f0 = 1 -ksi-eta
     
     return(f0)
  if indice ==1:
      f1 = ksi
      
      return(f1)
  if  indice == 2:
      f2 =  eta
      
      return(f2)
  



