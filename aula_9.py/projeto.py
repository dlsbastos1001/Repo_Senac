#Sistema de Atendimento do Restaurante Kamado Tanjirō

# Cardápio do restaurante
cardapio = {
    1: {"item": "Sushi", "preço": 25.00},
    2: {"item": "Tempurá", "preço": 20.00},
    3: {"item": "Yakissoba", "preço": 30.00},
    4: {"item": "Sashimi", "preço": 35.00},
    5: {"item": "Gyoza", "preço": 15.00},
    6: {"item": "Harumaki", "preço": 12.00},
    7: {"item": "Missoshiro", "preço": 10.00},
    8: {"item": "Chá verde", "preço": 8.00},
    9: {"item": "Sake", "preço": 18.00},
    10: {"item": "Tempurá de camarão", "preço": 22.00},
    11: {"item": "Uramaki", "preço": 28.00},
    12: {"item": "Nigiri", "preço": 26.00},
    13: {"item": "Hossomaki", "preço": 24.00},
    14: {"item": "Onigiri", "preço": 14.00},
    15: {"item": "Karaage", "preço": 19.00},
    16: {"item": "Tonkatsu", "preço": 32.00},
    17: {"item": "Okonomiyaki", "preço": 29.00},
    18: {"item": "Takoyaki", "preço": 16.00},
    19: {"item": "Edamame", "preço": 11.00},
    20: {"item": "Chirashi", "preço": 34.00},
}

# Lista de garçons válidos
garcons = ["Ana", "Maria", "Carla", "Cassio", "João"]

# Lista de mesas disponíveis
mesas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

# Dicionário para armazenar os pedidos
pedidos_registrados = {}
contador_pedidos = 1

def exibir_cardapio():
    """Função para exibir o cardápio completo"""
    print("\n" + "="*55)
    print("          CARDÁPIO KAMADO TANJIRŌ")
    print("="*55)
    print("CÓD | ITEM                  | PREÇO (R$)")
    print("-"*55)
    for codigo, item_info in cardapio.items():
        print(f"{codigo:3} | {item_info['item']:20} | {item_info['preço']:8.2f}")
    print("="*55)

def registrar_pedido(garcom):
    """Função para registrar um novo pedido"""
    global contador_pedidos
    
    print(f"\nOlá, {garcom}! Vamos registrar um novo pedido.")
    
    # Selecionar mesa
    print("\nMesas disponíveis:", ", ".join(mesas))
    mesa = input("Digite a letra da mesa: ").upper()
    
    if mesa not in mesas:
        print("Mesa inválida! Use uma letra de A a J.")
        return
    
    # Coletar itens do pedido
    itens_pedido = []
    print("\nDigite os códigos dos itens do pedido (0 para finalizar):")
    
    while True:
        exibir_cardapio()
        try:
            codigo = int(input("\nCódigo do item: "))
            if codigo == 0:
                break
            if codigo not in cardapio:
                print("Código inválido! Tente novamente.")
                continue
            itens_pedido.append(codigo)
            print(f"Item adicionado: {cardapio[codigo]['item']}")
        except ValueError:
            print("Por favor, digite um número válido.")
    
    if not itens_pedido:
        print("Nenhum item foi adicionado ao pedido.")
        return
    
    # Calcular total do pedido
    total = sum(cardapio[item]['preço'] for item in itens_pedido)
    
    # Registrar pedido
    pedidos_registrados[contador_pedidos] = {
        'mesa': mesa,
        'garcom': garcom,
        'itens': itens_pedido,
        'total': total
    }
    
    print(f"\n Pedido registrado com sucesso!")
    print(f"Número do pedido: {contador_pedidos}")
    print(f"Mesa: {mesa}")
    print(f"Total: R$ {total:.2f}")
    
    contador_pedidos += 1

def fechar_conta():
    """Função para fechar a conta de um pedido"""
    try:
        numero_pedido = int(input("\nDigite o número do pedido para fechar a conta: "))
        
        if numero_pedido not in pedidos_registrados:
            print("Pedido não encontrado!")
            return
        
        pedido = pedidos_registrados[numero_pedido]
        
        print("\n" + "="*50)
        print("         CONTA DO RESTAURANTE")

        print(f"Nº do pedido: {numero_pedido}")
        print(f"Mesa: {pedido['mesa']}")
        print(f"Garçom: {pedido['garcom']}")
        print("-"*50)
        print("ITENS:")
        for item in pedido['itens']:
            print(f"  {cardapio[item]['item']} - R$ {cardapio[item]['preço']:.2f}")
        print("-"*50)
        print(f"TOTAL: R$ {pedido['total']:.2f}")

        print("Obrigado pela preferência!")
        
    except ValueError:
        print("Por favor, digite um número válido.")

def ver_pedidos_garcom(garcom):
    """Função para visualizar todos os pedidos de um garçom"""
    print(f"\n PEDIDOS REGISTRADOS POR {garcom.upper()}")
    print("="*60)
    
    encontrados = False
    for num, pedido in pedidos_registrados.items():
        if pedido['garcom'] == garcom:
            encontrados = True
            print(f"Pedido #{num} | Mesa: {pedido['mesa']} | Total: R$ {pedido['total']:.2f}")
            print("Itens:", ", ".join([cardapio[item]['item'] for item in pedido['itens']]))
            print("-"*60)
    
    if not encontrados:
        print("Nenhum pedido registrado por este garçom.")

def main():
    """Função principal do sistema"""
    print("   RESTAURANTE KAMADO TANJIRŌ")
    print("      Sistema de Atendimento")
    
    # Login do garçom
    while True:
        garcom = input("\nDigite seu nome para fazer login: ")
        if garcom in garcons:
            print(f"Bem-vindo(a), {garcom}!")
            break
        else:
            print("Garçom não reconhecido. Tente novamente.")
            print("Garçons válidos:", ", ".join(garcons))
    
    # Menu principal
    while True:
        print("\n" + "="*30)
        print("        MENU PRINCIPAL")
        print("="*30)
        print("1. Visualizar cardápio")
        print("2. Registrar novo pedido")
        print("3. Fechar conta")
        print("4. Ver meus pedidos")
        print("5. Sair do sistema")
        print("="*30)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            exibir_cardapio()
        elif opcao == "2":
            registrar_pedido(garcom)
        elif opcao == "3":
            fechar_conta()
        elif opcao == "4":
            ver_pedidos_garcom(garcom)
        elif opcao == "5":
            print(f"\nObrigado por usar o sistema, {garcom}! Até logo!")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção de 1 a 5.")

# Executar o programa
if __name__ == "__main__":
    main()

