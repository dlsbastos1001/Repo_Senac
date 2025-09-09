'''O restaurante Kamado Tanjirō, especializado
em culinária japonesa, está localizado na Av.
Lúcio Costa, na Barra da Tijuca – RJ. Com um
espaço de 100 m2, o restaurante oferece
ambientes climatizados e área ao ar livre,
atendendo a uma clientela exigente e
crescente. Atualmente, a equipe conta com
70 colaboradores, entre recepcionistas,
garçons, cozinheiros e equipe administrativa.
Com o aumento da demanda, a direção do restaurante decidiu automatizar
o processo de atendimento, especialmente a realização de pedidos. Para
isso, será desenvolvido um sistema simples que permita aos garçons:
• Visualizar o cardápio digital.
• Registrar os pedidos feitos pelos clientes.
• Associar cada pedido à mesa e ao garçom responsável.
• Gerar um número de pedido para que o cliente possa realizar o
pagamento no caixa.
Objetivo da atividade:
Você deverá criar um programa em Python que simule esse sistema básico
de pedidos. Para isso, será necessário implementar funções que
representem as principais ações do restaurante.

🔧Requisitos do sistema (funções que devem ser criadas):
1. Função para exibir o cardápio
Deve mostrar os pratos disponíveis, suas descrições e respectivos
preços.
2. Função para registrar um pedido
Deve receber como parâmetros: número da mesa, nome do garçom e
lista de itens escolhidos. A função deve calcular o valor total do
pedido e gerar um número identificador.
3. Função para fechar a conta
Deve receber o número do pedido e exibir os detalhes: mesa, garçom,
itens pedidos e valor total a ser pago.'''

pedidos = []
cardapio = ['Sushi',
'Udon',
'Ramen',
'Sashimi',
'Soba',
'Yakitori',
'Tonkatsu',
'Okonomiyaki', 
'Tempura', 
'Takoyaki', 
'Katsudon', 
'Unagi',
'Onigiri',
'Gyoza',
'Chawanmushi',
'Karaage',
'Nikujaga',
'Miso']

def menu():

    while True:
        try:
            pedido = str(input('digite um pedido: (ou out para sair) '))
            if pedido in cardapio:
                print(f'{pedido} foi adicionado aos seus pedidos')
                pedidos.append(pedido)
                pedido = None
            elif pedido == 'out':
                break
            else:
                print('esse item não está no cardapio')
        except:
            print('esse item não está no cardapio')

pedido = str(input('qual é o seu pedido: '))