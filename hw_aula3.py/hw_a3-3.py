'''
Um motorista de táxi deseja calcular o rendimento de seu carro ao
final do dia. Desenvolva um programa que receba:
- A marcação do odômetro no início e no fim do dia (em km),
- A quantidade de litros de combustível consumidos,
- O valor total recebido dos passageiros (em reais).
Sabendo que o preço do combustível é R$ 4,87 por litro, o programa
deve calcular:
- A média de consumo (km por litro),
- O gasto com combustível,
- O lucro líquido do dia (valor recebido - gasto com combustível).'''

while True:
    try:
        kilometragem_inicial = float(input('Qual era a km no início da corrida? '))
        if kilometragem_inicial <= 0:
            print ('Por favor, insira uma kilometragem inicial.')
        else:
            break
    except:
        print('Por favor, insira um valor numérico positivo.')

while True:
    try:
        kilometragem_final = float(input('Qual foi a kilometragem no final da corria? '))
        if kilometragem_final < kilometragem_inicial:
            print ('Por favor, insira uma kilometragem final maior que a inicial.')
        else:
            break
    except:
        print('Por favor, insira um valor numérico positivo.')

while True:
    try:
        combustivel = float(input('Quantos litros de combustível foram consumidos? '))
        if combustivel <= 0:
            print ('Por favor, insira um valor numérico válido.')
        else:
            break
    except:
        print('Por favor, insira um valor numérico válido.')

while True:
    try:
        receita = float(input('Qual foi valor o das passagens? '))
        if receita <= 0:
            print ('Por favor, insira um valor numérico válido.')
        else:
            break
    except:
        print('Por favor, insira um valor numérico válido.')

Ds_corrida = kilometragem_final - kilometragem_inicial
custo_g = combustivel * 4.87
m_consumo = Ds_corrida / combustivel
lucr_liquido = receita - custo_g

print(f'A média de consumo foi de {m_consumo:.2f} Km/l, o gasto com combustível foi de R$ {custo_g:.2f} e o lucro líquido do dia foi de R$ {lucr_liquido:.2f}.')
