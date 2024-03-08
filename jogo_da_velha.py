velha = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]


def jogo(tabela):
    count = 1
    for pos in tabela:
        if count < 3:
            print(f' {pos} ', end=' | ')
            count += 1
        else:
            print(f' {pos} ')
            count = 1
    print()


def player1(tabela1):
    escolha = int(input('Em qual posição deseja jogar o X? '))
    posicao = tabela1.index(escolha)
    tabela1[posicao] = '\033[31mX\033[m'


def player2(tabela1):
    escolha = int(input('Em qual posição deseja jogar o O? '))
    posicao = tabela1.index(escolha)
    tabela1[posicao] = '\033[32mO\033[m'


jogo(velha)
while True:
    player1(velha)
    jogo(velha)
    if velha[0] == velha[1] == velha[2] or velha[3] == velha[4] == velha[5] or velha[6] == velha[7] == velha[8]:
        break
    elif velha[0] == velha[3] == velha[6] or velha[1] == velha[4] == velha[7] or velha[2] == velha[5] == velha[8]:
        break
    if velha[0] == velha[4] == velha[8] or velha[2] == velha[4] == velha[6]:
        break
    player2(velha)
    jogo(velha)
    if velha[0] == velha[1] == velha[2] or velha[3] == velha[4] == velha[5] or velha[6] == velha[7] == velha[8]:
        break
    elif velha[0] == velha[3] == velha[6] or velha[1] == velha[4] == velha[7] or velha[2] == velha[5] == velha[8]:
        break
    if velha[0] == velha[4] == velha[8] or velha[2] == velha[4] == velha[6]:
        break
