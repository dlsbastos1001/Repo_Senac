'''
Uma pessoa está reformando sua cozinha e precisa saber quantas
caixas de azulejos comprar para revestir todas as paredes. Escreva um
programa que receba:
- Comprimento, largura e altura da cozinha (em metros).
Considere que:
- Todas as quatro paredes serão revestidas,
- Cada caixa de azulejos cobre 1,5 m2,
- Não será descontada a área de portas e janelas.
O programa deve calcular:
- A área total das paredes,
- A quantidade de caixas necessárias (arredondando para cima).'''


comprimento = float(input("Qual o comprimento da cozinha? "))
largura = float(input("Qual a largura da cozinha? "))
altura = float(input("Qual a altura da cozinha? "))
a1 = comprimento * largura 
a2 = comprimento * largura
a3 = comprimento * altura
a4 = comprimento * altura
a5 = largura * altura
a6 = largura * altura
Area = a1 + a2 + a3 + a4 + a5 + a6
caixa_pisos = (Area / 1.5)
print (f'devemos comprar {caixa_pisos:.0f} caixas de azulejo')































