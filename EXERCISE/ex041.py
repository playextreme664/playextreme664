nasc = int(input('Digite sua data de nascimento: '))
cat = 2026 - nasc
if cat <= 9:
    print('Você está na categoria Mirim! ')
elif cat <= 14 and cat > 9:
    print('Você está na categoria Infantil!')    
elif cat <= 19 and cat > 14:
    print('Você está na categoria Junior!')
elif cat == 20:    
    print('Você está na categoria Sênior!')
elif cat > 20:
    print('Você está ma categoria Master!')
