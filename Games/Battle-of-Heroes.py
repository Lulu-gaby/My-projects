# Требования:
# Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.
# Игра должна быть реализована как консольное приложение.
# Классы:
# Класс Hero:
# Атрибуты:
# Имя (name)
# Здоровье (health), начальное значение 100
# Сила удара (attack_power), начальное значение 20
# Методы:
# attack(other): атакует другого героя (other), отнимая здоровье в размере своей силы удара
# is_alive(): возвращает True, если здоровье героя больше 0, иначе False
# Класс Game:
# Атрибуты:
# Игрок (player), экземпляр класса Hero
# Компьютер (computer), экземпляр класса Hero
# Методы:
# start(): начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет.
# Выводит информацию о каждом ходе (кто атаковал и сколько здоровья осталось у противника)
# и объявляет победителя.

import random
import time

class Hero:
    def __init__(self, name, health = 100, attack_power = 20):
        self.name = name
        self.health = health
        self.attack_power = attack_power


    def attack(self, other):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит урон {damage}")


    def is_alive(self):
       return self.health>0

class Player(Hero):
    def __init__(self, name):
        super().__init__(name)

    def take_turn(self, other):
        input("Нажмите Enter, чтоб атаковать")
        self.attack(other)
        print(f"{self.name} атаковал {other.name}. У {other.name} осталось {self.health} здоровья")
        time.sleep(1)

class Computer(Hero):
    def __init__(self):
        super().__init__("Компьютер")

    def take_turn(self, other):
        print("Ход делает Компьютер")
        time.sleep(1)
        self.attack(other)
        print(f"{self.name} атаковал {other.name}. У {other.name} осталось {self.health} здоровья")
        time.sleep(1)

class Game:
    def __init__(self, player_name):
        self.player = Player (player_name)
        self.computer = Computer()

    def start(self):
        print(f"Играют {self.player.name} против {self.computer.name}. Битва началась!")

        while self.player.is_alive() and self.computer.is_alive():
            self.player.take_turn(self.computer)
            if not self.computer.is_alive():
                print(f"{self.computer.name} убит. {self.player.name} вы одержали победу!")
                break


            self.computer.take_turn(self.player)
            if not self.player.is_alive():
                print(f"{self.player.name} убит. {self.computer.name} вы одержали победу!")
                break

player_name = input("Введите имя вашего Героя: ")
game = Game(player_name)
game.start()









