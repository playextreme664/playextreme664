import random
alun1 = str(input('Digite o primeiro nome: '))
alun2 = str(input('Digite o segundo nome: '))
alun3 = str(input('Digite o terceiro nome: '))
alun4 = str(input('Digite o quarto nome: '))
nomes = [alun1, alun2, alun3, alun4]
sort = random.choice(nomes)
print(f'O aluno escolhido foi {sort}')
