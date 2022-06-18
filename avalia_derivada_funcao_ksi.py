def avalia_derivada_funcao_ksi (indice, ksi, eta):

 if  indice ==0 : #correto
     funcoes_0 = -3.0 +4*ksi +4*eta
     return(funcoes_0)

 elif indice ==1: #Correto
     funcoes_1 = 4*ksi-1.0
     return(funcoes_1)

 elif indice ==2: #Correto
     funcoes_2 =0.0
     return (funcoes_2)

 elif indice ==3: #Correto
     funcoes_3 =-8*ksi + 4-4*eta
     return (funcoes_3)

 elif indice ==4: #Correto
     funcoes_4 =4*eta
     return (funcoes_4)

 elif indice ==5: #coreeto
     funcoes_5 =-4*eta 
     return (funcoes_5)

 