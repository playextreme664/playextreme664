import time
def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.09)  # Ajuste o tempo de atraso conforme necessário
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 > n2 and n3 < n1:
    print_slow(f'{n1} é o maior')
elif n2 > n1 and n3 < n2:
    print_slow(f'{n2} é o maior')
elif n3 > n2 and n1 < n3:
    print_slow(f'{n3} é o maior')    
print('')
if n1 < n2 and n3 > n1:
    print_slow(f'{n1} é o menor')
elif n2 < n2 and n3 > n2:
    print_slow(f'{n2} é o menor')
elif n3 < n2 and n1 > n3:
    print_slow(f'{n3} é o menor')    

