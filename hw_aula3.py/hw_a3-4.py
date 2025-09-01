'''
Em uma turma, os alunos realizam duas avaliações principais e têm a opção
de fazer uma terceira avaliação (optativa), que pode substituir a nota mais baixa.
Escreva um programa que receba:
- Nota da primeira avaliação,
- Nota da segunda avaliação,
- Nota da avaliação optativa (ou -1 caso não tenha feito).
O programa deve calcular a média do semestre considerando a substituição da
menor nota, se a optativa for válida. Depois, deve exibir:
- A média final,
- Uma mensagem indicando a situação do aluno:
- Aprovado: média ≥ 6.0
- Reprovado: média < 3.0
- Exame: média ≥ 3.0 e < 6.0'''

# Garantindo que o usuario de uma primeira nota valida
while True:
    try:
        nota1 = float(input('Qual foi a nota da sua primeira prova:'))
        if nota1 < 0 or nota1 > 10:
            print('insira um valor numérico válido: (0/10)')
        else:
            break
    except:
        print('Por favor, insira um valor numérico válido.')

# Garantindo que o usuario de uma segunda nota valida
while True: 
    try:
        nota2 = float(input('Qual foi a nota da sua segunda prova:'))
        print()
        if nota2 < 0 or nota2 > 10:
            print('insira um valor numérico válido: (0/10)')
        else:
            break
    except:
        print('Por favor, insira um valor numérico válido.')

# Calculando a média inicial para recomendar ou não a terceira avaliação
media1 = (nota1 + nota2) / 2
if media1 < 6 :
    recomendação = str('sim')
else:
    recomendação = str('não')

if media1 >= 6:
    situação = str('Aprovado')
elif 4 < media1 < 6: 
    situação = str('Recuperação')
else: 
    situação = str("Reprovado")

# Garantindo que o usuario de uma valor valido para uma eventual terceira avaliação
# Por que o if da linha 59 não garante que o aluno decidiu entre fazer ou não a terceira avaliação?
while True:
    try:
        terceira_av = str(input(f'Considerando situação de {situação} você deseja fazer uma terceira avaliação? (recomendado: {recomendação}) ' ))
        print()
        if terceira_av != 'Sim' or 'sim' or 's' or 'Não' or 'não' or 'n':
            break
        else:
            print('Por favor, responda com Sim ou Não')
    except:
        print('Por favor, responda com Sim ou Não')

# Garantindo que se o usuario fez a terceira avaliação uma nota valida foi dada
# Por que o if da linha 68 não garante que o aluno que decidiu não fazer a terceira avaliação não tenha sua media_semestral alterada?
if terceira_av == 'Sim' or 'sim' or 's':
    while True:
        try:
            nota3 = float(input('Qual a nota da sua terceira avaliação: '))
            if nota3 < 0 or nota3 > 10:
                print('Por favor insira um valor numerico valido: (0/10)')
            else:
                break
        except:
            print('Por favor insira um valor numerico valido')
else: 
    nota3 = -1

# Calculando a média final considerando, ou não, que a terceira avaliação substituiu a menor nota
if nota3 > 0:
    if nota3 < nota1 and nota3 < nota2:
        media_semestral = (nota1 + nota2) / 2
    elif nota1 > nota2:
        nota2 = nota3
        media_semestral = (nota1 + nota2) / 2
    elif nota1 == nota2:
        nota1 = nota3
        media_semestral = (nota1 + nota2) / 2
    else:
        nota1 = nota3
        media_semestral = (nota1 + nota2) / 2
else:
    media_semestral = (nota1 + nota2) / 2

# Calculando a situação da média semestral do aluno
if media_semestral >= 6:
    situação = str('Aprovado')
elif 4 < media_semestral < 6: 
    situação = str('Repetência')
else: 
    situação = str("Reprovado")
print(f'A sua media semestral foi {media_semestral:.2f}, logo a sua situação é de: {situação}.')
