numero = int(input('digite um numero'))

#match case:
match numero:
    case 5:
        print('amoeba')
    case 10:
        print('banana')
    case _:
        print('outro valor')
