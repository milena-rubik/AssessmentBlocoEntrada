"""B) Desenvolva um programa contendo uma função que liste, por país, a estimativa de variação do PIB, em percentual,
entre 2013 e 2020. Exemplo de saída do programa:

EUA                  Variação de 34.13% entre 2013 e 2020.
China                Variação de 70.72% entre 2013 e 2020.
Japão                Variação de 0.2% entre 2013 e 2020.
Alemanha             Variação de 9.92% entre 2013 e 2020.
Reino Unido          Variação de 39.18% entre 2013 e 2020.
[...] """

def variacaopib(nomearquivo):
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
        pibspicados.append(listapibs)
    
    paises.pop(15) #remover o item vazio da lista pasíses 
    
    for x in paises:
        indicepais = paises.index(x)#captura o índice de cada país
        variacao = (float(pibspicados[indicepais][7])-float(pibspicados[indicepais][0]))/(float(pibspicados[indicepais][0]))
        variacaoporcentagem = round(variacao*100,2)
        print(f'{x}:  Variação de {variacaoporcentagem} % entre 2013 e 2020')
 
    

    

variacaopib('Assessment_PIBs.csv')