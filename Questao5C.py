"""C) Desenvolva uma função que, para um país, exiba o gráfico da evolução do PIB ao longo dos anos.
A função deve receber, como entrada, o nome de um país, e exibir o gráfico para todo o período listado na tabela.
O gráfico deve conter os valores do PIB no eixo das ordenadas (vertical) e os anos no eixo das abscissas (horizontal)
 """
import matplotlib.pyplot as pl

def graficopib (nomearquivo, pais):
    paises = list()
    pibspicados = list()

    arquivo = open(nomearquivo,'r')
    pibs = arquivo.read()
    pibs = pibs.split('\n') #gera lista, separa cada item por quebra de linha
    rotulos = pibs.pop(0) #cria a lista de rótulos (paises e os anos) como um item só
    rotulos = rotulos.split(',') #cada coisa separada por ',' vira um item em rótulos
    
    for x in pibs:
        listapibs = x.split(',') #gera lista, separa cada item pela vírgula
        paises.append(listapibs[0])#cria lista com os países
        listapibs.pop(0) #retira o primeiro item que se refere a países e deixa só os valores dos Pibs
        pibspicados.append(listapibs) #cria uma lista aninhada onde cada item dos pibspicados é uma lista de pibs de um certo país
    
    paises.pop(15) #remover o item vazio da lista pasíses 
    
    if pais in paises:
        indicepais = paises.index(pais)#captura o índice do país
        eixoy = list()
        for x in (pibspicados[indicepais]): #esse 'for' vai transformar os PIBs do pais escolhido em float e colocá-los no eixo y
            x = float(x)
            eixoy.append(x)
        eixox = rotulos 
        eixox.pop(0) #retira a palavra 'país' deixando apenas os anos
        pl.plot(eixox,eixoy) #determina os eixos
        pl.title(pais)
        pl.xlabel('Anos')
        pl.ylabel('PIB em trilhões de US$')
        pl.show()
    else:
        print('País não disponível')


print('Instruções: O país deve ser informado com a inicial maíscula e acento se houver, como por exemblo "Itália", para os Estados Unidos use "EUA" \n')
paisconsultado = input('Informe um País: ')

graficopib('Assessment_PIBs.csv',paisconsultado)
