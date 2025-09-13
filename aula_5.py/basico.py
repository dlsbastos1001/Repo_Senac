#1
'''nome = str(input('Qual o seu nome: '))
idade = int(input('qual é a sua idade: '))
cidade = str(input('qual é a sua cidade: '))
print (f'Você é {nome}, tem {idade} anos e mora na cidade {cidade}')'''

#2
'''idade = int(input('qual é a sua idade: '))

if idade > 18:
    print('você é maior de idade!')
else:
    print ('Você é menor de idade!')'''

#3
'''for i in range(1, 11, 2):
    print(i)'''

#4
'''contador = 0
while contador <= 5:
    print(contador)
    contador += 1'''

#5
'''frutas = ['banana', 'pera', 'uva', 'laranja', 'limão']
print (frutas)
print (f'aprimeira fruta é {frutas[0]} e a ultima é {frutas[-1]}')'''

#6
'''frutas = ['banana', 'pera', 'uva', 'laranja', 'limão']
frutas.insert(0, 'goiaba')
frutas.remove('laranja')
print (frutas)'''

#7
'''contador = 0
nomes = ['ana', 'maria', 'pedro', 'joão', 'guilherme']
for i in range (len(nomes)):
    print (f'{nomes[contador]} você é @ {contador + 1}° da lista')
    contador += 1'''

#8
'''teste = 1
idades = [15, 19, 20, 21, 22]
for i in range (len(idades)):
    teste = (idades[i])
    if teste > 18:
        teste = ('maior de idade')
    else:
        teste = ('menor de idade')
    print(f'{idades[i]} você é {teste}')
'''
#9
nomes = []
n1 =str(input('digite  primeiro nome:'))
n2 =str(input('digite  segundo nome:'))
n3 =str(input('digite  terceiro nome:'))
nomes.append(n1)
nomes.append(n2)
nomes.append(n3)
print (nomes)
