import time
def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.09)  # Ajuste o tempo de atraso conforme necessário
l1 = int(input('Digite o primeiro lado: '))
l2 = int(input('Digite o segundo lado: '))
l3 = int(input('Digite o terceiro lado: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print_slow('Com a soma dos lados será possivel formar um triangulo!')
else:
    print_slow('Com a soma dos lados não será possivel formar um triangulo!')

