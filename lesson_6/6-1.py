from time import sleep


class TrafficLight:
    _color = ["Красный", "Желтый", "Зеленый"]

    def running(self):
        count = 0
        while True:
            print(f"{self._color[count]}")
            if count == 0:
                sleep(7)
            elif count == 1:
                sleep(2)
            elif count == 2:
                sleep(10)
                count = 0
                continue
            count += 1


tl = TrafficLight()
tl.running()
