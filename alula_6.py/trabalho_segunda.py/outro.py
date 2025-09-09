'''LEVE: excesso de 105 ACIMA DO LIMITE PERMITIDO : 180.00R$
MEDIA:  EXCESSO ENTRE 10% E 30% ACIMA DO LIMITE: 340.56R$
GRAVE: EXCESSO ACIMA DE 30% DO LIMITE: 480.98R$'''

'''def multa(velocidade_via, velocidade_motorista):
    velocidade_via = int(input('Digite a velocidade da via em KM/H: '))
    velocidade_motorista = int(input('Digite a velocidade do motorista em KM/H: '))

    if velocidade_motorista <= velocidade_via:
        teste = velocidade_motorista - velocidade_via
        if teste <= velocidade_via * 1.1:
            print('Sem multa')
        elif velocidade_via*1.1 <= teste <=  velocidade_via*1.3:
            print('Multa LEVE: excesso de 105 ACIMA DO LIMITE PERMITIDO : 180.00R$')
        elif velocidade_via*1.3 <= teste <= velocidade_via*1.5:
            print('Multa MEDIA: EXCESSO ENTRE 10 e 30% ACIMA DO LIMITE: 340.56R$')
        elif teste > velocidade_via*1.5:
            print('Multa GRAVE: EXCESSO ACIMA DE 30% DO LIMITE: 480.98R$')'''


#taxa metabolica basal

'''def TMB(sexo, peso, altura, idade):
    if sexo == 'M':
        TMB = 66.5 + (13.75 * peso) + (5.003 * altura) - (6.755 * idade)
        print(f'Sua taxa metabolica basal é de {TMB:.2f} Kcal')
    else:
        TMB = 655.1 + (9.56 * peso) + (1.850 * altura) - (4.676 * idade)
        print(f'Sua taxa metabolica basal é de {TMB:.2f} Kcal')

sexo = int(input('Digite 1 para masculino e 2 para feminino: '))
peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em cm: '))
idade = int(input('Digite sua idade em anos: '))

TMB(sexo, peso, altura, idade)'''