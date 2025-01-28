#Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def make_sound(self):
        pass

    def eat(self):
        print (f"{self.name} кушает")

class Bird (Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} чирикает")

    def fly(self):
        print(f"{self.name} летает c размахом крыльев {self.wing_span} метров")

class Mammal (Animal):
    def __init__(self, name, age, speed_run):
        super().__init__(name, age)
        self.speed_run = speed_run

    def make_sound(self):
        print(f"{self.name} рычит")

    def run (self):
        print(f"{self.name} бежит со скоростью {self.speed_run} км/ч")

class Reptile(Animal):
    def __init__(self, name, age, skin_color):
        super().__init__(name, age)
        self.skin_color = skin_color

    def make_sound(self):
        print(f"{self.name} шипит")

    def crawl (self):
        print(f"{self.name} ползет, цвет ее чешуи {self.skin_color}")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo():
    def __init__(self):
        self.animals = []
        self.staff = []


    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} добавлен(а) в список животных Зоопарка")

    def remove_animal (self, animal):
        self.animals.remove(animal)
        print(f"{animal.name} удален(а) из списка животных Зоопарка")


    def add_staff(self, staff_name):
        self.staff.append(staff_name)
        print(f"{staff_name} добавлен(а) в список сотрудников Зоопарка")

    def remove_staff(self, staff_name):
        self.staff.remove(staff_name)
        print(f"{staff_name} удален(а) из списка сотрудников Зоопарка")

    def get_info_animals(self):
        print("Список животных в Зоопарке:")
        for animal in self.animals:
            print(f"-", animal.name)

    def get_info_staff(self):
        print("Список сотрудников в Зоопарке:")
        for staff in self.staff:
            print(f"-", staff.name)



class Zookeeper():
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")

    def __str__(self):
        return f"Хранитель зоопарка: {self.name}"

class Veterinarian():
    def __init__(self, name,):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")

    def __str__(self):
        return f"Ветеринар: {self.name}"



bird = Bird("Голубь", 4, 1)
mammal = Mammal("Рысь", 3, 15)
reptile = Reptile("Анаконда", 6, "зеленый")

animals = [bird, mammal, reptile]

for animal in animals:
    animal.make_sound()

bird.fly()
mammal.run()
reptile.crawl()

zookeeper = Zookeeper("Мария")
vet = Veterinarian ("Доктор Шмидт")

zoo = Zoo ()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

zoo.add_staff(zookeeper)
zoo.add_staff(vet)

zookeeper.feed_animal(mammal)
vet.heal_animal(bird)

zoo.get_info_animals()
zoo.get_info_staff()