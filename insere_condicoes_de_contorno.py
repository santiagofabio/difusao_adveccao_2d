def insere_condicoes_de_contorno(KGLOBAL_post,KGLOBAL_ant, vetor_independente,BCDNH,BCDH,NNEVT):

  #condicoes de contono NÂO HOMOGENEA
  print(f'Condicao de contorno nao homogenea')
  for linha in BCDNH :
         #Tratamento 1 linha global 
        linha = int(linha)
        print(f'{linha}')
        for j in range(0,NNEVT): 
              KGLOBAL_post[linha][j] =0.0
              KGLOBAL_ant[linha][j] =0.0
              
        KGLOBAL_post[linha][linha] =1.0
        KGLOBAL_ant[linha][linha] = 1.0
        vetor_independente[linha] = float (1.0)


      #condicoes de contono HOMOGENEA
  print(f'Condicao de contorno  homogenea')    
  for linha in BCDH:
        linha =int (linha) 
        print(f'{linha}')
        for j in range(0,NNEVT): 
              KGLOBAL_post[linha][j] =0.0
              KGLOBAL_ant[linha][j] =0.0


        KGLOBAL_post[linha][linha] =1.0
        KGLOBAL_ant[linha][linha] =1.0
        vetor_independente[linha] = float (0.0)

  return(KGLOBAL_post,KGLOBAL_ant,vetor_independente)