print('********************************')
print('CALCULADORA DE VALOR COM IMPOSTO')
print('********************************')

valorbase = float(input('Digite o valor base do produto: R$'))
valorimposto = valorbase * 0.18
print('Valor do imposto: ', valorimposto)
valorfinal = valorbase + valorimposto
print('Preço base : R$',valorbase, '|', 'Imposto: 18%', '|', 'Preço Final: R$', valorfinal)
