import time
def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.09)  # Ajuste o tempo de atraso conforme necessário
s = float(input('Digite o seu salário: '))
a1 = s * 0.10 + s 
a2 = s * 0.15 + s
if s >= 1.251:
    print_slow(f'Seu salário aumentou para {a1:.3f}')
else:
    print_slow(f'O seu salário aumentou para {a2:.4f}')   