'''
Nome: Aélton Sousa Das Virgens 
Universidade: Univerdidade de Brasília
Curso: Engenharia de Computação
Semestre atual:6º Semestre
''' 

from statistics import quantiles
from typing import Counter
from xmlrpc.client import boolean

#Função que transforma os códigos de pacotes em Strings
def TratarDados(dados):
    trincas = []
    origem = ''
    destino = ''
    cogigoLoggi = ''
    vendedor = ''
    tipoProduto = ''
    validadeProduto=True
    

    #Separando em Trincas
    for index in range(0, len(dados), 3):
        trincas.append(dados[index : index + 3])

    #Classicando as Trincas
    if int(trincas[0]) < 100:
        origem = 'Sudeste'
    elif int(trincas[0]) > 99 and int(trincas [0]) < 200:
        origem = 'Sul'
    elif int(trincas[0]) > 199 and int(trincas [0]) < 300:
        origem = 'Centro-oeste'
    elif int(trincas[0]) > 299 and int(trincas [0]) < 400:
        origem = 'Nordeste'
    else:
        origem = 'Norte'
    

    if int(trincas[1]) < 100:
        destino = 'Sudeste'
    elif int(trincas[1]) > 99 and int(trincas [0]) < 200:
        destino = 'Sul'
    elif int(trincas[1]) > 199 and int(trincas [0]) < 300:
        destino = 'Centro-oeste'
    elif int(trincas[1]) > 299 and int(trincas [0]) < 400:
        destino = 'Nordeste'
    else:
        destino = 'Norte'
    
    cogigoLoggi = trincas[2]
    vendedor = trincas[3]

    if trincas[4] == '001':
        tipoProduto = 'Jóias'
    elif trincas[4] == '111':
        tipoProduto = 'Livro'
    elif trincas[4] == '333':
        tipoProduto = 'Eletrônico'
    elif trincas[4] == '555':
        tipoProduto = 'Bebida'
    elif trincas[4] == '888':
        tipoProduto = 'Brinquedo'
    else:
        tipoProduto = 'Inválido'

    #Tratando validade do Pacote

    if tipoProduto == 'Inválido':
        validadeProduto = False
    if tipoProduto == 'Centro-oeste' and origem == 'Centro-oeste':
        validadeProduto = False
    if vendedor == '367':
        validadeProduto = False

    dadosTratados=[origem,destino,cogigoLoggi,vendedor,tipoProduto, validadeProduto]
    
    return dadosTratados

#Lista de códigos de pacote
codPacotes =['288355555123888',
'335333555584333',
'223343555124001',
'002111555874555',
'111188555654777',
'111333555123333',
'432055555123888',
'079333555584333',
'155333555124001',
'333188555584333',
'555288555123001',
'111388555123555',
'288000555367333',
'066311555874001',
'110333555123555',
'333488555584333',
'455448555123001',
'022388555123555',
'432044555845333',
'034311555874001'] 

#Transformando os pacotes em uma lista
pacotes = []
for index in range(len(codPacotes)):
    pacotes.append(TratarDados(codPacotes[index]))

    
print('#########################################################################\n')
#Questão 1
#Identificar a região de destino de cada pacote, com totalização de pacotes (soma região); 
print('QUESTÃO 1:\n')

pacotesNorte=0
pacotesNordeste=0
pacotesCentroOeste=0
pacotesSudeste=0
pacotesSul=0
pacotesinvalidos=0

for index in range (len(pacotes)):
    if not pacotes[index][5]:
        pacotesinvalidos+=1
        print('PACOTE %d -> DESTINO: INVÁLIDO' % (index + 1))
    
    else:
        if pacotes[index][1]== 'Norte':
            pacotesNorte+=1
            print('PACOTE %d -> DESTINO: NORTE' % (index + 1))
        if pacotes[index][1]== 'Nordeste' :
            pacotesNordeste+=1
            print('PACOTE %d -> DESTINO: NORDESTE' % (index + 1))
        if pacotes[index][1]== 'Centro-oeste':
            pacotesCentroOeste+=1
            print('PACOTE %d -> DESTINO: CENTRO-OESTE' % (index + 1))
        if pacotes[index][1]== 'Sudeste':
            pacotesSudeste+=1
            print('PACOTE %d -> DESTINO: SUDESTE' % (index + 1))
        if pacotes[index][1]== 'Sul':
            pacotesSul+=1
            print('PACOTE %d -> DESTINO: SUL' % (index + 1))
print('\n')

print('TOTAL DE PACOTES ENVIADOS PARA:\nNORTE: %d\nNORDESTE: %d\nCENTRO-OESTE: %d\nSUDESTE: %d\nSUL: %d\nINVÁLIDOS: %d\n\n' % (pacotesNorte,pacotesNordeste,pacotesCentroOeste,pacotesSudeste,pacotesSul, pacotesinvalidos))

print('#########################################################################\n')

#Questão 2
#Saber quais pacotes possuem códigos de barras válidos e/ou inválidos;
print('QUESTÃO 2:\n')
for index in range (len(pacotes)):
    if pacotes[index][4]=='Inválido':
        print('PACOTE %d: CÓDIGO INVÁLIDO\n'%(index+1))
    else:
        print('PACOTE %d: CÓDIGO VÁLIDO\n' %(index+1))


print('#########################################################################\n')

#Questão 3
# Identificar os pacotes que têm como origem a região Sul e Brinquedos em seu conteúdo; 
print('QUESTÃO 3:\n')
brinquedosDoSul=[]
quantidade=0

