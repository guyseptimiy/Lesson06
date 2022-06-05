# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.status = 'stopped'
        self.speed = 0

    def go(self):
        self.status = 'running'
        print(f'{self.name}: running')

    def stop(self):
        self.status = 'stopped'
        print(f'{self.name}: stopped')

    def increase_speed(self, gap=10):
        self.speed += gap

    def decrease_speed(self, gap=10):
        self.speed -= gap
        if self.speed < 0:
            self.speed = 0
            print(f'{self.name}: EMERGENCY breaking!')
        if self.speed == 0:
            self.stop()

    def show_speed(self):
        print(f'{self.name}: current speed is: {self.speed}')
        return self.speed

    def turn(self, direction):
        print(f'{self.name}: turned to the {direction}')


class TownCar(Car):

    def __init__(self, *args):
        super().__init__(*args)
        self.__max_speed = 60

    def show_speed(self):
        print(f'{self.name}: current speed is: {self.speed}')
        if self.speed > self.__max_speed:
            print(f'{self.name}: current speed larger than speed limit {self.__max_speed}')
        return self.speed


class SportCar(Car):

    def __init__(self, *args):
        super().__init__(*args)
        self.__max_speed = 200


class WorkCar(Car):

    def __init__(self, *args):
        super().__init__(*args)
        self.__max_speed = 40

    def show_speed(self):
        print(f'{self.name}: current speed is: {self.speed}')
        if self.speed > self.__max_speed:
            print(f'{self.name}: current speed larger than speed limit {self.__max_speed}')
        return self.speed


class PoliceCar(Car):

    def __init__(self, *args):
        super().__init__(*args)
        self.is_police = 1
        self.__max_speed = 200


tc = TownCar('Ford Fiesta', 'Blue')
tc.go()
tc.increase_speed(10)
tc.show_speed()
tc.increase_speed(70)
tc.show_speed()
tc.turn('rigth')
tc.turn('left')
tc.decrease_speed(10)
tc.decrease_speed(60)
tc.decrease_speed(20)

print()

wc = WorkCar('Ford F-350', 'Gray')
wc.go()
wc.increase_speed(10)
wc.show_speed()
wc.increase_speed(70)
wc.show_speed()
wc.turn('rigth')
wc.turn('left')
wc.decrease_speed(10)
wc.decrease_speed(60)
wc.decrease_speed(20)

print()

sc = SportCar('Ford Mustang', 'Red')
sc.go()
sc.increase_speed(10)
sc.show_speed()
sc.increase_speed(70)
sc.show_speed()
sc.turn('rigth')
sc.turn('left')
sc.decrease_speed(10)
sc.decrease_speed(60)
sc.decrease_speed(20)

print()

pc = PoliceCar('Ford Explorer', 'Black')
pc.go()
pc.increase_speed(10)
pc.show_speed()
pc.increase_speed(70)
pc.show_speed()
pc.turn('rigth')
pc.turn('left')
pc.decrease_speed(10)
pc.decrease_speed(60)
pc.decrease_speed(20)
