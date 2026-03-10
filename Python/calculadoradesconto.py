print('*******************')
print('Calculadora de desconto')
print('*******************')

precoproduto = float(input('Digite o valor do produto: '))
valordesconto = precoproduto  * 0.10
print ('O valor descontado é de: R$', valordesconto)
precofinal = precoproduto - valordesconto
print('Preço inificial: R$', precoproduto, '|', 'Desconto: ', valordesconto,'%', '|', 'Preço final: R$', precofinal)   
