

'''
Um morador deseja saber quantas lâmpadas são necessárias para iluminar
adequadamente um cômodo de sua casa. Para isso, você deve desenvolver um
programa que receba:
- A potência da lâmpada (em watts),
- As dimensões do cômodo (largura e comprimento, em metros).
Considere que:
- A potência ideal de iluminação é de 3 watts por metro quadrado.
- A cada 3 m2 deve haver um bocal para uma lâmpada.
O programa deve calcular:
- A área do cômodo,
- A potência total necessária,
- A quantidade de lâmpadas necessárias (arredondando para cima).'''


potencia = int(input("Qual a potência da lâmpada? "))
largura = float(input("Qual a largura do cômodo? "))
comprimento = float(input("Qual o comprimento do cômodo? "))
area = largura * comprimento
potencia_necessaria = area * 3
quantidade_lampadas = area / 3

print(f"A área do cômodo é de {area:.2f} m², a potência total necessária é de {potencia_necessaria:.2f} watts.")
print(f"A quantidade de lâmpadas necessárias é de {int(quantidade_lampadas) + (quantidade_lampadas % 1 > 0)} lâmpadas.")











































