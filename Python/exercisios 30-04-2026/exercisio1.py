'''
Um sistema monitora tentativas de login em um servidor.
O usuário deve informar repetidamente:
• 1 → tentativa válida
• 2 → tentativa suspeita
Digite 0 para encerrar.
Ao final, mostre:
• total de tentativas válidas
• total de tentativas suspeitas
'''

validas = 0
suspeitas = 0

while True:
    entrada = int(input('Digite (1 = Válida, 2 = Suspeita , 0 = Encerrar): '))

    if entrada == 0:
        break
    elif entrada == 1:
        validas += 1
    elif entrada == 2:
        suspeitas += 1

print(f'Total Válidas: {validas}')
print(f'Total Suspeitas: {suspeitas}')
        
