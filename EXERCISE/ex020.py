from random import shuffle
n1 = str(input('primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
nomes = [n1, n2, n3, n4]
shuffle(nomes)
print('A ordem de apresentação será')
print(nomes)