for index in range (len(pacotes)):
    if pacotes[index][0] == 'Sul' and pacotes[index][4] == 'Brinquedo' and pacotes[index][5]:
        brinquedosDoSul.append(index+1)
        quantidade+=1
print('PACOTES COM BRINQUEDOS DE ORIGEM SUL: ')
print(brinquedosDoSul)
print('QUANTIDADE: %d'% (quantidade))


print('#########################################################################\n')

#Questão 4
#Listar os pacotes agrupados por região de destino (Considere apenas pacotes válidos); 
print('QUESTÃO 4:\n')

listaPacotesNorte=[]
listaPacotesNordeste=[]
listaPacotesCentroOeste=[]
listaPacotesSudeste=[]
listaPacotesSul=[]
listaPacotesinvalidos=[]

for index in range (len(pacotes)):
    if not pacotes[index][5]:
        listaPacotesinvalidos.append(index+1)
       
    
    else:
        if pacotes[index][1]== 'Norte':
            listaPacotesNorte.append(index+1)
        
        if pacotes[index][1]== 'Nordeste' :
            listaPacotesNordeste.append(index+1)
         
        if pacotes[index][1]== 'Centro-oeste':
            listaPacotesCentroOeste.append(index+1)
            
        if pacotes[index][1]== 'Sudeste':
            listaPacotesSudeste.append(index+1)
          
        if pacotes[index][1]== 'Sul':
            listaPacotesSul.append(index+1)
      
print('PACOTES COM DESTINO:\n' )
print('NORTE:')
print(listaPacotesNorte)
print('NORDESTE:')
print(listaPacotesNordeste)
print('CENTRO-OESTE:')
print(listaPacotesCentroOeste)
print('SUDESTE:')
print(listaPacotesSudeste)
print('SUL:')
print(listaPacotesSul)


print('#########################################################################\n')

#Questão 5
#Listar o número de pacotes enviados por cada vendedor (Considere apenas pacotes válidos); 
print('QUESTÃO 5\n')

vendedores=[]

for index in range (len(pacotes)):
    if pacotes[index][5]:
        vendedores.append(pacotes[index][3])
print("VENDORES E PRODUTOS ENVIADOS:\n")
print(Counter(vendedores))


print('#########################################################################\n')

#Questão 6
#Gerar o relatório/lista de pacotes por destino e por tipo (Considere apenas pacotes válidos); 
print('QUESTÃO 6\n')

listaAuxiliar=[]
for index in range (len(listaPacotesNorte)):
    listaAuxiliar.append(pacotes[listaPacotesNorte[index]-1][4])
print('Pacotes Norte:')
print(Counter(listaAuxiliar))

listaAuxiliar=[]
for index in range (len(listaPacotesNordeste)):
    listaAuxiliar.append(pacotes[listaPacotesNordeste[index]-1][4])
print('Pacotes Nordeste:')
print(Counter(listaAuxiliar))

listaAuxiliar=[]
for index in range (len(listaPacotesCentroOeste)):
    listaAuxiliar.append(pacotes[listaPacotesCentroOeste[index]-1][4])
print('Pacotes Centro-oeste:')
print(Counter(listaAuxiliar))

listaAuxiliar=[]
for index in range (len(listaPacotesSudeste)):
    listaAuxiliar.append(pacotes[listaPacotesSudeste[index]-1][4])
print('Pacotes Sudeste:')
print(Counter(listaAuxiliar))

listaAuxiliar=[]
for index in range (len(listaPacotesSul)):
    listaAuxiliar.append(pacotes[listaPacotesSul[index]-1][4])
print('Pacotes Sul:')
print(Counter(listaAuxiliar))


print('#########################################################################\n')

#Questão7
#Se o transporte dos pacotes para o Norte passa pela Região Centro-Oeste, quais são os pacotes que devem ser despachados no mesmo caminhão? 
print('QUESTÃO 7\n')

caminhãoSulNorte=[]
caminhãoSudesteNorte=[]

for index in range (len(pacotes)):
    if pacotes[index][5]:
        if (pacotes[index][0]=='Sul' and pacotes[index][1]=='Centro-oeste') or (pacotes[index][0]=='Sul' and pacotes[index][1]=='Norte'):
            caminhãoSulNorte.append(pacotes[index+1])
        if (pacotes[index][0]=='Sudeste' and pacotes[index][1]=='Centro-oeste') or (pacotes[index][0]=='Sudeste' and pacotes[index][1]=='Norte'):
            caminhãoSudesteNorte.append(pacotes[index+1])
print('PACOTES QUE DEVEM IR NO MESMO CAMINHÃO SUL -> CENTRO-OESTE -> NORTE: ')
print(caminhãoSulNorte)
print('PACOTES QUE DEVEM IR NO MESMO CAMINHÃO SUDESTE -> CENTRO-OESTE -> NORTE: ')
print(caminhãoSudesteNorte)


print('#########################################################################\n')

#Questão 8
#Se todos os pacotes fossem uma fila qual seria a ordem de carga para o Norte no caminhão para descarregar os pacotes da Região Centro Oeste primeiro; 
print('QUESTÃO 8:\n NÃO PROCESSADO\n')


print('#########################################################################\n')

#Questão 9
#No item acima considerar que as jóias fossem sempre as primeiras a serem descarregadas; 

print('QUESTÃO 9:\n NÃO PROCESSADO\n')


print('#########################################################################\n')

#Questão 10
#Listar os pacotes inválidos. 

print('QUESTÃO 10:\n')

print('PACOTES INVÁLIDOS:\n')
for index in range (len(pacotes)):
    if not pacotes[index][5]:
        print('PACOTE %d\n' %(index+1))


print('#########################################################################\n')

