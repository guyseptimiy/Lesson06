# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('draw started')


class Pen(Stationery):

    def draw(self):
        print(f'{self.title} pen drawing')


class Pencil(Stationery):

    def draw(self):
        print(f'{self.title} pencil drawing')


class Handle(Stationery):

    def draw(self):
        print(f'{self.title} handle drawing')


pen = Pen('Red')
pen.draw()

pencil = Pencil('Blue')
pencil.draw()

handle = Handle('Brown')
handle.draw()
