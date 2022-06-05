# Реализовать базовый класс Worker (работник).
#   определить атрибуты: name, surname, position (должность), income (доход);
#   последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
#   оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
#   в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
#   и дохода с учётом премии (get_total_income);
#
# проверить работу примера на реальных данных:
#   создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:

    @staticmethod
    def __income(salary=0, bonus=0):
        return {'salary': salary, 'bonus': bonus}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = self.__income(0, 0)

    def set_salary(self, salary, bonus):  # , wage, bonus
        self.income = self.__income(salary, bonus)


class Position(Worker):

    def __init__(self, *args):
        super().__init__(*args)

    def get_full_name(self):
        return " ".join([self.name, self.surname])

    def get_total_income(self):
        return self.income.get("salary") + self.income.get("bonus")


# Создаем worker
worker1 = Worker('Jhon', 'Smith', 'Driver')
print(f'I am {worker1.name} {worker1.surname}, {worker1.position}')

worker1.set_salary(salary=100, bonus=10)
print(f'my salary is {worker1.income.get("salary")} and my bonus is {worker1.income.get("bonus")}')

# Создаем position
pos = Position('Daniel', 'Woo', 'Accountant')
pos.set_salary(1000, 100)
print(f'I am {pos.name} {pos.surname}, {pos.position}')
print(f'My full name is: {pos.get_full_name()}')
print(f'My full salary is: {pos.get_total_income()}')
