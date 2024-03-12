n = int(input('Digite um valor em metros: '))
c = n / 100
m = n / 1000
print('{} metros é igual a {:.3f} centimetros,'
      '\n{} metros é igual a {:.3f} milimetros'.format(n, c, n, m))
