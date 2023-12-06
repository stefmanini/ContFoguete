import time


def contagem_regressiva(nome_foguete):
    print(f'Contagem regressiva para o lançamento do foguete {nome_foguete}...\n')

    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)

    print(f'Lançamento do foguete {nome_foguete} iniciado!')


contagem_regressiva(input("Digite o nome do foguete: "))