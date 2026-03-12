l1 = int(input('Digite o primeiro lado: '))
l2 = int(input('digite o segundo lado: '))
l3 = int(input('digite o terceiro lado: '))
if l1 == l2 and l2 == l3 and l3 == l1:
    print('Esse é um triangulo Equilátero pois todos os lados são iguais')
elif l1 == l2 and l3 != l1 and l2:
    print('Esse é um triangulo Isósceles pois tem dois lados iguais')
elif l1 != l2 and l3 != l1 and l2 != l3:
    print('Esse é um triangulo Escaleno pois todo os lados são diferentes')
