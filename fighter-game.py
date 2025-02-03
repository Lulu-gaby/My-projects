from abc import ABC, abstractmethod
from nntplib import decode_header


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def get_damage(self):
        pass


class Sword(Weapon):
    def attack(self):
        print(f"Боец наносит удар мечом!")

    def get_damage(self):
        return 3


class Bow(Weapon):
    def attack(self):
        print("Боец делает выстрел из лука!")

    def get_damage(self):
        return 2


class Fighter():
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def choosing_weapon(self):
        print(f"Боец {self.name} выбирает оружие")

    def fight(self, monster):
        self.weapon.attack()
        damage = self.weapon.get_damage()
        monster.take_damage(damage)

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon
        print(f"Боец {self.name} сменил оружие")


class Monster():
    def __init__(self, max_health):
        self.max_health = max_health
        self.health = max_health
        self.dead = False

    def take_damage(self, damage):
        if self.dead:
            return

        self.health -= damage
        if self.health > 0:
            print(f"Монстр ранен! Осталось здоровья: {self.health}")
        else:
            self.die()

    def die(self):
        print("Монстр умер!")
        del self

sword = Sword()
bow = Bow()

fighter = Fighter("Илья Муромец", sword)
monster = Monster(10)

fighter.choosing_weapon()
fighter.fight(monster)
fighter.fight(monster)
fighter.fight(monster)

fighter.change_weapon(bow)
fighter.fight(monster)

