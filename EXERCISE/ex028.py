import random
import time
def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.07)  # Ajuste o tempo de atraso conforme necessário
print_slow('Olá, tente adivinhar em qual número de 0 a 5 eu estou pensando? ')
print('')
print_slow('pensando.....')
print('')
eu = int(input('Qual foi o número que eu pensei? '))
n = [0, 1, 2, 3, 4, 5]
pc = (random.choice(n)) 
if eu == pc :
    print_slow('Parabéns, você ganhou')
else:
    print_slow('Que pena, você perdeu')
    print('')    
print_slow(f'O número que eu pensei foi: {pc}') 