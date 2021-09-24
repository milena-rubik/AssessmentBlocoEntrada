""" A) Desenvolva um programa contendo uma função que permita ao usuário solicitar o PIB de um país para um 
determinado ano. O programa solicita ao usuário o nome do país e o ano desejado. Caso o país solicitado ou 
o ano não sejam válidos, o programa deve informar, na saída, a mensagem: País não disponível ou Ano não disponível
a depender do tipo de dado não encontrado. Exemplo de saída do programa:
Informe um país: Brasil
Informe um ano entre 2013 e 2020: 2020
PIB Brasil em 2020: US$2.35 trilhões."""


def consultarpib(nomearquivo,pais,ano):
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
        pibspicados.append(listapibs) #coloca a listapibs em pibspicados, aninhamento de listas
  
    if pais in paises:
        indicepais = paises.index(pais)#captura o índice do pais desejado
    else:
        print('País não disponível')
    
    if ano in rotulos:
        indiceano = rotulos.index(ano)
    else:
        print('Ano não disponível')
    
    print(f'PIB {pais} em {ano}: U$$ {pibspicados[indicepais][indiceano-1]} trilhões')
    



print('Instruções: O país deve ser informado com a inicial maíscula e acento se houver, como por exemblo "Itália", para os Estados Unidos use "EUA" ')
paisconsultado = input('Informe um País: ')
anoconsultado = input('Informe um ano entre 2013 e 2020: ')

consultarpib('Assessment_PIBs.csv',paisconsultado,anoconsultado) #chama a função de consulta de PIB




    

