"""Crie um programa contendo uma função que, dados um valor de renda mensal total, gastos totais com moradia, gastos totais
com educação e gastos totais com transporte, faça um diagnóstico da saúde financeira do usuário, com base nos valores 
percentuais acima expostos, informando qual é o percentual da renda mensal total comprometido por cada custo. 
Se o gasto estiver dentro do percentual recomendado, informe ainda que Seus gastos estão dentro da margem recomendada.
Caso contrário, informe:
Portanto, idealmente, o máximo de sua renda comprometida com {tipo} deveria ser de R$ {valor_max}
Onde tipo deve ser moradia, educação ou transportes e valor_max deve ser o valor equivalente ao percentual máximo de gasto
com esse tipo de custo.
Regra: máximo, 30% da sua renda mensal à moradia, 20% à educação e 15% ao transporte."""

def diagnostico(renda, moradia, educacao, transporte):
    permoradia = round(moradia / renda,2)*100
    pereducacao = round(educacao / renda,2)*100
    pertransporte = round(transporte / renda,2)*100
    if permoradia <= 30:
        print(f'Seus gastos com moradia comprometem {permoradia} % de sua renda total. O máximo recomendado é 30%. Seus gastos estão dentro da margem recomendada.')
    else:
        print(f'Seus gastos com moradia comprometem {permoradia} % de sua renda total. O máximo recomendado é 30%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {round((renda*0.3),2)} .')

    if pereducacao <= 20:
        print(f'Seus gastos com educação comprometem {pereducacao} % de sua renda total. O máximo recomendado é 20%. Seus gastos estão dentro da margem recomendada.')
    else:
        print(f'Seus gastos com educação comprometem {pereducacao} % de sua renda total. O máximo recomendado é 20%. Portanto, idealmente, o máximo de sua renda comprometida com educação deveria ser de R$ {round((renda*0.2),2)} .')

    if pertransporte <= 15:
        print(f'Seus gastos com transporte comprometem {pertransporte} % de sua renda total. O máximo recomendado é 15%. Seus gastos estão dentro da margem recomendada.')
    else:
        print(f'Seus gastos com transporte comprometem {pertransporte} % de sua renda total. O máximo recomendado é 15%. Portanto, idealmente, o máximo de sua renda comprometida com transporte deveria ser de R$ {round((renda*0.15),2)} .')


while True:
    try:
        renda = float(input('Informe o valor total da renda mensal: R$ ')) 
        break
    except:
        print('Entrada inválida! Exemplo de formato válido: R$ 20.10')

while True:
    try:
        moradia = float(input('Informe os gastos totais com moradia: R$ '))  
        break
    except:
        print('Entrada inválida! Exemplo de formato válido: R$ 20.10')

while True:
    try:
        educacao = float(input('Informe os gastos totais com educação: R$ '))
        break
    except:
        print('Entrada inválida! Exemplo de formato válido: R$ 20.10')

while True:
    try:
        transporte = float(input('Informe os gastos totais com transporte: R$ '))     
        break
    except:
        print('Entrada inválida! Exemplo de formato válido: R$ 20.10')

diagnostico(renda, moradia, educacao, transporte)


