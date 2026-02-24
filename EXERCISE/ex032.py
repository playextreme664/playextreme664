import time
def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.09)  # Ajuste o tempo de atraso conforme necessário
ano = int(input('Digite o ano: '))
n = ano % 4
if n == 0:
    print_slow(f'O ano de {ano} é bissexto')
else:
    print_slow(f'O ano de {ano} não é bissexto')
