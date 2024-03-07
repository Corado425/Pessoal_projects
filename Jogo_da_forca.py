from random import choice

palavras = ['macaco', 'camaleao', 'cachorro', 'ovelha', 'gato', 'pato', 'sapo', 'vaca', 'tamandua', 'baleia', 'leao',
            'tigre', 'carneiro', 'tubarao', 'papagaio', 'ornitorrinco', 'urubu', 'gaviao', 'falcao', 'galinha', 'galo']
escolha = choice(palavras)
forca = []

print(f'{"Jogo da Forca":^40}')
print(f'\nQuantidade de letras: ')
print()

for letras in escolha:
    forca.append('_')

for letras in forca:
    print(letras, end=' ')
print()

while True:
    rodada = str(input('\nDigite uma letra: g')).lower().strip()
    if rodada in escolha:
        pos = escolha.find(f'{rodada}')
        if escolha.count(rodada) == 1:
            forca[pos] = escolha[pos]
        else:
            quantidade = escolha.count(rodada)
            while True:
                forca[pos] = escolha[pos]
                nova_pos = escolha.find(f'{rodada}', pos+1)
                pos = nova_pos
                quantidade -= 1
                if quantidade == 0:
                    break

    for letras in forca:
        print(letras, end=' ')
    print()

    if forca.count('_') == 0:
        break
