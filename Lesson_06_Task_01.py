# Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность
#   первого состояния (красный) составляет 7 секунд,
#   второго (жёлтый) — 2 секунды,
#   третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.

from datetime import datetime
# импортируем работы с циклическими коллекциями
from itertools import cycle
# импортируем получение текущей даты и времени
from time import sleep


class TrafficLight:
    __color = 'Red'

    # цвета Red, Yellow, Green
    __time_of_colors = {'Red': 7, 'Yellow': 2, 'Green': 15}

    # определяем метод запуска
    def running(self):
        # Перебираем цвета в бесконечном цикле работы
        for next_color in cycle(self.__time_of_colors):
            self.__color = next_color

            print(f'{datetime.now()}: Traffic light changed to: {self.__color}')
            sleep(self.__time_of_colors.get(next_color))


trafic_light_obj = TrafficLight()
trafic_light_obj.running()
