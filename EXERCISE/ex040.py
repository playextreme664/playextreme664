n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('Você está reprovado')
elif m >= 5.0 and m <= 6.9:
    print('Você está em recuperação')
else:
    print('Você está aprovado')
