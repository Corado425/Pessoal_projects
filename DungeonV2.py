from random import randint, choice
from time import sleep


class Protagonista:
    def __init__(self, nome, vivo=True, level=0, poder=20, vida=100):
        self.nome = nome
        self.vivo = vivo
        self.level = level
        self.poder = poder
        self.vida_max = vida
        self.vida_atual = self.vida_max

    def atacar(self, inimigo):
        print('-=' * 50)
        sleep(2)
        print('Sua vez de atacar! Pressione ENTER para rolar o dado!')
        input()
        print('Rolando o dado...')
        sleep(2)
        d20 = randint(1, 20)
        print(f'\nVocê tirou {d20} no d20!')
        sleep(2)

        if 1 <= d20 <= 5:
            dano = randint(1, 6)
            print(f'\n{inimigo.nome} desviou do ataque e deu \033[33m{dano:.2f} de dano\033[m no seu HP')
            self.vida_atual -= dano
            if self.vida_atual <= 0:
                self.vivo = False

        elif 6 <= d20 <= 9:
            dano = self.poder * 0.5
            print(f'\n{inimigo.nome} bloqueou parcialmente o seu ataque, tomando apenas '
                  f'\033[33m{dano:.2f} de dano físico\033[m')
            inimigo.vida -= dano

        elif 10 <= d20 <= 17:
            dano = self.poder
            print(f'\nVocê acertou {inimigo.nome} em cheio, causando \033[33m{dano:.2f} de dano\033[m físico!')
            inimigo.vida -= dano

        else:
            d6 = randint(1, 6)
            bonus = 1 + (d6 * 10 / 100)
            dano = self.poder * bonus
            print('\nHabilidade \033[35mHEAVY ATTACK\033[m ativada! Bonus de 1d6 a mais de dano!')
            sleep(2)
            print('\nPressiona ENTER para rolar o dado!')
            input()
            print('Rolando o dado...')
            sleep(2)
            print(f'\nBônus de \033[35m{d6*10}%\033[m ativado!')
            sleep(2)
            print(f'\nVocê acertou um golpe certeiro na cabeça de {inimigo.nome}, causando '
                  f'\033[33m{dano:.2f} de dano\033[m físico e a mesma quantidade em dano emocional!')
            inimigo.vida -= dano

        if inimigo.vida > 0:
            print('-=' * 50)
            sleep(2)
            print(f'\nVida atual de {self.nome}: {self.vida_atual:.2f} HP')
            print(f'Vida atual de {inimigo.nome}: {inimigo.vida:.2f} HP\n')
        else:
            print('-=' * 50)
            sleep(2)
            print(f'\nVocê matou {inimigo.nome}!\n')
            inimigo.vivo = False
            print('-=' * 50)

    def level_up(self):
        if self.vida_atual < self.vida_max:
            self.vida_atual += self.vida_max * 0.15

            if self.vida_atual > self.vida_max:
                self.vida_atual = self.vida_max

            elif self.vida_atual <= self.vida_max * 0.25:
                self.vida_atual += self.vida_max * 0.10

        self.vida_max *= 1.15
        self.level += 1
        self.poder *= 1.20

        return print(f'{self.nome} subiu de nível!\nStatus atual:\n'
                     f'\033[36mNível\033[m = {self.level}\n'
                     f'\033[35mPoder\033[m = {self.poder:.2f}\n'
                     f'\033[32mVida Atual/Máxima:\033[m {self.vida_atual:.2f}/{self.vida_max:.2f} HP')


class Goblin:
    nomes_goblin = ['\033[31mStradald\033[m', '\033[31mCrokokt\033[m', '\033[31mBregonk\033[m',
                    '\033[31mXiglegz\033[m', '\033[31mUbhigs\033[m']

    def __init__(self, vivo=True):
        self.nome = choice(self.nomes_goblin)
        self.nomes_goblin.remove(self.nome)  # Feito para não repetir os nomes
        self.vivo = vivo
        self.poder = randint(10, 15)
        self.vida = randint(40, 50)

    def atacar(self, protagonista):

        print('-=' * 50)
        sleep(2)
        print(f'Vez de {self.nome} atacar!')
        sleep(2)
        d20 = randint(1, 20)
        sleep(2)

        if 1 <= d20 <= 5:

            print(f'\n{self.nome} errou o ataque!')
            sleep(2)
            print(f'\n{protagonista.nome} ativou \033[35mATAQUE DE OPORTUNIDADE\033[m')
            sleep(2)
            print('\nPressione ENTER para rolar 1d6!')
            input()
            print('Rolando dado...')
            dano = randint(1, 6)
            sleep(2)
            print(f'\nVocê causou \033[33m{dano} de dano\033[m no HP de {self.nome}')
            self.vida -= dano
            if self.vida <= 0:
                self.vivo = False

        elif 6 <= d20 <= 9:
            dano = self.poder * 0.5
            print(f'\n{self.nome} acertou um ataque fraco! {protagonista.nome} recebeu \033[33m{dano:.2f} de dano\033[m'
                  f' físico')
            protagonista.vida_atual -= dano

        elif 10 <= d20 <= 17:
            dano = self.poder
            print(f'\n{self.nome} acertou {protagonista.nome} em cheio, causando \033[33m{dano:.2f} de dano\033[m '
                  f'físico!')
            protagonista.vida_atual -= dano

        else:
            dano = self.poder * 1.5
            print(f'\n{self.nome} ativou a habilidade \033[35mDILACERAR\033[m que causa 50% a mais de dano!')
            print(f'\n{protagonista.nome} sofreu \033[33m{dano:.2f} de dano\033[m físico!')
            protagonista.vida_atual -= dano

        if protagonista.vida_atual > 0:
            print('-=' * 50)
            sleep(2)
            print(f'\nVida atual de {protagonista.nome}: {protagonista.vida_atual:.2f} HP')
            print(f'Vida atual de {self.nome}: {self.vida:.2f} HP\n')

        else:
            print('-=' * 50)
            sleep(2)
            print(f'\nVocê foi morto por {self.nome}!\n')
            protagonista.vivo = False
            print('-=' * 50)

    def info(self, prota):
        return print(f'{prota.nome}, agora você enfrentará {self.nome}, um goblin com {self.poder} FC e {self.vida} HP')


player = Protagonista(input('Qual o seu nome, guerreiro? '))
player.nome = f'\033[034m{player.nome}\033[m'
dungeon = [Goblin() for x in range(3)]

for goblin in dungeon:

    if player.vivo:
        goblin.info(player)

    while goblin.vivo and player.vivo:

        if goblin.vivo and player.vivo:

            if player.vivo:
                player.atacar(goblin)
            else:
                break

            if goblin.vivo:
                goblin.atacar(player)
            else:
                break

if player.vivo:
    print(f'\nVocê completou a dungeon\n')
    player.level_up()
else:
    print('\nGAME OVER!')
