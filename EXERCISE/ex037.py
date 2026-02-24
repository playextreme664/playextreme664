n1 = int(input('Digite um número: '))
print('1 para binário\n2 para octal\n3 para hexadecimal')
n2 = int(input('Qual será a base da conversão: '))
if n2 == 1:
    print('O número que você digitou em binário é')
    print((bin(n1)[2:]))
elif n2 == 2:
    print('O número que você digitou em octal é')
    print(oct(n1)[2:])
elif n2 == 3:
    print('O número que você digitou em hexadecimal é ') 
    print(hex(n1)[2:])
else:
    print('Opcão invalida. Tente novamente. ')
        