servidores = [0] * 1000

while True:
    id_servidor = int(input('ID do servidor acessado (0 para parar): '))

    if id_servidor == 0:
        break
    elif 1 <= id_servidor <= 1000:
        servidores[id_servidor - 1] += 1
    else:
        print('ID inválido')
for i in range(1000):
    print(f'Servidor {i+1}: {servidores[i]} acesso(s)')