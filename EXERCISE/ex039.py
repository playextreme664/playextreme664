nasc = int(input('Digite o seu ano de nascimento: '))
adian = nasc - 2008
atr = (nasc - 2008) * -1
if nasc == 2008:
    print('Está na hora de você se alistar!')
elif nasc > 2008:
    print('Você ainda vai se alistar')
    print('Falta {} anos para você se alistar'.format(adian))
elif nasc < 2008:
    print('Já passou da hora de você se alistar!')
    print('Você está {} anos atrasado do tempo de alistamento '.format(atr))   
