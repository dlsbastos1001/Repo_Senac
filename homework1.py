'''
Contexto: Você foi contratado para desenvolver um sistema básico de reservas
para o Konoha Hotel. O sistema deve permitir que o usuário informe seu nome,
número de noites que deseja ficar e o tipo de quarto. Com base nessas
informações, o programa deve calcular o valor total da estadia e exibir uma
confirmação formatada.
Regras do sistema:
● Quarto Genin: R$ 120,00 por noite
● Quarto Jounin: R$ 180,00 por noite
● Suíte Hokage: R$ 250,00 por noite
'''
nome = input("Qual o seu nome: ")

while True:
    try:
        noites = int(input("Quantas noites você deseja ficar: "))
        if noites > 0:
            break
        else:
            print("Por favor, insira um número positivo de noites")
    except:
        print("Entrada inválida. Por favor, insira um número valido de noites")

while True:
    try:     
        tipo_quarto = input("Qual o tipo de quarto (Genin, Jounin, Hokage): ")
        if tipo_quarto == "Genin" or tipo_quarto == "Jounin" or tipo_quarto == "Hokage" or tipo_quarto == "jounin" or tipo_quarto == "genin" or tipo_quarto == "hokage":
            break
        else:
            print("Tipo de quarto inválido. Por favor, escolha entre Genin, Jounin ou Hokage")
    except:
        print("Entrada inválida. Por favor, insira um tipo de quarto valido")
        
if tipo_quarto == "Genin" or tipo_quarto == "genin":
    tipo_quarto = 120
elif tipo_quarto == "Jounin" or tipo_quarto == "jounin":
    tipo_quarto = 180
else:
    tipo_quarto = 250
 
preço = tipo_quarto * noites
print(f'A estadia de {noites} noites  do {nome} vai ser no quarto {tipo_quarto} e custará {preço:.2f} R$ ')