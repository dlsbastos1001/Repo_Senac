

#estruturas de repetições 
'''contador = 1
while contador <= 5:
    print (f'contador: {contador}')
    contador += 1'''

'''password = input('digite senha ')
while password != '1234':
    senha = input('digite uma senha': ).strip()
    if password != '1234':
        password = int(input('digite uma senha: '))

print ('acesso liberado!')'''


#VERIFICADOR DE MAIOR QUE DEZ
'''for alfarroba in range (0, 10, 1):
    print (alfarroba)'''

'''while True:
    try:
        Numero = int(input('Digite um numero maior do que dez: '))
        break
    except:
        print('Tente um valor válido')

while Numero < 10:
    print ('Esse numero é Menor que dez!')
    Numero = int(input('Digite um número maior do que Dez: '))

print('Esse número é maior que Dez!')'''


#QUAL NUMERO VC QUER DA TBUADA?
'''while True: 
    try:
        numero = int(input('De qual numero vc quer a tabuada: '))
        break
    except:
        print('valor invalido!')

        
for i in range (1, 11, 1):
    print (numero * i)'''



#CONTADOR DE ZERO A VINTE
'''
n = 0
while n < 22:
        print(n)
        n += 2'''


#LISTAS E TUPLAS
'''
nome = ['joão', 22, 4800, 'rua jota']
print(type(nome))
print(nome[0:4])

telefone = 21
nome.append(telefone)
print (nome)

for i in nome:
    print (i)'''

'''
dados = [nome, idade, salario, local]
nome = str(inbput('digite seu nome: '))
idade = int(input('Digite sua idade: '))
salario = int(input('Digite seu salario: '))
local = int(input('Digite seu DDD': ))
for i in nome:
    print(i)'''


#LISTA DO CLIENTE
cliente = []

while True:
    try:
        num = int(input('Digite um numero: '))
        cliente.append(num)
        sair = input('o cliente deseja incluir mais um numero? (s/n)').upper().strip()
        if sair == 'N':
            break
    except:
        print('digite um número válido')

for i in cliente:
    print (i)


#LISTA DA OPÇÃO
'''    print ('1\n 2\n 3\n 4\n')
while True:
    try: 
        opção = int(input('opção'))
        if opção in [1,2,3,4]:
            print('opção ok')
        else:
            print('opção invalida!')
    except: 
        print('Digite uym numero válido')'''
