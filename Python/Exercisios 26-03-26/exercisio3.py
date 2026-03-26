temperatura = float(input('Digite a temperatura ambiente em C(Celsius): '))

if temperatura <= 0:
    print('Congelante')

elif 0 <= temperatura <= 15:
    print ('Frio')

elif 16 <= temperatura <= 25:
    print ('Agradavel')

else:
    print ('Quente')


