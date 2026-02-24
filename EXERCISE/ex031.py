import time
def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.09)  # Ajuste o tempo de atraso conforme necessário
d = int(input('"Qual a distancia da viagem em KM? '))
n1 = d * 0.50
n2 = d * 0.45
if d <= 200:
    print_slow(f'O preço da viagem será de {n1}')
else:
    print(f'O preço da viagem será de {n2}')    
