# Ты разрабатываешь программное обеспечение для сети магазинов.
# Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики,
# такие как адрес, название и ассортимент товаров. Ваша задача — создать класс Store,
# который можно будет использовать для создания различных магазинов.

class Store ():
    def __init__(self, address, name):
        self.address = address
        self.name = name
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def delete_item(self, item_name):
        if item_name in self.items:
            del self.items [item_name]

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items [item_name] = new_price

store1 = Store("Киевское ш., 127к3", "Магазин мебели")
store1.add_item ("стол журнальный", " 8700 руб.")
store1.add_item("тумбочка прикроватная", "17000 руб.")
store1.add_item("диван", "83000 руб.")

store2 = Store("Тверской бульвар, 4", "Магазин Продукты")
store2.add_item ("яблоки", " 230 руб.")
store2.add_item("бананы", "170 руб.")
store2.add_item("виноград", "300 руб.")

store3 = Store("ул. Цветочная, 10", "Цветочный магазин Фиалка")
store3.add_item ("роза", "100 руб.")
store3.add_item("гладиолус", "250 руб.")
store3.add_item("сирень", "500 руб.")
store3.add_item("подсолнух", "500 руб.")
print(store3.items)

print(store3.get_price("роза"))
print(store3.get_price("каллы"))

store3.delete_item ("роза")
print(store3.items)

store3.update_price("гладиолус", "400")
print(store3.items)




