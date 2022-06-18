def avalia_derivada_funcao_eta (indice, ksi, eta):
  if  indice ==0 : #correto
     funcoes_0 = -3.0 +4*ksi +4*eta
     return(funcoes_0)

  elif indice ==1: #Correto
     funcoes_1 = 0.0
     return(funcoes_1)

  elif indice ==2: #Correto
     funcoes_2 = 4*eta-1.0
     return (funcoes_2)

  elif indice ==3: #Correto
     funcoes_3 =-4*ksi
     return (funcoes_3)

  elif indice ==4: #Correto
     funcoes_4 =4*ksi
     return (funcoes_4)

  elif indice ==5: #coreeto
     funcoes_5 =4-4*ksi-8*eta
     return (funcoes_5)
