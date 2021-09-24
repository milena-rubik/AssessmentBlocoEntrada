""" 'Os juros compostos são a força mais poderosa do universo e a maior invenção da humanidade, porque permitem uma 
confiável e sistemática acumulação de riqueza.' Albert Einstein
Crie um programa que ponha a hipótese de Einstein à prova. Em uma função, receba, como entrada, um montante financeiro 
inicial, um percentual de rendimento por período, um valor de aporte para cada período e uma quantidade de períodos.
Crie uma função que exiba um gráfico da evolução do valor acumulado, tendo como eixo das abscissas (horizontal) o número 
de períodos e, no eixo das ordenadas (vertical), o valor acumulado, em reais. """

import matplotlib.pyplot as pl

def juros(valor):
    for i in range (1,periodos+1):
        valor = round((valor+(valor*(rendimento/100)) + aporte),2)
        print(f'Após {i} período(s), o montante será de R$ {valor} ')
        listavalory.append(valor) #adiciona os valores a lista que comporá o eixo y
        listaperiodox.append(i) #adiciona os valores a lista que comporá o eixo x
    pl.plot(listaperiodox,listavalory) #determinando o eixo x e o y do gráfico
    pl.xlabel('Períodos') #nomeando eixo x
    pl.ylabel('Montante') #nomeando eixo y
    pl.show()
        

print('Alerta: Todos os valores informados devem utilizar "." como separador decimal')

valor = float(input('Informe o valor inicial (R$): '))
rendimento = float(input('Informe o rendimento por período (%): '))
aporte = float(input('Informe o aporte a cada período (R$): '))
periodos = int(input('Informe o total de períodos: '))

listavalory = list()
listaperiodox = list()

juros(valor)

