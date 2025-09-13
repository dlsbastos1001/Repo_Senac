#valor = int(input('escolha uma opção (1, 2, 3, 4, 0) '))
nome = str(input('Qual o seu nome? (alfredo ou bernardo) '))
opção =  str(input('oque você quer: (adicionar filme a a, adicionar filmes a b, remover filme, ver filmes de a, ver filmes de todos os usuarios ou sair?) '))
dicionario = {'filmes de alfredo' : [],'filmes de bernardo': []}
while True:
    try:
        if opção == 'adicionar filme a a':   
            adicionario_filme = str(input('Qual filme a a quer adicionar? '))
            dicionario['filmes de a'].append(adicionario_filme)
            print('filme adicionado com sucesso!')
        elif opção == 'adicionar filmes a b':
            dicionario_filme_b = str(input('Qual filme a b quer adicionar? '))
            dicionario['filmes de b'].append(dicionario_filme_b)
        elif opção == 'remover filme':
            remover = str(input('de onde quer remover filme: (a/b) '))
            if remover == 'a':
                remover_a = str(input('Qual filme a a quer remover? '))
                dicionario['filmes de a'].remove(remover_a)
            else:
                remover_b = str(input('Qual filme a b quer remover? '))
                dicionario['filmes de b'].remove(remover_b)
        elif opção == 'ver filmes de a':
            print({dicionario.get('filmes de a')})
        elif opção == 'ver filmes de todos os usuarios':
            print({dicionario.get('filmes de a')})
            print({dicionario.get('filmes de b')})
        else:
            print('você encerrou o programa!')
            break
    except:
        print('opção inválida, tente novamente')
    