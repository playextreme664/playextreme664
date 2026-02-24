cs = float(input('Qual o valor da casa? R$'))

sl = float(input('Qual o valor do seu sálario bruto? R$'))

ans = float(input('Em quantos anos você pretende pagar? '))

prest = cs / (ans * 12)

if prest > (sl * 0.3):
    print('Para pagar uma casa no valor de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(cs, ans, prest))
    print('Emprestimo negado!')

else:
    print('Para pagar uma casa no valor de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(cs, ans, prest))
    print('Emprestimo aprovado!')
