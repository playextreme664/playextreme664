import time
def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.09)  # Ajuste o tempo de atraso conforme necessário
eu = int(input('Digite um número: '))
n = eu % 2 
if n == 0: 
    print_slow(f'{eu} é um numero PAR')
else:
    print_slow(f'{eu} é um numeo IMPAR')    

