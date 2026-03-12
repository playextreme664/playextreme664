import random
print('[Pedra] [Papel] [Tesoura]')
n = str(input('Qual a sua escolha? '))
jk = ['Pedra', 'Papel', 'Tesoura']
r = (random.choice(jk))
print('O computador escolheu',(r))    
#Pedra
if n == 'pedra' and r == 'Papel':
    print('Você perdeu!')
elif n == 'pedra' and r == 'Tesoura':
    print('Você ganhou!')     
elif n == 'pedra' and r == 'Pedra':
    print('Empate!')
#Papel    
elif n == 'papel' and r == 'Pedra':
    print('Você ganhou!')
elif n == 'papel' and r == 'Tesoura':
    print('Você perdeu!') 
elif n == 'papel' and r == 'Papel':
    print('Empate!')
#Tesoura         
elif n == 'tesoura' and r == 'Pedra':
    print('Você perdeu!')
elif n == 'tesoura' and r == 'Papel':
    print('Você ganhou!')
elif n == 'tesoura' and r == 'Tesoura':       
    print('Empate!')