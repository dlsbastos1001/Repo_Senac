'''def saudação():
    print('bem vindo ao senac')

print(saudação())'''

'''def saudação(nome):
    print(f'bem vindo ao senac {nome}')

print(saudação('joão'))'''

'''def soma(a, b):
    return a + b
resultado = (soma(5, 3))
print(resultado)'''

numeros = {'primeiro' : [], 'segundo' : [], 'terceiro' : []} 
i = 0
while True:
    try:
        if i < 2:
            'primeiro'[] = int(input('digite o primeiro par: '))
            i += 1
        else:
            break
    except:
        print('valor inválido, digite um número inteiro')

while True:
    try:
        i = 0
        if i < 2:
            'segundo'[] = int(input('digite o segundo par: '))
            i += 1
        else:
            break
    except:
        print('valor inválido, digite um número inteiro')

while True:
    try:
        i = 0
        if i < 2:
            'terceiro'[] = int(input('digite o terceiro par: '))
            i += 1
        else:
            break
    except:
        print('valor inválido, digite um número inteiro')

print('a soma do primeiro par é:' , numeros['primeiro'])













