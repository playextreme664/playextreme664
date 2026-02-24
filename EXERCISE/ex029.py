import time
def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.09)  # Ajuste o tempo de atraso conforme necessário
v = int(input('Qual foi a velociade do carro? '))
m = (v - 80) * 7.0
if v > 80:
    print_slow('Você foi multado! ')
    time.sleep(2)
    print('')
    print_slow(f'O Valor da multa será de {m}R$')
else:
    print_slow('Tudo bem, você não foi multado')



