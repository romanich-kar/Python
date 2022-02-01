"""1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод."""

from itertools import cycle
from time import sleep

class TrafficLight:
    colours_line = ('Red', 'Yellow','Green')
    time_line = (7, 2 ,5)

    def __init__(self, colour):
        self.__colour = colour

    def running(self):
        my_cycle = cycle(self.colours_line)
        for traffic_colour in my_cycle:
            print('Traffic light: ', self.__colour)
            sleep(self.time_line[self.colours_line.index(self.__colour)])
            self.__colour = next(my_cycle)

my_traffic = TrafficLight('Red')
my_traffic.running()
