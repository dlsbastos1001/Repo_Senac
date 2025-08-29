#n1 = int(input('digite o primeiro numero: '))
#n2 = int(input('digite o segundo numero: '))
#r = n1 + n2
#print(r)

nome = input('digite seu nome: ').title()

while True:
    try:
        n1 = float(input('digite a primeira nota nota: '))
        break
    except:
        print('insira um valor válido!')

while True:
    try:
        n2 = float(input('digite a segunda nota: '))
        break
    except:
        print('insira um valor válido!')

m = (n1 + n2)/2
if m < 5:
    r = ('reprovou')
elif 5 < m < 7:
    r = ('recuperação')
else:
    r = ('passou')

print (f'@ alun@ {nome} fiocu com a media {m} e condição {r}')
















































