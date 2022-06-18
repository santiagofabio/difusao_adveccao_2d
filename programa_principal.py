import sys
import os
from time import process_time_ns
import time 
import numpy
from resolve_difusao import resolve_difusao
from imprime_matriz import imprime_matriz
from monta_sistema_global import monta_sistema_global
from insere_condicoes_de_contorno import insere_condicoes_de_contorno 
from calcula_termo_advectivo import calcula_termo_advectivo
from calcula_termo_decaimento import calcula_termo_decaimento
import matplotlib.pyplot as plt 
from indexa_malha import indexa_malha
from scipy.linalg import lu
from scipy import linalg

os.system('cls')



print("****INICIO EXECUSSAO*****")





# Parametroz fisicos
alpha =float(1.5)
vx = float(0.01)
vy = float(0.01)
delta = float(0.001)


#Importacao das malhas de calculo
MATRIZ =numpy.loadtxt('DOMINIO.txt')
BCDNH =numpy.loadtxt('BCDNH.txt')
BCDH =numpy.loadtxt('BCDH.txt')
coordenadas = numpy.loadtxt('coordenadas.txt')

cordenadas_x = coordenadas[:,0]
cordenadas_y = coordenadas[:,1]
MATRIZ,BCDNH,BCDH = indexa_malha(MATRIZ,BCDNH,BCDH )

#Dimesnoes do Sistema Global
NEFT, NNEV = MATRIZ.shape
NNEVT =len(cordenadas_x)

print(NEFT)
# Torres de paralelizacao
K11_TORRE_post =numpy.zeros((NEFT,NNEV,NNEV))
K11_TORRE_ant =numpy.zeros((NEFT,NNEV,NNEV))


# Constantes método de Cranck  Nicolson

dt =0.05
#Tempo posterior
const_post__decaimento =float( 1.0 + delta*dt*0.5)
const_post__difusao = float(alpha*dt*0.5)
const_post_adv_vx = float( vx*dt*0.5)
const_post_adv_vy = float( vy*dt*0.5)

#Tempo anterior
const_ant__decaimento =float( 1.0 - delta*dt*0.5)
const_ant__difusao = float( - alpha*dt*0.5)
const_ant_adv_vx = float( -vx*dt*0.5)
const_ant_adv_vy = float( -vy*dt*0.5)






# inicio do calculos sobre a malha
for elemento in range(0,NEFT):  
    print(f'Elmento {elemento} , Restam {NEFT-elemento}' )
    k_elemento_difusao = resolve_difusao(elemento,MATRIZ,cordenadas_x, cordenadas_y,NNEV)
    k_elemento_advecao_vx,k_elemento_advecao_vy  = calcula_termo_advectivo(cordenadas_x, cordenadas_y,vx,vy,NNEV)
    k_elemento_decaimento = calcula_termo_decaimento(cordenadas_x,cordenadas_y,NNEV)

    
    for i_local in range(0,NNEV):
        for j_local in range(0,NNEV):
             #Aloca  torre posterior
             K11_TORRE_post[elemento][i_local][j_local] =  const_post__decaimento*k_elemento_decaimento[i_local][j_local] +const_post__difusao*k_elemento_difusao[i_local][j_local] +const_post_adv_vx *k_elemento_advecao_vx[i_local][j_local] + const_post_adv_vy*k_elemento_advecao_vy[i_local][j_local] 
             K11_TORRE_ant[elemento][i_local][j_local] =   const_ant__decaimento*k_elemento_decaimento[i_local][j_local]  +const_ant__difusao*k_elemento_difusao[i_local][j_local] +  const_ant_adv_vx*k_elemento_advecao_vx[i_local][j_local] + const_ant_adv_vy*k_elemento_advecao_vy[i_local][j_local] 


            
                                                                                                                                                                   




#MOntagem do sistema global
KGLOBAL_post,KGLOBAL_ant = monta_sistema_global(MATRIZ,K11_TORRE_ant,K11_TORRE_post,NNEV,NNEVT,NEFT)

VETOR_B = numpy.zeros((NNEVT),  dtype=float)

KGLOBAL_post, KGLOBAL_ant, VETOR_B = insere_condicoes_de_contorno(KGLOBAL_post,KGLOBAL_ant,VETOR_B, BCDNH,BCDH,NNEVT)



#Iteração no tempo
solucao_anterior = numpy.zeros(NNEVT)
solucao_anterior = VETOR_B 



tempo_max = 10.0
tempo =0.0
contador = int(0)

P,L,U = lu(KGLOBAL_post)
while (tempo<=tempo_max):

      vetor_independente = KGLOBAL_ant.dot(solucao_anterior)
      
      vetor_independente =P.dot(vetor_independente)
      y = linalg.solve(L,vetor_independente)
      x_posterior =linalg.solve(U,y)
      
      contador =contador+1
      tempo = dt*contador
      print(tempo)
      solucao_anterior = x_posterior


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') 
ax.plot_trisurf(cordenadas_x, cordenadas_y, x_posterior)
plt.show()
