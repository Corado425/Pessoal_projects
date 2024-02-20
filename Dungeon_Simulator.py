from random import *
from time import sleep


# Classes dos personagens
class Protagonist:
    def __init__(self):
        self.type = 'main'
        self.name = ''
        self.health_points = randint(90, 200)
        self.combat_power = randint(10, 30)

    def get_info(self):
        return print(f'\033[32mSir {self.name}, you have {self.health_points} HP and {self.combat_power} '
                     f'CP score!\033[m')


class Enemy:
    def __init__(self):
        enemies = ['Goblin', 'Bandit', 'Boss']
        self.type = choice(enemies)
        self.health_points = 0
        self.combat_power = 0
        if self.type == 'Goblin':
            self.health_points = randint(35, 45)
            self.combat_power = randint(5, 15)

        elif self.type == 'Bandit':
            self.health_points = randint(50, 85)
            self.combat_power = randint(5, 25)

        else:
            self.health_points = randint(90, 140)
            self.combat_power = randint(20, 35)

    def get_info(self):
        return print(f'\033[31mNow you face a {self.type} with {self.health_points} HP and {self.combat_power} '
                     f'CP score\033[m')


def attack(protagonist, enemy0):

    d20 = randint(1, 20)
    print('-=' * 40)
    sleep(2)
    print(f"\033[32mIt's your turn!\n"
          f"Your d20 rolled {d20}\033[m")
    sleep(2)

    if 1 <= d20 <= 3:  # Pune o atacante com uma perda de 1d4 no HP
        damage = randint(1, 4)
        print(f'\033[32mCRITICAL FAIL, {protagonist.name} lost {damage} HP\033[m')
        protagonist.health_points -= damage

    elif 4 <= d20 < 10:  # O ataque não pega em cheio e causa apenas 30% do CP em dano.
        damage = protagonist.combat_power * 0.3
        print(f'\033[32mNOTHING BUT A SCRATCH, {enemy0.type} lost {damage:.2f} HP\033[m')
        enemy0.health_points -= damage

    elif 10 <= d20 <= 17:  # O ataque pega em cheio e causa 100% do CP em dano.
        damage = protagonist.combat_power
        print(f'\033[32mYOU GOT HIM, {enemy0.type} lost {damage:.2f} HP\033[m')
        enemy0.health_points -= damage

    else:  # d20 = 20, acerto crítico, o ataque causa 30% de dano adicional
        damage = protagonist.combat_power * 1.3
        print(f'\033[1;32mCRITICAL HIT, {enemy0.type} lost {damage:.2f} HP\033[m')
        enemy0.health_points -= damage

    if enemy0.health_points > 0:
        print('-=' * 40)
        print(f'\033[32mYou have {protagonist.health_points:.2f} HP\033[m')
        print(f'\033[31m{enemy0.type} HP is now {enemy0.health_points:.2f}\033[m')

    else:
        print('-=' * 40)
        print('\033[32mYOUR ENEMY IS DEAD. Congratulations!\033[m')


def defend(enemy1, protagonist):

    d20 = randint(1, 20)
    print('-=' * 40)
    sleep(2)
    print(f"\033[31mIt's enemy's turn!\033[m")
    sleep(2)

    if 1 <= d20 <= 4:  # O inimigo erra o ataque, dando a chance do protagonista causar 1d6 de dano.
        damage = randint(1, 6)
        print(f'\033[31mTHE {enemy1.type.upper()} MISSED THE ATTACK!\033[m\n'
              f'\033[32mNow you have got an Opportunity Attack\033[m')
        enemy1.health_points -= damage
        print(f'\033[32mYou dealt {damage} points of damage to the enemy!\033[m')

    elif 5 <= d20 <= 11:  # O inimigo acerta um ataque fraco, que causa 30% do dano.
        damage = enemy1.combat_power * 0.3
        protagonist.health_points -= damage
        print(f'\033[31mLIGHT ATTACK! {enemy1.type} dealt {damage:.2f} points of damage to your life!\033[m')

    elif 12 <= d20 <= 17:  # O inimigo acerta um ataque em cheio, causando 100% do dano.
        damage = enemy1.combat_power
        protagonist.health_points -= damage
        print(f'\033[31mTHE {enemy1.type.upper()} GOT YOU! He dealt {damage:.2f} damage points to your life!\033[m')

    else:  # Acerto crítico do inimigo, causa 30% de dano adicional
        damage = enemy1.combat_power * 1.3
        protagonist.health_points -= damage
        print(f'\033[31mCRITICAL HIT! The {enemy1.type} found an opening at your guard and dealt {damage:.2f} '
              f'damage points to your life!\033[m')

    if protagonist.health_points > 0:
        print('-=' * 40)
        print(f'\033[32mYour HP is now {protagonist.health_points:.2f}\033[m')
        print(f'\033[31m{enemy1.type} has {enemy1.health_points:.2f} HP\033[m')

    else:
        print('-=' * 40)
        print('\033[31mYOU DIED! GAME OVER\033[m')


# Definindo o protagonista
main_character = Protagonist()
main_character.name = input("What's your name, mighty warrior? ")
sleep(1)
print('-=' * 40)
main_character.get_info()
sleep(2)

# Definindo a quantidade de inimigos
dungeon = [Enemy() for enemy in range(3)]

# Combatendo a dungeon
for idx, creatures in enumerate(dungeon):
    enemy = dungeon[idx]

    if main_character.health_points > 0:
        sleep(2)
        print()
        print('-=' * 40)
        enemy.get_info()
        sleep(2)

    while True:

        if enemy.health_points > 0 and main_character.health_points > 0:
            attack(main_character, enemy)
            sleep(1)
        else:
            break

        if main_character.health_points > 0 and enemy.health_points > 0:
            defend(enemy, main_character)
            sleep(1)
        else:
            break
print('GAME FINISHED! Thanks for playing!')
