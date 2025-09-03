#produtos = int(input('quantos produtos deseja cadastrar: '))
produtos = []
n = []
v = []
while True: 
    try: 
        nome = input('digite o nome do produto: ')
        n.append(nome)
        produtos.append(nome)
        valor = int(input('digite o valor do produto: '))
        v.append(valor)
        produtos.append(valor)
        print (produtos)
        sair = input('deseja sair: (s/n)')
        if sair == 's':
            break
    except:
        print ("digite um valor valido")

for i in produtos-2:
    print (f'o produto {n} custa {v}')
