class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(F"Запуск {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(F"Запуск {self.title}")


class Handle(Stationery):

    def draw(self):
        super().draw()
        print(F"Печатает {self.title}")


a = Stationery("a")
a.draw()
obj_1 = Pen("ручка")
obj_1.draw()

obj_2 = Pencil("карандаш")
obj_2.draw()

obj_3 = Handle("жирный маркер")
obj_3.draw()
