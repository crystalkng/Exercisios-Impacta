valor = float(input('Digite o valor:R$ '))
valordesconto = 0


if valor <= 100:
    valordesconto = valor * 0.05
    valorfinal = valor - valordesconto

elif 101 <= valor <= 500:
    valordesconto = valor * 0.10
    valorfinal = valor - valordesconto

elif valor < 500:
    valordesconto = valor * 0.15
    valorfinal = valor - valordesconto

print ('O valor final é de: R$', valorfinal)



