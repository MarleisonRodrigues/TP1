
from collections import deque


#Classe Nó
class Node:
    def __init__(self):
       self.tabuleiro = []

class Pilha:
    """Esta classe representa uma pilha usando uma estrutura encadeada."""

    def __init__(self):
        self.topo = None


    def __repr__(self):
        return "[" + str(self.topo) + "]"
    
#Realizar os movimentos no tabuleiro     
def move(tab_original):

    """
    Checa possíveis movimentos (os nós)
    da árvore
    """
    movimentos = []
    tab = eval(tab_original) #comparar os dois tabuleiro, atual com o final 
    i = 0
    j = 0
    
    while 0 not in tab[i]: i += 1 #enquanto espaço em branco não estiver no objetivo
    j = tab[i].index(0)

    
    if i<2:         #mover o 0 para baixo  
        tab[i][j], tab[i+1][j] = tab[i+1][j], tab[i][j]   # Troca elemento de lugar com o pai.
        movimentos.append(str(tab))
        tab[i][j], tab[i+1][j] = tab[i+1][j], tab[i][j]
        

    if i>0:         #mover o 0 para cima
        tab[i][j], tab[i-1][j] = tab[i-1][j], tab[i][j] 
        movimentos.append(str(tab))
        tab[i][j], tab[i-1][j] = tab[i-1][j], tab[i][j]  
        

    if j<2:         #mover o 0 para a direita
        tab[i][j], tab[i][j+1] = tab[i][j+1], tab[i][j] 
        movimentos.append(str(tab))
        tab[i][j], tab[i][j+1] = tab[i][j+1], tab[i][j]
        

    if j>0:         #mover o 0 para a esquerda
        tab[i][j], tab[i][j-1] = tab[i][j-1], tab[i][j] 
        movimentos.append(str(tab))
        tab[i][j], tab[i][j-1] = tab[i][j-1], tab[i][j]
      
    return movimentos


#Algoritmo de Busca em Largura 
def buscaLargura(start,end):
    
    explorado = [] 
    fila = [[start]] 

    #Estrutura de repetição
    while fila: #enquanto a fila não for vazia
        i = 0
        caminho = fila[i] 
    
        #Fatiamento de Listas
        fila = fila[:i] + fila[i+1:] 
        final = caminho[-1] 

        if final in explorado: 
            continue
       
        #Não sendo objetivo Gero seus sucessores 
        for movimento in move(final): #Chamando a função para gerar os sucessores realizando os movimento
            
            if movimento in explorado:
                continue
            fila.append(caminho + [movimento]) 
        explorado.append(final) 

        if final == end: break 

    print('\nNós expandidos: ', (len(explorado)-1))
    print('\nMovimentos da solução da busca em largura:')
    print()
    return caminho

#Método de Busca em Profundidade Limitada
#Definindo o limite do nós da profundidade como 25 para que consiga 
#alcançar a solução para o problema
def buscaProfundidadeLimitada(start, end, limite):

    explorado = [] 
    pilha = [[start]]  

    #Estrutura de repetição
    while len(pilha)>0: 

        i=0
        caminho = pilha[i]  

        #Fatiamento de Listas
        pilha = pilha[:i] + pilha[i+1:] 

        final = caminho[-1] 

        if final in explorado:  
            continue
        
        #Gerar os sucessores
        for movimento in move(final): #chamando a função sucessor que realiza os movimentos 

            if movimento in explorado:
                continue

            pilha.append(caminho + [movimento]) 
        explorado.append(final) 
        
        #Uma forma para garantir que a busca seja feita até o limite
        #por exemplo, se definir o limite igual a 3 terei problemas  
        #preciso mais de 3 movimentos para chegar a solução
        #desta forma a busca não vai ser eficiente
        if ((len(caminho)/len(movimento))*10) > limite:
            continue
       
        if final == end: break 

    print('\nNós expandidos: ', (len(explorado)-1))
    print('\nMovimentos da solução da busca em Profundidade:')
    print()
    return caminho


#main

#preenchimento do tabuleiro inicial
raiz=Node
raiz.tabuleiro=[]

for i in range (0,3):
    local=[]
    for i in range(0,3):
        local.append(int(input('Digite um número: ')))
    raiz.tabuleiro.append(local)
print("\nO tabuleiro está: ")

for i in range (0,3):
    print(raiz.tabuleiro[i])


tabuleiro = str(raiz.tabuleiro)

obj_final = str([
                [1,2,3],
                [4,5,6],
                [7,8,0]
            ])


print ('\nO objetivo é: ')
print (obj_final)

print('\nInforme qual algoritmo de busca deseja utilizar para chegar ao objetivo: ')
print()
print("1: Busca em Largura")
print("2: Busca em Profundidade Limitada")
print()


op = int(input('Informe uma opção: '))
if(op==1):
    print('\n___________MÉTODO DE BUSCA EM LARGURA___________')
    for i in buscaLargura(tabuleiro,obj_final):
        print(i, end="\n")
if(op==2):
    print('\n___________MÉTODO DE BUSCA EM PROFUNDIDADE LIMITADA___________')
    for i in buscaProfundidadeLimitada(tabuleiro, obj_final, 25):
        print(i, end="\n")
