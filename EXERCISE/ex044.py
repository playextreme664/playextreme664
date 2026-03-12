valor = float(input('Digite o valor do produto:R$ '))
print('[1] A vista no dinheiro: 10% de desconto')
print('[2] A vista no cartão: 5% de desconto')
print('[3] Em até 2x no cartão sem juros')
print('[4] Em até 3x ou mais  no cartão: 20% de juros')
pag = int(input('Qual a forma de pagamento? '))
din = valor * 0.90
cart = valor * 0.95
tres = valor * 0.20 + valor
if pag == 1:
    print('A vista no dinheiro fica R${}'.format(din))
elif pag == 2:
    print('A vista no cartão fica R${}'.format(cart))    
elif pag == 3:
    print('Em até 2x no cartão fica R${}'.format(valor))
elif pag == 4:
    print('Em 3x ou mais no cartão fica R${}'.format(tres))